from django.db import models
# from apps.account1.models import LegerAcc

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=200)
    role = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)

class Invoice(models.Model):
    invoice_num = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    items = models.ForeignKey('InvoiceItem', on_delete=models.CASCADE)
    required_date = models.DateField(auto_now=True)
    
    status = models.CharField(max_length=20, choices=[('Need approval', 'Need approval'), ('Approve', 'Approve'), ('Waiting Payment', 'Waiting Payment'), ('Paid', 'Paid'), ('Close / Complete', 'Close / Complete')])
    ship_to = models.CharField(max_length=100, default='Default Value')
    bill_to = models.CharField(max_length=100, default='Default Value')
    docs = models.ForeignKey('Document', on_delete=models.CASCADE, null=True, blank=True)

    terms = models.ForeignKey('Terms', on_delete=models.CASCADE)
    tax = models.ForeignKey('TaxInfo',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_num)
    
class InvoiceItem(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=40)
    unit = models.CharField(max_length=10)
    quantity = models.FloatField()
    price = models.FloatField()
    total = models.CharField(max_length=100)
    # account = models.ForeignKey(LegerAcc, on_delete=models.CASCADE, default=1)
    
    tax_group = models.ForeignKey('TaxInfo', on_delete=models.CASCADE, null=True, blank=True)
    # tax_amount = models.FloatField()

    def __str__(self):
        return str(self.name)
    
class Document(models.Model):
    name = models.CharField(max_length=10)
    docs = models.CharField(max_length=10)
    # docs = models.FileField(upload_to='documents/')    
   
    def __str__(self):
        return str(self.name)

class TaxInfo(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return str(self.name)
    
class Terms(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.name)