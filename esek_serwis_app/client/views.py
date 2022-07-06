from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Client
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
    
    def get_success_url(self):
        return reverse_lazy('client:client-detail', kwargs={'pk': self.kwargs['pk']})
    
class ClientDeleteView(generic.DeleteView):
    model = Client
    success_url = reverse_lazy('client:client-list')
