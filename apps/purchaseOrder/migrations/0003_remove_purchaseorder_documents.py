# Generated by Django 5.1.3 on 2024-11-11 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseOrder', '0002_purchaseorder_documents_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='documents',
        ),
    ]
