# Generated by Django 5.1.3 on 2024-11-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_organization_created_at_organization_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]