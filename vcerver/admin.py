from django.contrib import admin

from vcerver.models import *

class URLInline(admin.TabularInline):
    model = URL
    extra = 5

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 5

class ContactAdmin(admin.ModelAdmin):
    inlines = (URLInline, PhoneInline)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Company)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(URL)

