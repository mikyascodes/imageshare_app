from django import forms
from django.contrib.auth.models import User
from .models import Memeber
from Home.models import Imagepage
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model =Memeber
        fields = ['username', 'email', 'password1', 'password2', 'profile_pic']
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Memeber
        fields = ['username', 'email']

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model=Imagepage
        fields= ['img','name','description','post_date']
