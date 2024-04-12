from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post 



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=15)


    

    class Meta:
        model = User
        fields = ["username", "name", "surname",  "email", "phone", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
