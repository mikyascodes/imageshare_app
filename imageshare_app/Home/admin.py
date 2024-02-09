from django.contrib import admin
from .models import Imagepage
# Register your models here.

class ImagePageAdmin (admin.ModelAdmin):
    list_display = ('id','img', 'name', 'description','post_date','user_name')
    list_editable = ('img', 'name', 'description')

admin.site.register(Imagepage, ImagePageAdmin)





