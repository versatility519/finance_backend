# Generated by Django 5.1.3 on 2024-11-13 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_rename_item_manufaccode_receptionitem_item_manufacturer_code'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(),
        ),
    ]
