# Generated by Django 5.1.2 on 2024-10-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('payabler', 'Payabler'), ('buyer', 'Buyer'), ('storekeeper', 'Storekeeper'), ('supplier', 'Supplier'), ('clients', 'Clients')], default='storekeeper', max_length=20),
        ),
    ]
