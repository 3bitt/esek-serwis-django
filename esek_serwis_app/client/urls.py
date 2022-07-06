from django.contrib import admin
from django.urls import path, include

from .views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView


app_name = 'client'

urlpatterns = [
    path('detail/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),
    path('detail/<int:pk>/update', ClientUpdateView.as_view(), name='client-update'),
    path('detail/<int:pk>', ClientDetailView.as_view(), name='client-detail'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('', ClientListView.as_view(), name='client-list'),
]

