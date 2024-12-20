# Generated by Django 5.1.3 on 2024-11-19 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_initial'),
        ('purchaseOrder', '0002_initial'),
        ('supplier', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
        ),
        migrations.AddField(
            model_name='suppliercontact',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_contact', to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='supplieritem',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.orderunit'),
        ),
        migrations.AddField(
            model_name='supplieritem',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_items', to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='supplierpo',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseOrder.purchaseorder'),
        ),
        migrations.AddField(
            model_name='supplierpo',
            name='shipping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.shipping'),
        ),
    ]
