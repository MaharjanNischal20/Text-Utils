# Generated by Django 4.0.4 on 2022-05-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders_payment_completed_orders_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='payment_completed',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='payment_method',
        ),
    ]
