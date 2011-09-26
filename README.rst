==============
django-vcerver
==============

Django-vcerver is a VCard server, allowing you to serve virtual cards to
short urls, with the proper content type. Useful for example to link to
from QR Codes to easily add contact info from smartphones.

Uses vObject_, and views based on this snippet_.

.. _vObject: http://vobject.skyhouseconsulting.com
.. _snippet: http://djangosnippets.org/snippets/58/

Install
=======

See env/requirements.txt for pip requirements. Create a virtualenv, create a 
django project, then ::

    pip install git+git@github.com:ecometrica/django-vcerver.git#egg=django-vcerver

And pip-install the dependencies. Then Add vcerver to your INSTALLED_APPS, run
``./manage.py migrate``, and add contacts in the admin, and include the app's
urls to your project's ``urls.py`` (e.g. at ``/c/``).

Not done yet: generate the corresponding QR Codes.

