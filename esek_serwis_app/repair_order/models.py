from enum import Enum
from django.db import models

from client.models import Client


class RepairOrder(models.Model):
    
    class Status(models.TextChoices):
        NEW = 'NEW', 'Nowy'
        IN_PROGRESS = 'IN_PROGRESS', 'W trakcie naprawy'
        FIXED = 'FIXED', 'Naprawiony'
        CLOSED = 'CLOSED', 'Zakończone'
        
    client = models.ForeignKey(Client, verbose_name="client", on_delete=models.SET_NULL, null=True)
    equipment_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.NEW,
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    fixed_date = models.DateTimeField(editable=False, null=True, blank=True)