# Generated by Django 2.2.4 on 2020-08-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200726_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='productquantity',
            name='shipping_charge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]