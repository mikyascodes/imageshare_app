from django.urls import path
from . import views

urlpatterns = [path("imagepage/", views.imagegallery, name="imagegallery")]
