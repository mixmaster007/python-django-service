# Generated by Django 4.0.4 on 2022-07-04 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_gate_user_alter_batch_finish_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.FloatField(default=0.0, max_length=3),
        ),
        migrations.AlterField(
            model_name='batch',
            name='finish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 23, 27, 37, 258904)),
        ),
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 23, 27, 37, 258904)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 23, 27, 37, 257904)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Deposit_Received_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 23, 27, 37, 258904)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='User_Balance_updated_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 4, 23, 27, 37, 258904)),
        ),
    ]
