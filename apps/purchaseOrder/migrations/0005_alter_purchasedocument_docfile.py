# Generated by Django 5.1.3 on 2024-11-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseOrder', '0004_rename_name_purchasedocument_doc_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedocument',
            name='docfile',
            field=models.FileField(upload_to='documents/purchase_docs'),
        ),
    ]
