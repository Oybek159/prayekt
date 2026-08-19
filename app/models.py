from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    discount = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    img = models.ImageField(upload_to = 'products/', blank = True, null = True)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.IntegerField()

    last_login = models.DateTimeField(null=True, blank=True)