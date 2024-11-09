from django.db import models

# Create your models here.

class SubThreeAccount(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('SubTwoAccount', related_name='threelayer_account', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name) 
    
class SubTwoAccount(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('SubOneAccount', related_name='twolayer_account', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class SubOneAccount(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('SubSAccount', related_name='onelayer_account', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class SubSAccount(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('LegerAccount', related_name='subs_accounts', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class LegerAccount(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]

    LegerName = models.CharField(max_length=100)
    # account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    type_status = models.CharField(max_length=10, choices=[('increase', 'Increase'), ('decrease', 'Decrease')])

    def __str__(self):
        return str(self.LegerName)
    