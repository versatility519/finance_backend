# Generated by Django 5.1.3 on 2024-11-20 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseOrder', '0003_rename_name_purchaseorder_po_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedocument',
            old_name='docfile',
            new_name='docdoc_filefile',
        ),
    ]
