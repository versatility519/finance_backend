# Generated by Django 5.1.2 on 2024-10-31 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0012_requisition_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisition',
            old_name='total_amount_before_tax',
            new_name='total_net_amount',
        ),
        migrations.AlterField(
            model_name='requisition',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitionItems', to='requisition.requisitionitem'),
        ),
    ]
