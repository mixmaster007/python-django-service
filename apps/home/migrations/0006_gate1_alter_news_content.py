# Generated by Django 4.0.4 on 2022-05-27 18:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_book_alter_news_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gate1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(null=True)),
                ('u_ma_me', models.CharField(help_text='Enter field Udermanitain Message', max_length=100)),
                ('about', ckeditor.fields.RichTextField()),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
