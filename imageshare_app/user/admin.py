from django.contrib import admin
from .models import Memeber

# Register your models here.
class MemeberAdmin (admin.ModelAdmin):
    list_display = ('id','username','email','password','profile_pic','is_staff', 'is_superuser')
    list_editable=('username', 'email')
    list_display_links=None
   
admin.site.register(Memeber,MemeberAdmin)
