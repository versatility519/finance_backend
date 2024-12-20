# Generated by Django 5.1.3 on 2024-11-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to='documents/productions')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('p_start_date', models.DateTimeField(auto_now_add=True)),
                ('p_end_date', models.DateTimeField(auto_now_add=True)),
                ('p_status', models.CharField(choices=[('create', 'Create'), ('waiting_approval', 'Waiting_approval'), ('approve', 'Approve'), ('started', 'Started'), ('ended', 'Ended')], max_length=32)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufacturer_code', models.CharField(max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('approved_quantity', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
