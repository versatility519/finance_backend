# Generated by Django 5.1.3 on 2024-11-09 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_name_legeraccount_legername'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubOneAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onelayer_account', to='account.subsaccount')),
            ],
        ),
        migrations.CreateModel(
            name='SubTwoAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twolayer_account', to='account.suboneaccount')),
            ],
        ),
        migrations.CreateModel(
            name='SubThreeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threelayer_account', to='account.subtwoaccount')),
            ],
        ),
        migrations.DeleteModel(
            name='SubAccount',
        ),
    ]