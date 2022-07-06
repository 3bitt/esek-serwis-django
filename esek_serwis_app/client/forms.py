from django import forms

from .models import Client

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name',
                  'last_name',
                  'mobile',
                  'email',
                  'street',
                  'home_number',
                  'zip_code',
                  'city',
                  'country',
                  'extra_info'
                  ]