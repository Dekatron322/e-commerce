# Generated by Django 2.2.4 on 2020-07-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pass_code',
            field=models.CharField(default='none', max_length=150),
        ),
    ]