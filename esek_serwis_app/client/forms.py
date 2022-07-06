from django import forms

from .models import Client

class ClientCreateForm(forms.ModelForm):
    street = forms.CharField(max_length=255)
    home_number = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    
    
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'mobile', 'email']