# Generated by Django 5.1.2 on 2024-10-31 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0008_remove_requisition_created_by'),
        ('users', '0003_customuser_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_requisitions', to='users.customuser'),
            preserve_default=False,
        ),
    ]
