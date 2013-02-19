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

import tempfile
import qrcode

from django.core.urlresolvers import reverse
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
    if person.personnal_address:
        a = person.personnal_address
        addr = v.add('ADR')
        addr.type_param = 'HOME'
        street = a.street1
        if a.street2: street += ', ' + a.street2
        addr.value = vobject.vcard.Address(
            street=street,
            city=a.city,
            region=a.state,
            code=a.zipcode,
            country=a.country
        )
    if person.work and person.work.address:
        a = person.work.address
        addr = v.add('ADR')
        addr.type_param = 'WORK'
        street = a.street1
        if a.street2: street += ', ' + a.street2
        addr.value = vobject.vcard.Address(
            street=street,
            city=a.city,
            region=a.state,
            code=a.zipcode,
            country=a.country
        )

    if person.email:
        email = v.add('email')
        email.value = person.email
        email.type_param='INTERNET'
    if person.title:
        v.add('title')
        v.title.value = person.title
    if person.work:
        org = v.add('org')
        org.value = (person.work.name, )
    for tel in person.phone_set.all():
        t = v.add('tel')
        t.type_param = tel.name.upper()
        t.value = tel.number
    for url in person.url_set.all():
        u = v.add('url')
        if url.explicit_url:
            u.type_param = 'HOME'
            u.value = url.explicit_url
        else:
            u.type_param = url.type.upper()
            u.value = URLS[url.type]%url.__dict__

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

def qr_code(request, contact_id):
    url = request.build_absolute_uri(reverse('vcard', args=[contact_id]))
    img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_L)
    pipe = tempfile.TemporaryFile()
    img.save(pipe)
    pipe.seek(0)
    filename = "%s.png" % (contact_id)
    response = HttpResponse(pipe.read(), mimetype="image/png")
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
