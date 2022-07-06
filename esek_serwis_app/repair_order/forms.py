from django import forms
from client.models import Client

from repair_order.models import RepairOrder

class CustomClientChoiceField(forms.ModelChoiceField):
    to_field_name='client_name'
    
    def label_from_instance(self, obj):
        return f'{obj.first_name} {obj.last_name} - ID: {obj.id}'


class RepairOrderCreateForm(forms.ModelForm):
    client = CustomClientChoiceField(queryset=Client.objects.all())

    class Meta:
        model = RepairOrder
        
        fields = [
            'client',
            'equipment_name',
            'description',
            'status',
        ]
        
        widgets = {
            'equipment_name': forms.TextInput(attrs= {
                'class': 'input'
            }),
            # 'client': CustomClientChoiceField(
            #     queryset=Client.objects.all())
        }
        