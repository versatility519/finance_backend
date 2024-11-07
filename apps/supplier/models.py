from django.db import models
from apps.users.models import CustomUser
from apps.inventory.models import OrderUnit
# Create your models here.

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    address = models.TextField(max_length=200) 
    billing_address = models.TextField(max_length=200)
    shipping_address = models.TextField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.supplier_name)
    
class SupplierItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    sku = models.CharField(max_length=100)

    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    measureUnit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)   
    

    growth = models.BooleanField(default=False)
    growth_fre = models.CharField(max_length=100, choices=[
        ('weekly', 'Weekly'),
        ('bi_weekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
        ('quaters', 'Monthly'),
        ('half_yearly', 'Half-Yearly'),
        ('yearly', 'Yearly'),
    ])
    growth_ercnetage = models.FloatField()

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
    
class SupplierContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    role = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.first_name)
