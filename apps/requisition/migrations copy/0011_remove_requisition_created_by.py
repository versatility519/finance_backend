# Generated by Django 5.1.2 on 2024-10-31 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0010_requisitiondoc_docs_alter_requisitiondoc_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='created_by',
        ),
    ]