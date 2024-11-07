from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tax(models.Model):
    tax_name = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=3)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    def __str__(self):
        return self.name