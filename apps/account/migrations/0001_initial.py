# Generated by Django 5.1.2 on 2024-10-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegerAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=10)),
                ('type_status', models.CharField(choices=[('increase', 'increase'), ('decrease', 'decrease')], max_length=10)),
            ],
        ),
    ]