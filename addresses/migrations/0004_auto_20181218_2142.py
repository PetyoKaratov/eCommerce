# Generated by Django 2.0.7 on 2018-12-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_auto_20181218_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
