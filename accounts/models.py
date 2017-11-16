from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class ClientManager(BaseUserManager):
    def create_user(self, email, full_name, company_name, industry, position, city_headquarters, num_employees, phone_number, password=None):
        if not email:
            raise ValueError("Clients must have an email address.")
        if not full_name:
            raise ValueError("Clients must have a full name.")
        client_obj = self.model(
            email = self.normalize_email(email)
        )
        client_obj.set_unusable_password()
        client_obj.full_name = full_name
        client_obj.company_name = company_name
        client_obj.industry = industry
        client_obj.position = position
        client_obj.city_headquarters = city_headquarters
        client_obj.num_employees = num_employees
        client_obj.phone_number = phone_number
        client_obj.save(self._db)
        return client_obj

class Client(AbstractBaseUser):
    email               = models.EmailField(max_length=254, unique=True)
    full_name           = models.CharField(max_length=254, blank=True)
    company_name        = models.CharField(max_length=254, blank=True)
    industry            = models.CharField(max_length=254, blank=True)
    position            = models.CharField(max_length=254, blank=True)
    city_headquarters   = models.CharField(max_length=254, blank=True)
    num_employees       = models.IntegerField(blank=True)
    phone_number        = PhoneNumberField(blank=True)

    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'    # email acts as a username
    REQUIRED_FIELDS = ['full_name', 'company_name' , 'industry', 'position', 'city_headquarters', 'num_employees', 'phone_number']

    objects = ClientManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
