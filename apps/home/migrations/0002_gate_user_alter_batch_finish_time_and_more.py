# Generated by Django 4.0.4 on 2022-07-04 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gate',
            name='user',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='batch',
            name='finish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 15, 40, 6, 887369)),
        ),
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 15, 40, 6, 887369)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 15, 40, 6, 884371)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Deposit_Received_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 15, 40, 6, 886370)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='User_Balance_updated_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 15, 40, 6, 886370)),
        ),
    ]
