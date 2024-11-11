from django.db import models

class LedgerAccount(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]

    ledger_name = models.CharField(max_length=100, choices=ACCOUNT_TYPES) 
    account_type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    status_change = models.CharField(max_length=10, choices=[('increase', 'Increase'), ('decrease', 'Decrease')])

    def __str__(self):
        return self.ledger_name  

# class SubAccount(models.Model):
#     name = models.CharField(max_length=100)
#     parent = models.ForeignKey(
#         'self', 
#         null=True, 
#         blank=True, 
#         related_name='children', 
#         on_delete=models.CASCADE
#     )
#     ledger_account = models.ForeignKey(
#         LedgerAccount, 
#         related_name='sub_accounts', 
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return self.name  

class SubAccount(models.Model):
    # Each SubAccount has a name and can be linked to a parent SubAccount to allow nested structures.
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',  # Allows referencing another SubAccount as parent
        null=True,
        blank=True,
        related_name='children',  # Related name for reverse lookup of children
        on_delete=models.CASCADE
    )
    ledger_account = models.ForeignKey(
        LedgerAccount,
        related_name='sub_accounts',  # Related name for reverse lookup of sub_accounts in LedgerAccount
        on_delete=models.CASCADE
    )

    def __str__(self):
        # Display the sub-account name and the level hierarchy
        return self.name

    class Meta:
        # Optional ordering to display sub-accounts in a structured way (e.g., alphabetically by name)
        ordering = ['name']