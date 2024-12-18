# Generated by Django 5.1.3 on 2024-11-19 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('project', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='preferred_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_inventory_items', to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='suppliers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_inventory_items', to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
