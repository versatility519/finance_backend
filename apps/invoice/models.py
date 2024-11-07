from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum
from apps.inventory.models import IssueUnit
from apps.client.models import Client, Contact
from apps.account.models import LegerAcc
from apps.organization.models import Tax

class InvoiceDoc(models.Model):
    name = models.CharField(max_length=100)
    docs = models.FileField(upload_to='documents/invoices') 

    def __str__(self):
        return str(self.name)
 
class Terms(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
    
class InvoiceItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    measure_unit = models.ForeignKey(IssueUnit, on_delete=models.CASCADE, related_name='invoice_items')
    account = models.ForeignKey(LegerAcc, on_delete=models.CASCADE, related_name='invoice_items')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
   
    total = models.DecimalField(max_digits=10, decimal_places=3)
    
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True, related_name='invoice_items')

    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')
    
    def save(self, *args, **kwargs):

        print("Saving InvoiceItem...")
        self.total = self.quantity * self.price  
        self.tax_amount = self.total * self.tax_group.tax_rate if self.tax_group else 0
        super().save(*args, **kwargs) 

class Invoice(models.Model):
    invoice_num = models.CharField(max_length=100)
    created_date = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    items = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, related_name='invoiceItems')  

    # items = models.ManyToManyField(InvoiceItem, related_name='invoice_items')

    required_date = models.DateField()
    
    status = models.CharField(max_length=20, choices=[
        ('need approval', 'Need approval'),
        ('approve', 'Approve'),
        ('waiting Payment', 'Waiting Payment'),
        ('paid', 'Paid'),
        ('completed', 'Completed'),
        ('close', 'Close')
    ])
    terms = models.ForeignKey('Terms', on_delete=models.CASCADE)
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)
    docs = models.ForeignKey('InvoiceDoc', on_delete=models.CASCADE, null=True, blank=True)

    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  
    total_net_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    turn_to_pdf = models.BooleanField(default=False)

    def __str__(self):
        return str(self.invoice_num)

    # @classmethod
    # def total_tax_amount(cls):
    #     return InvoiceItem.objects.aggregate(Sum('tax_amount'))['tax_amount__sum']
    
    # def total_net_amount(cls):
    #     return InvoiceItem.objects.aggregate(Sum('price'))['tax_amount__sum']
    
    
    def save(self, *args, **kwargs):

        self.invoice_num = f"INV-{self.invoice_num}" 

        # self.total_tax_amount = sum(item.tax_amount for item in self.items.invoiceItems.all())
        # self.total_net_amount = sum(item.total for item in self.items.invoiceItems.all())
        # self.total_amount = self.total_tax_amount + self.total_net_amount

        super().save(*args, **kwargs)

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')  # Extract items data
    #     invoice = Invoice.objects.create(**validated_data)  # Save the invoice first

    #     # Now add items to the invoice
    #     for item_data in items_data:
    #         item = InvoiceItem.objects.create(**item_data)  # Create each item
    #         invoice.items.add(item)  # Add item to the invoice's many-to-many field

    #     return invoice