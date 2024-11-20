# Generated by Django 5.1.3 on 2024-11-20 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseOrder', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='name',
            new_name='po_name',
        ),
        migrations.RenameField(
            model_name='purchaseorderitem',
            old_name='name',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='purchasedocument',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedocument',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='purchaseorderitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorderitem',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseorderitem',
            name='reception_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='purchaseorderitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
