# Generated by Django 5.1.3 on 2024-11-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingitem',
            name='quantity',
            field=models.PositiveIntegerField(help_text='Quantity of items'),
        ),
    ]
