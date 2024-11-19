# Generated by Django 5.1.3 on 2024-11-19 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_initial'),
        ('project', '0001_initial'),
        ('purchaseOrder', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='storekeeper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_as_storekeeper', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='issue',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.issueitem'),
        ),
        migrations.AddField(
            model_name='issueitem',
            name='measureUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.issueunit'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='issue_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.issueunit'),
        ),
        migrations.AddField(
            model_name='bin',
            name='bin_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.location'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='order_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.orderunit'),
        ),
        migrations.AddField(
            model_name='reception',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseOrder', to='purchaseOrder.purchaseorder'),
        ),
        migrations.AddField(
            model_name='reception',
            name='storekeeper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reception_as_storekeeper', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='reception',
            name='recep_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.receptiondoc'),
        ),
        migrations.AddField(
            model_name='receptionitem',
            name='item_bin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bin'),
        ),
        migrations.AddField(
            model_name='reception',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.receptionitem'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_as_reserved_by', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='storekeeper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_as_storekeeper', to='users.customuser'),
        ),
        migrations.AddField(
            model_name='reservationitem',
            name='measureUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.issueunit'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.reservationitem'),
        ),
        migrations.AddField(
            model_name='location',
            name='storeroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.storeroom'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.subcategory'),
        ),
        migrations.AddField(
            model_name='transfert',
            name='bin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bin'),
        ),
        migrations.AddField(
            model_name='transfert',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
        ),
        migrations.AddField(
            model_name='transfertitem',
            name='item_bin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bin'),
        ),
        migrations.AddField(
            model_name='transfert',
            name='trans_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.transfertitem'),
        ),
    ]
