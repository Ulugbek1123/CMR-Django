# Generated by Django 3.1.2 on 2020-11-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeShop', '0002_auto_20201118_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
