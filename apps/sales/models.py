from django.db import models
from apps.account.models import LegerAccount
from apps.users.models import CustomUser
from apps.inventory.models import OrderUnit
from apps.organization.models import Tax, Department
# Create your models here.

class SalesItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    measureUnit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)   
    
    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)

    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE)

    status = models.CharField(max_length=100, choices=[
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('partially_received', 'Partially_Received'),
        ('complted', 'Completd'),
    ])
    # This belong to the Leger sub account, by default each account inside of inventory items has an account.
    account = models.ForeignKey(LegerAccount, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    
class Sales(models.Model):
    sales_number = models.PositiveIntegerField()
    created_date = models.DateField(auto_now=True)
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)
    items = models.ForeignKey('SalesItem', on_delete=models.CASCADE)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    approved = models.BooleanField(default=False)
    # ForeignKey to User that should belong to manager user group
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='approved_sales')
    # ForeignKey(User models) only Buyer should be able to create purchase order
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_sales')
    
    status = models.CharField(max_length=20, choices=[
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('sent', 'Sent'),
        ('paritially_Received', 'Paritially Received'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ])
    
    def __str__(self):
        return self.name
   