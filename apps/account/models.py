from django.db import models

# Create your models here.

class LegerAcc(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('debit', 'debit'), ('credit', 'credit')])
    type_status = models.CharField(max_length=10, choices=[('increase', 'increase'), ('decrease', 'decrease')])

    def __str__(self):
        return str(self.name)
    