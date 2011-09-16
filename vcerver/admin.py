from django.contrib import admin

from vcerver.models import *

class URLInline(admin.TabularInline):
    model = URL
    extra = 5

class ContactAdmin(admin.ModelAdmin):
    inlines = (URLInline, )

admin.site.register(Contact, ContactAdmin)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(URL)

