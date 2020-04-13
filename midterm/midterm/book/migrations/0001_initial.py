# Generated by Django 2.2.10 on 2020-03-02 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('num_pages', models.IntegerField(default=0)),
                ('publisher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('type', models.CharField(choices=[('Bullet', 'Bullet'), ('Food', 'Food'), ('Travel', 'Travel'), ('Sport', 'Sport')], max_length=200)),
                ('publisher', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
