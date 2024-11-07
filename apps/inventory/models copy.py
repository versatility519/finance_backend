from django.db import models
from apps.users.models import CustomUser
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name

class Documents(models.Model):
    doc_number = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.doc_number

class Storeroom(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    storeroom = models.ForeignKey(Storeroom, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 


class Bin(models.Model):
    bin_name = models.CharField(max_length=100)
    bin_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # bin_code = models.CharField(max_length=100)
    # bin_description = models.TextField()
    # bin_capacity = models.FloatField()
    # bin_current_quantity = models.FloatField()
    # bin_status = models.CharField(max_length=100)

    def __str__(self):
        return self.bin_name

class ReceptionItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacCode = models.CharField(max_length=100)

    item_quantity = models.FloatField()
    item_bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
    
class Reception(models.Model):
    pur_order = models.PositiveIntegerField()
    items = models.ForeignKey('ReceptionItem',on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)
    storekeeper = models.ForeignKey(
        CustomUser, 
        related_name='reception_as_storekeeper', 
        on_delete=models.CASCADE
    )
    date_received = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    recep_doc = models.ForeignKey('Documents', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.notes
    
class ReservationItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacCode = models.CharField(max_length=100)
    item_quantity = models.FloatField()
    item_unit = models.CharField(max_length=100)
    def __str__(self):
        return self.item_name

class Reservation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    items = models.ForeignKey('ReservationItem',on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    reserved_by = models.ForeignKey(
        CustomUser, 
        related_name='reservation_as_reserved_by',
        on_delete=models.CASCADE
    )
    storekeeper = models.ForeignKey(
        CustomUser, 
        related_name='reservation_as_storekeeper',
        on_delete=models.CASCADE
    )
    
    recep_doc = models.ForeignKey('Documents', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('created', 'Approve'),
        ('approved', 'approved'),
        ('completed', 'completed'),
        ('cancel', 'cancel')
    ])
    date_received = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notes

class IssueItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacCode = models.CharField(max_length=100)
    item_quantity = models.FloatField()
    item_unit = models.CharField(max_length=100)
    def __str__(self):
        return self.item_name
    
class Issue(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    items = models.ForeignKey('IssueItem',on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    notes= models.TextField()
    issued_by = models.ForeignKey(
        CustomUser,
        related_name='issue_as_issued_by',
        on_delete=models.CASCADE
    )
    storekeeper = models.ForeignKey(
        CustomUser,
        related_name='issue_as_storekeeper',
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    