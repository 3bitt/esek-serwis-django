from django.contrib import admin
from django.urls import path, include

from .views import ClientCreateView, ClientListView


app_name = 'client'

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create')
]

