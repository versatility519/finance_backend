# Generated by Django 5.1.3 on 2024-11-13 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_reception_purchase_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationitem',
            old_name='item_manufacCode',
            new_name='item_manufacturer_code',
        ),
    ]