# Generated by Django 5.1.2 on 2024-10-30 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_issue_issued_by'),
        ('users', '0003_customuser_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransfertItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descripton', models.TextField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufactures_code', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('status', models.CharField(choices=[('approve', 'Approve'), ('partially_approve', 'Partially Approve'), ('declined', 'Declined')], max_length=20)),
                ('Bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bin')),
            ],
        ),
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('trans_number', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('approve', 'Approve'), ('transfered', 'Transfered')], max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
                ('trans_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.transfertitem')),
            ],
        ),
    ]