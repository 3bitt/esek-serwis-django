from django.urls import path, include

from .views import RepairOrderCreate, RepairOrderList


app_name = 'repair_order'
urlpatterns = [
    path('create/', RepairOrderCreate.as_view(), name='repair_order_create'),
    path('', RepairOrderList.as_view(), name='repair_order_list')
]