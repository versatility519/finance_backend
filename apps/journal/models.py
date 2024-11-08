from django.db import models
from apps.account.models import LegerAccount

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    s_date = models.DateField(auto_now=True)
    e_date = models.DateField(auto_now=True)
    number = models.PositiveIntegerField()
    
    @property
    def totalCredit(self):
        return sum(transaction.amount for transaction in self.transactions.filter(type='credit'))
    @property
    def totalDebit(self):
        return sum(transaction.amount for transaction in self.transactions.filter(type='debit'))
    
    def __str__(self):
        return str(self.name)
    
    
class Transaction(models.Model):
    t_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField(max_length=200)
    type = models.CharField(max_length=7, choices=[('debit', 'debit'), ('credit', 'credit')])
    account = models.ForeignKey(LegerAccount,related_name='Leger Account+', on_delete=models.CASCADE)
    journalID = models.ForeignKey('Journal', related_name='transactions', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.name)
    

 