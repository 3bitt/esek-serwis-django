from django.contrib import admin
from django.urls import path, include

from .views import ClientCreateView, ClientDetailView, ClientListView, ClientUpdateView


app_name = 'client'

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('detail/<int:pk>', ClientDetailView.as_view(), name='client-detail'),
    path('detail/update/<int:pk>', ClientUpdateView.as_view(), name='client-update'),
    path('', ClientListView.as_view(), name='client-list'),
]

