from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    email               = models.EmailField(max_length=254, unique=True, blank=False)
    full_name           = models.CharField(max_length=254, blank=False)
    company_name        = models.CharField(max_length=254, blank=False)
    industry            = models.CharField(max_length=254, blank=False)
    position            = models.CharField(max_length=254, blank=False)
    city_headquarters   = models.CharField(max_length=254, blank=False)
    num_employees       = models.IntegerField(blank=False)
    phone_number        = PhoneNumberField(blank=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
