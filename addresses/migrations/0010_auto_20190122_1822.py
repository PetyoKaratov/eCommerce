# Generated by Django 2.0.7 on 2019-01-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0009_auto_20190122_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
