from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<contact_id>.*)$', 'vcerver.views.vcard', {}, 'vcard'),
    (r'^(?P<contact_id>.*)/qr$', 'vcerver.views.qr_code', {}, 'qr_code'),
)

