from django import forms
from client.models import Client

from repair_order.models import RepairOrder

class RepairOrderCreateForm(forms.ModelForm):

    class Meta:
        model = RepairOrder
        exclude = [
            'created_date',
        ]
        
        fields = [
            'client_id',
            'equipment_name',
            'description',
            'status',
        ]
        
        widgets = {
            'equipment_name': forms.TextInput(attrs= {
                'class': 'input'
            }),
            # 'client_id': forms.ModelChoiceField(
            #     queryset=Client.objects.all().order_by('-registration_date'))
        }