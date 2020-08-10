from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from login_app.models import *

class signupform(UserCreationForm):
    email=forms.EmailField(label="Email address", required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class updateprofile_form(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password']

class profilepic(forms.ModelForm):
    class Meta:
        model = user_profile
        fields= ['profile_pic']

