from django import forms
from django.forms.widgets import TextInput
from .models import ContactModel

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, widget=TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(max_length=40, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))


    