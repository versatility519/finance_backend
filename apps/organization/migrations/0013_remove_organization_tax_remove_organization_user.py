# Generated by Django 5.1.3 on 2024-11-13 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_alter_organization_tax_alter_organization_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
    ]