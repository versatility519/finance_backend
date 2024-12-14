# Generated by Django 5.1.3 on 2024-11-19 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('client', '0001_initial'),
        ('inventory', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now=True)),
                ('required_date', models.DateField()),
                ('ship_to', models.CharField(max_length=100)),
                ('bill_to', models.CharField(max_length=100)),
                ('total_tax_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total_net_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('turn_to_pdf', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('need approval', 'Need approval'), ('approved', 'Approved'), ('waiting payment', 'Waiting Payment'), ('paid', 'Paid'), ('completed', 'Completed'), ('close', 'Close')], max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.contact')),
                ('terms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.terms')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('doc_file', models.FileField(upload_to='documents/invoices')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceDocs', to='invoice.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('net_amount', models.DecimalField(decimal_places=3, editable=False, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=3, editable=False, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_items', to='account.ledgeraccount')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.invoice')),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_items', to='inventory.issueunit')),
                ('tax_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_items', to='organization.tax')),
            ],
        ),
    ]
