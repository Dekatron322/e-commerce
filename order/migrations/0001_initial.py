# Generated by Django 2.2.4 on 2020-07-19 12:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
