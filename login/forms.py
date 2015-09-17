from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={ 'required': 'true' }))
    password = forms.CharField(required = True,widget = forms.PasswordInput(attrs={ 'required': 'true' }))
    def clean(self):
        try:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
        except:
            raise forms.ValidationError(u"Blank username or password")
        user = authenticate(username=username, password=password)
        if user is None:
            
            raise forms.ValidationError(u"Wrong username and password")
        return self.cleaned_data
    
class SignUpForm(forms.Form):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={ 'required': 'true' }))
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={ 'required': 'true' }))
    password = forms.CharField(required = True, widget = forms.PasswordInput(attrs={ 'required': 'true' }))
    password_repeat = forms.CharField(required = True, widget = forms.PasswordInput(attrs={ 'required': 'true' }))
    def clean(self):
        password = self.cleaned_data['password']
        password_repeat = self.cleaned_data['password_repeat']
        if password != password_repeat:
            raise forms.ValidationError(u"Passwords do not match.")
        return self.cleaned_data
    def clean_username(self):
        try:
            username = self.cleaned_data['username']
        except:
            raise forms.ValidationError("User name is required")
        user = None
        try:
            user = User.objects.get(username = username)
        except:
            pass
        if user:
            raise forms.ValidationError("Username already exists")
        return self.cleaned_data['username']
    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email)            
        except:
            pass
        if user:
            raise forms.ValidationError("Email already exists")
        return self.cleaned_data['email']
 
    