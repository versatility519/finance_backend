# Generated by Django 5.1.2 on 2024-10-31 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0004_rename_totals_requisitionitem_totals_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisitionitem',
            old_name='totals_amount',
            new_name='total_amount',
        ),
    ]