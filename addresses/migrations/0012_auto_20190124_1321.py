# Generated by Django 2.0.7 on 2019-01-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0011_auto_20190123_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]