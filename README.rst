==============
django-vcerver
==============

Django-vcerver is a VCard server, allowing you to serve virtual cards to
short urls, with the proper content type. Useful for example to link to
from QR Codes to easily add contact info from smartphones.

See env/requirements.txt for pip requirements. Add vcerver to your
INSTALLED_APPS, run ``./manage.py migrate``, and add contacts in the admin, and
include the app's urls to your project's ``urls.py`` (e.g. at ``/c/``).

Not done yet: generate the corresponding QR Codes.

