# Generated by Django 5.1.3 on 2024-11-11 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0012_alter_subaccount_options_and_more'),
        ('inventory', '0014_alter_inventoryitem_account'),
        ('organization', '0006_organization_created_at_organization_updated_at'),
        ('users', '0003_customuser_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('ship_to', models.CharField(max_length=100)),
                ('bill_to', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('created', 'Created'), ('approved', 'Approved'), ('partially_received', 'Partially_received'), ('completed', 'Completed'), ('sent', 'Sent'), ('canncelled', 'Canncelled')], max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('sent', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.department')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('doc', models.FileField(upload_to='document/purchase_docs')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseOrder.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufacturer_code', models.CharField(max_length=100)),
                ('supplier_code', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('created', 'Created'), ('approved', 'Approved'), ('partially_received', 'Partially received'), ('completed', 'Completed')], max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ledgeraccount')),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.orderunit')),
                ('purchaseOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseOrder.purchaseorder')),
                ('tax_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.tax')),
            ],
        ),
    ]
