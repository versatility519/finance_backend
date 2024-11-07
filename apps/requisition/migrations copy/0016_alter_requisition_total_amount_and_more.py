# Generated by Django 5.1.2 on 2024-10-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0015_remove_requisition_items_requisitionitem_requisition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='total_amount',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='total_net_amount',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='total_tax_amount',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='requisitionitem',
            name='tax_amount',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='requisitionitem',
            name='total_amount',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=10),
        ),
    ]