# Generated by Django 5.1.3 on 2024-11-07 01:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_legeracc_type_alter_legeracc_type_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_accounts', to='account.legeracc'),
        ),
    ]