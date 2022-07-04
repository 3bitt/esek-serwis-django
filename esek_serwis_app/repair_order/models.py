from enum import Enum
from django.db import models

from client.models import Client


class RepairOrder(models.Model):
    
    class Status(models.TextChoices):
        NEW = 'NEW', 'Nowy'
        IN_PROGRESS = 'IN_PROGRESS', 'W trakcie naprawy'
        FIXED = 'FIXED', 'Naprawiony'
        CLOSED = 'CLOSED', 'Zakończone'
        
    client_id = models.ForeignKey(Client, verbose_name="", on_delete=models.DO_NOTHING)
    equipment_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.NEW,
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    