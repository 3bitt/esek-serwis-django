from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Client, ClientAddress

class ClientListView(generic.ListView):
    queryset = Client.objects.all().order_by('-registration_date')
    template_name = 'client/html/client_list.html'
    
class ClientCreateView(generic.CreateView):
    model = Client
    template_name = 'client/html/client_create.html'
    fields = '__all__'
    success_url = reverse_lazy('client:client_list')