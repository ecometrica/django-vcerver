"""
Functions for generating individual and group vCards from Django

The functions assume a "Person" object with the following fields:

  firstname
  lastname
  email
  phone
  id (automatically created by Django)

This code uses VObject: http://vobject.skyhouseconsulting.com/
"""

# TODO: urls, phone

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import vobject

from vcerver.models import *

def _vcard_string(person):
    """
    Helper function for vcard views. Accepts a 'person' object 
    with certain attributes (firstname, lastname, email, phone, id)
    and returns a string containing serialized vCard data.
    """
    # vobject API is a bit verbose...
    v = vobject.vCard()
    v.add('n')
    v.n.value = vobject.vcard.Name(family=person.lastname, given=person.firstname)
    v.add('fn')
    v.fn.value = "%s %s" % (person.firstname, person.lastname)
    v.add('email')
    v.email.value = person.email
    #v.add('tel')
    #v.tel.value = person.phone
    #v.tel.type_param = 'WORK'
    v.add('url')
    v.url.value = "http://example.org/people/%s/" % person.id
    output = v.serialize()
    return output
    
def vcard(request, contact_id):
    """
    View function for returning single vcard
    """
    person = get_object_or_404(Contact.objects, card_id=contact_id)
    output = _vcard_string(person)
    filename = "%s.vcf" % (person.card_id)
    response = HttpResponse(output, mimetype="text/x-vCard")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def group_vcard(request):
    """
    View function for returning group vcard
    """
    all = Person.objects.order_by('lastname', 'firstname')
    output = '\n'.join(_vcard_string(one) for one in all)
    response = HttpResponse(output, mimetype="text/x-vCard")
    response['Content-Disposition'] = 'attachment; filename=example_org_people.vcf'
    return response
