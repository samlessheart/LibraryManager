from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import fields, widgets
from django.forms import Textarea
from django.forms.widgets import PasswordInput, TextInput
from .models import MyUser, Profile 
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    email = forms.EmailField()
    member_id = forms.IntegerField(min_value=1000)
    password = forms.fields.CharField(widget=forms.PasswordInput, min_length=6 )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    

    class Meta:
        model = MyUser
        fields=('email', 'member_id', 'phone', 'fname', 'lname',)

    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('password')
        data2 = cleaned_data.get('password2')        
        if data!=data2:
            self.add_error('password2', 'password must match')
        return self.cleaned_data
        


class LoginForm(forms.Form):
    username = forms.EmailField( help_text='Enter your email or member id ' ,)
    password = forms.CharField(widget=forms.PasswordInput,)


        

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dob',)

        labels = {'dob':"Your Date of Birth", }





