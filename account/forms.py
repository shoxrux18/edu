from django import forms
from django.core.exceptions import ValidationError
from .models import User
from validate_email import validate_email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    
    def clean_username(self):
        value=self.cleaned_data.get('username')
        if not value.islower():
            raise ValidationError('Please,Enter in lower case!')
        return value 
     


class RegistrationForm(forms.ModelForm):
    
    confirm=forms.CharField(max_length=100,widget=forms.PasswordInput)
    username=forms.CharField(required=True,max_length=150)
    

    class Meta:
        model=User
        fields=('username','email','password','confirm')
        widgets={
            'password': forms.PasswordInput
        }
    def clean(self):
        data=super().clean()
        if data.get('password') != data.get('confirm'):
            raise ValidationError({"confirm": "Passwords are not the same"})
        return data

    def clean_email(self):
        value=self.cleaned_data.get('email')
        if not validate_email(value):
            raise ValidationError('Please,Enter in right way')
        return value