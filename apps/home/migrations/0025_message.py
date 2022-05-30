# Generated by Django 4.0.4 on 2022-05-29 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000000)),
            ],
        ),
    ]
