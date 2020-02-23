# Generated by Django 3.0.3 on 2020-02-23 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'low'), (2, 'normal'), (3, 'high')], default=2)),
                ('completed', models.BooleanField(default=False)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.List')),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
    ]
