# Generated by Django 5.1.3 on 2024-11-19 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='client_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='InvoiceNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=200)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='invoice.invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_user', to='users.customuser')),
            ],
        ),
    ]
