# Generated by Django 2.2.12 on 2020-04-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0002_auto_20200415_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'sold_out'), (2, 'in_sell')], default=2),
        ),
    ]
