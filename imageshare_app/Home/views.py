from django.shortcuts import render,HttpResponse
from .models import Imagepage

def imagegallery(request):
    images = Imagepage.objects.all()
    return render(request,'imagepage.html',{'image':images})





