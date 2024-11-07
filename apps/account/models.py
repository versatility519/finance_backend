from django.db import models

# Create your models here.

class SubAccount(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('LegerAcc', related_name='sub_accounts', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class LegerAcc(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]

    name = models.CharField(max_length=100)
    # account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    type_status = models.CharField(max_length=10, choices=[('increase', 'Increase'), ('decrease', 'Decrease')])

    def __str__(self):
        return str(self.name)
    