from django.contrib import admin 
from .models import Enquiry #enquiry is model name


#customize view in database
class EnquiryAdmin(admin.ModelAdmin):  #we will destructure modelAdmin here
    list_display=("name","email","message")  #this variable is in admin

    # again regester (modal, customize view)
admin.site.register(Enquiry, EnquiryAdmin)