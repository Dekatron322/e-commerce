# Generated by Django 2.2.4 on 2020-07-27 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_pass_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='pass_code',
            new_name='password',
        ),
    ]
