# Generated by Django 2.2.12 on 2020-04-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0012_auto_20200416_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
