# Generated by Django 5.1.3 on 2024-11-20 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_rename_name_production_p_name_pdocument_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdocument',
            old_name='docfile',
            new_name='doc_file',
        ),
    ]