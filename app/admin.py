from django.contrib import admin
from app.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('firstname','lastname','phone','subject','email','message','pic')

    @admin.register(featured)
    class featured(admin.ModelAdmin):
        pass
@admin.register(faq)
class faq(admin.ModelAdmin):
    pass
  
@admin.register(blog)
class blog(admin.ModelAdmin):
    pass