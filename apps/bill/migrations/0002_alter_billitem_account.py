# Generated by Django 5.1.3 on 2024-11-09 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_ledgeraccount_remove_subaccount_leger_account_and_more'),
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billitem',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ledgeraccount'),
        ),
    ]