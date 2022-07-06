from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy

from .models import RepairOrder
from .forms import RepairOrderCreateForm


class RepairOrderList(generic.ListView):
    model = RepairOrder
    queryset = RepairOrder.objects.all().order_by('-created_date')
    context_object_name = 'order_list'
    template_name = 'repair_order/html/repair_order_list.html'


class RepairOrderCreate(generic.CreateView):
    model = RepairOrder
    template_name = 'repair_order/html/repair_order_create.html'
    form_class = RepairOrderCreateForm
    success_url = reverse_lazy('repair_order:repair_order_list')