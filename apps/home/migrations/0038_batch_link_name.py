# Generated by Django 4.0.4 on 2022-06-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_batch_finish_time_batch_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='link_name',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
