from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.TextChoices):
    TECH = 'Tech'
    FOOD = 'Food'
    HOME = 'Home'


class Product(models.Model):
    name = models.CharField(max_length=50, default="", blank=False)
    description =models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=7 , decimal_places=2, blank=False)
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=50, choices=Category.choices, blank=False)
    stock = models.IntegerField(default=0)
    created_at =models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # quantity =
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name