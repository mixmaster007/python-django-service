# Generated by Django 4.0.4 on 2022-05-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_gate_rename_result1_format_admin_setting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gate_link',
            name='Link_Fomart',
            field=models.ManyToManyField(help_text='Select a Format for this Link', to='home.format'),
        ),
    ]
