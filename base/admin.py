from django.contrib import admin
from .models import Contact
# Register your models here

class ContactModel(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'subject','contact_date')
    list_filter = ('name','contact_date',)
admin.site.register(Contact,ContactModel)
