# Generated by Django 5.1.3 on 2024-11-13 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_reception_purchase_order'),
        ('purchaseOrder', '0005_alter_purchasedocument_docfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='order_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.orderunit'),
            preserve_default=False,
        ),
    ]
