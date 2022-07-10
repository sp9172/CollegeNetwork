# from rest_framework import serializers
from .models import PersonModel
from django import forms

class PersonForm(forms.ModelForm):
    class Meta:
        model=PersonModel
        fields='__all__'
        labels={
            'fname':'First Name',
            'lname':'Last Name',
            'mobile':'Mobile',
            'username':'Username',
            'password':'Password',
        }
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }


class personloginForm(forms.ModelForm):
    class Meta:
        model=PersonModel
        fields=['username','password']
        labels={
            
            'username':'Username',
            'password':'Password',
        }
        widgets={
          
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

