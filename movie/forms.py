from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField(max_length='255')
    email = forms.EmailField(required=True)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

def username(self):
    username=self.cleaned_data['username'].lower()
    new=User.objects.filter(username=username)
    if new.count():
        raise ValidationError("Username already exists")
    return username

def email(self):  
    email = self.cleaned_data['email'].lower()  
    new = User.objects.filter(email=email)  
    if new.count():  
        raise ValidationError(" Email Already Exist")  
    return email  

def password2(self):  
    password1 = self.cleaned_data['password1']  
    password2 = self.cleaned_data['password2']  
  
    if password1 and password2 and password1 != password2:  
        raise ValidationError("Password don't match")  
    return password2  
  
def save(self):  
    user = User.objects.create_user(  
    self.cleaned_data['username'],  
    self.cleaned_data['email'],  
    self.cleaned_data['password1']  
    )  
    return user  



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

        