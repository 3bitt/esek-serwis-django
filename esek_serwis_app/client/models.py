from django.db import models


class Client(models.Model):

    class Meta:
        ordering = ['-registration_date']
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)
    street = models.CharField(max_length=255)
    home_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    extra_info = models.CharField(max_length=255, null=True, blank=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
