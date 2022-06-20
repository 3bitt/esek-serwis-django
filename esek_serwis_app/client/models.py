from pyexpat import model
from django.db import models



class Client(models.Model):
    firstName = models.TextField(max_length=255)
    lastName = models.TextField(max_length=255)
    mobile = models.TextField(max_length=255)
    email = models.TextField(max_length=255)

    
class ClientAddress(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    street = models.TextField(max_length=255)
    home_number = models.TextField(max_length=255)
    zip_code = models.TextField(max_length=255)
    city = models.TextField(max_length=255)