from django.db import models
from apps.organization.models import Department
from apps.users.models import CustomUser
from apps.supplier.models import Supplier
from apps.organization.models import Tax
from apps.inventory.models import OrderUnit
# Create your models here.

class RequisitionDoc(models.Model):
    name = models.CharField(max_length=100)
    docs = models.FileField(upload_to='documents/requisition')
    def __str__(self):
        return self.name
 
class RequisitionItem(models.Model):
    requisition = models.ForeignKey('Requisition', related_name='items', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    measureUnit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)

    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    
    # quantity is the quantity we want to order
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)

    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    '''
        Reception quantity is to track the quantity we received or we are about to received
        Every time a reception is performed by storekeeper, this quantity will increase and the status of each items should change
    '''
    
    reception_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.price
        self.tax_amount = self.total_amount * self.tax_group.tax_rate
        super().save(*args, **kwargs)


class Requisition(models.Model):
    requisition_number = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    docs = models.ForeignKey('RequisitionDoc', on_delete=models.CASCADE, related_name='requisitionItems')
    # items = models.ForeignKey('RequisitionItem', on_delete=models.CASCADE, related_name='requisitionItems')
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # ForeignKey to User that should belong to manager user group
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='approved_requisitions')
    # ForeignKey to User belonging to every department
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_requisitions')
    
    status = models.CharField(max_length=20, choices=[
        ('inProgress', 'In Progress'),
        ('approved', 'Approved'),
        ('created', 'Created'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel')
    ])
    
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=3)
    total_net_amount = models.DecimalField(max_digits=10, decimal_places=3)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)
   
    def __str__(self):
        return f"Requisition #{self.requisition_number}"
    
    def save(self, *args, **kwargs):
        # Calculate total amounts based on related items
        net_amounts = [item.total_amount for item in self.items.all()]
        tax_amounts = [item.tax_amount for item in self.items.all()]

        self.total_net_amount = sum(net_amounts)
        self.total_tax_amount = sum(tax_amounts)
        self.total_amount = self.total_net_amount + self.total_tax_amount

        super().save(*args, **kwargs)

