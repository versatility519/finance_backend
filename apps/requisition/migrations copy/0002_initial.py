# Generated by Django 5.1.2 on 2024-10-30 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0005_alter_tax_tax_rate'),
        ('requisition', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitionitem',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='tax_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.tax'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisition.requisitionitem'),
        ),
    ]