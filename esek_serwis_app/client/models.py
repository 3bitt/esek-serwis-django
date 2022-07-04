from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)


class ClientAddress(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    home_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)