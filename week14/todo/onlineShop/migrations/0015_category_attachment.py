# Generated by Django 2.2.12 on 2020-04-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0014_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='attachment',
            field=models.FileField(null=True, upload_to='home/dana/Рабочий стол/BFDjango/week12/todo/onlineShop/files'),
        ),
    ]
