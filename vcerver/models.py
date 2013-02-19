from django.core.urlresolvers import reverse
from django.db import models

class Contact(models.Model):
    card_id = models.CharField(max_length=64, blank=False,
                              help_text=u"id bit of contact url")
    local_user = models.ForeignKey(
        'auth.User', null=True, blank=True,
        help_text=u"If set, name and email will be taken from the "
                  u"corresponding django User object"
    )
    _firstname = models.CharField(max_length=128, blank=True)
    _lastname = models.CharField(max_length=128, blank=True)
    _email = models.EmailField(blank=True)
    personnal_address = models.ForeignKey('Address', null=True, blank=True)
    work = models.ForeignKey('Company', null=True, blank=True)
    title = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return u"%(card_id)s (%(firstname)s)"%{'card_id': self.card_id,
                                               'firstname': self.firstname}

    @property
    def firstname(self):
        return self.local_user and self.local_user.firstname or self._firstname

    @property
    def lastname(self):
        return self.local_user and self.local_user.lastname or self._lastname

    @property
    def email(self):
        return self.local_user and self.local_user.email or self._email

    def get_absolute_url(self):
        return reverse('vcard', args=[self.card_id])


class Phone(models.Model):
    contact = models.ForeignKey('Contact', null=False, blank=False)
    name = models.CharField(max_length=256, blank=False)
    number = models.CharField(max_length=256, blank=False)

class Company(models.Model):
    name = models.CharField(max_length=256, blank=False)
    address = models.ForeignKey('Address', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Address(models.Model):
    street1 = models.CharField(max_length=256, blank=False)
    street2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=False)
    state = models.CharField(max_length=256, blank=False)
    country = models.CharField(max_length=256, blank=False)
    zipcode = models.CharField(max_length=16, blank=True)

    def __unicode__(self):
        return u'%(street1)s %(street2)s, %(city)s'%self.__dict__

URLTYPES = (("linkedin", "LinkedIn"), 
            ("twitter", "Twitter"),
            ("facebook", "Facebook"),
            ("skype", "Skype"),
            ("gtalk", "GTalk"),
            ("msn", "MSN"),
           )
URLS = {"linkedin": "http://linkedin.com/in/%(username)s",
        "twitter": "http://twitter.com/%(username)s",
        "facebook": "http://facebook.com/%(username)s",
        "skype": "%(username)s",
        "gtalk": "%(username)s",
        "msn": "%(username)s",
       }

class URL(models.Model):
    """
    For twitter, linkedin, etc.
    
    Either fill in the type + username, or fill in an explicit URL
    """
    contact = models.ForeignKey('Contact', null=False)
    type = models.CharField(max_length=16, choices=URLTYPES, blank=True)
    username = models.CharField(max_length=64, blank=True)
    explicit_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.url

    @property
    def url(self):
        if not self.explicit_url and self.type:
            return URLS[self.type]%self.__dict__
        else:
            return self.explicit_url

