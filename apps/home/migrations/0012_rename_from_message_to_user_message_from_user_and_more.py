# Generated by Django 4.0.4 on 2022-06-28 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_user_to_message_from_remove_message_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='From',
            new_name='To_User',
        ),
        migrations.AddField(
            model_name='message',
            name='From_User',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='batch',
            name='finish_time',
            field=models.DateTimeField(blank=True, default='28.06.2022 09:42:09'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(blank=True, default='28.06.2022 09:42:09'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 9, 42, 9, 654743)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Deposit_Received_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 9, 42, 9, 655742)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='User_Balance_updated_At',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 9, 42, 9, 655742)),
        ),
    ]