# Generated by Django 4.0.4 on 2022-05-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_chekoutaddress_checkoutaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='apartment_address',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]