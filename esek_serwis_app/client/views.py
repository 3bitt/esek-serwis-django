from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Client, Address
from .forms import ClientCreateForm


class ClientListView(generic.ListView):
    queryset = Client.objects.all().order_by('-registration_date')
    context_object_name = 'client_list'
    template_name = 'client/html/client_list.html'
    
class ClientCreateView(generic.CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'client/html/client_create.html'
    success_url = reverse_lazy('client:client-list')
    
    def form_valid(self, form: ClientCreateForm):
        if form.is_valid():
            self.object = form.save()
            address_obj = {
                'client_id': self.object,
                'street': form.cleaned_data.pop('street'),
                'home_number': form.cleaned_data.pop('home_number'),
                'zip_code': form.cleaned_data.pop('zip_code'),
                'city': form.cleaned_data.pop('city'),
                'country': form.cleaned_data.pop('country')
            }
            Address.objects.create(**address_obj)    

        return super().form_valid(form)


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'client/html/client_detail.html'
    context_object_name = 'client'
    
class ClientUpdateView(generic.UpdateView):
    model = Client
    template_name = 'client/html/client_update.html'
    form_class = ClientCreateForm
    context_object_name = 'client'
