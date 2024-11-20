# Generated by Django 5.1.3 on 2024-11-20 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisition',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='requisitiondoc',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitiondoc',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
