from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import transaction

# Create your models here.

class Category(models.TextChoices):
    TECH = 'Tech'
    FOOD = 'Food'
    HOME = 'Home'


class Product(models.Model):
    name = models.CharField(max_length=50, default="", unique=True, blank=False)
    description =models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=7 , decimal_places=2, blank=False, validators=[MinValueValidator(0.01)])
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=50, choices=Category.choices, blank=False)
    stock_quantity  = models.IntegerField(default=0, validators=[MinValueValidator(0)],)
    created_at =models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    img_url = models.URLField(max_length=200, blank=True, null=True)

    def reduce_stock(self, quantity):
        if quantity > self.stock_quantity:
            raise ValueError("Not enough stock available")
        
        with transaction.atomic():
            self.stock_quantity -= quantity
            self.save()
            self.refresh_from_db()

    def __str__(self):
        return self.name
    

