# Generated by Django 5.1.2 on 2024-10-30 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_issue_project_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='issued_by',
        ),
    ]