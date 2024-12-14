# Generated by Django 5.1.3 on 2024-11-20 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipdocs',
            old_name='name',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='supplieritem',
            old_name='name',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='carrier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shipdocs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipdocs',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipping',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shippingitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='suppliercontact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suppliercontact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='supplieritem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplieritem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='supplierpo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 20, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplierpo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='shipping_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
