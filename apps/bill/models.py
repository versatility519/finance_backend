from django.db import models
from apps.supplier.models import Supplier
from apps.inventory.models import OrderUnit
from apps.account.models import LegerAcc    
from apps.organization.models import Tax

class BillDoc(models.Model):
    name = models.CharField(max_length=100)
    docs = models.FileField(upload_to='documents/bills') 

    def __str__(self):
        return str(self.name)
 
class Terms(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
    
class BillItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    unit = models.CharField(max_length=10)
    measure_unit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)
    account = models.ForeignKey(LegerAcc, on_delete=models.CASCADE)
    
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
 
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price  
        self.tax_amount = self.total * self.tax_group.tax_rate if self.tax_group else 0
        super().save(*args, **kwargs) 

# class Bill(models.Model):
#     bill_num = models.CharField(max_length=100)
#     date_created = models.DateField(auto_now=True)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     items = models.ForeignKey(BillItem, on_delete=models.CASCADE)  
#     required_date = models.DateField()
    
#     status = models.CharField(max_length=20, choices=[
#         ('need approval', 'Need approval'),
#         ('approve', 'Approve'),
#         ('waiting Payment', 'Waiting Payment'),
#         ('paid', 'Paid'),
#         ('completed', 'Completed'),
#         ('close', 'Close')
#     ])
#     ship_to = models.CharField(max_length=100, default='Default Value')
#     bill_to = models.CharField(max_length=100, default='Default Value')
#     docs = models.ForeignKey('BillDoc', on_delete=models.CASCADE, null=True, blank=True)
#     terms = models.ForeignKey('Terms', on_delete=models.CASCADE)
 

#     def __str__(self):
#         return str(self.bill_num)
#     def save(self, *args, **kwargs):
#         self.name = f"Bill-{self.bill_num}" 
#         super().save(*args, **kwargs) 
