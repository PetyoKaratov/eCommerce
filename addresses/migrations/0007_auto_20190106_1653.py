# Generated by Django 2.0.7 on 2019-01-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20190104_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=120),
        ),
    ]
