# Generated by Django 5.1.3 on 2024-11-19 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_initial'),
        ('organization', '0001_initial'),
        ('requisition', '0001_initial'),
        ('supplier', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='approved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approved_requisitions', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_requisitions', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.department'),
        ),
        migrations.AddField(
            model_name='requisitiondoc',
            name='requisition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisition_docs', to='requisition.requisition'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='docs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitiondocs', to='requisition.requisitiondoc'),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='measureUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.orderunit'),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='requisition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='requisition.requisition'),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='tax_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requisition_items', to='organization.tax'),
        ),
    ]
