# Generated by Django 4.0.4 on 2022-05-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(null=True)),
                ('DD', models.IntegerField(null=True)),
                ('MM', models.IntegerField(null=True)),
                ('YY', models.IntegerField(null=True)),
                ('disits1', models.IntegerField(null=True)),
                ('disits2', models.IntegerField(null=True)),
                ('string1', models.CharField(help_text='Enter String', max_length=100)),
                ('string2', models.CharField(max_length=100)),
                ('string3', models.CharField(max_length=100)),
                ('string4', models.CharField(max_length=100)),
                ('string5', models.CharField(max_length=100)),
                ('string6', models.CharField(max_length=100)),
                ('string7', models.CharField(max_length=100)),
                ('string8', models.CharField(max_length=100)),
                ('string9', models.CharField(max_length=100)),
                ('string10', models.CharField(max_length=100)),
                ('result1', models.CharField(max_length=100)),
                ('result2', models.CharField(max_length=100)),
                ('result3', models.CharField(max_length=100)),
                ('result4', models.CharField(max_length=100)),
                ('batch_id', models.IntegerField(null=True)),
                ('gate_link_name', models.CharField(help_text='Enter field gate_link_name', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='format',
            old_name='result1',
            new_name='Admin_Setting',
        ),
        migrations.RenameField(
            model_name='format',
            old_name='result2',
            new_name='Members_View_Format',
        ),
        migrations.RemoveField(
            model_name='format',
            name='DD',
        ),
        migrations.RemoveField(
            model_name='format',
            name='MM',
        ),
        migrations.RemoveField(
            model_name='format',
            name='YY',
        ),
        migrations.RemoveField(
            model_name='format',
            name='batch_id',
        ),
        migrations.RemoveField(
            model_name='format',
            name='disits1',
        ),
        migrations.RemoveField(
            model_name='format',
            name='disits2',
        ),
        migrations.RemoveField(
            model_name='format',
            name='gate_link_name',
        ),
        migrations.RemoveField(
            model_name='format',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='format',
            name='result3',
        ),
        migrations.RemoveField(
            model_name='format',
            name='result4',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string1',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string10',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string2',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string3',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string4',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string5',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string6',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string7',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string8',
        ),
        migrations.RemoveField(
            model_name='format',
            name='string9',
        ),
    ]
