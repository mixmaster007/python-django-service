# Generated by Django 4.0.4 on 2022-06-28 19:28

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(default='000', max_length=10)),
                ('State', models.CharField(default='#', max_length=10)),
                ('City', models.CharField(default='#', max_length=100)),
                ('Country', models.CharField(default='#', max_length=100)),
                ('Time_Zone', models.CharField(default='#', max_length=100)),
                ('URL', models.CharField(default='#', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.IntegerField(default=0)),
                ('status', models.CharField(default='Running', max_length=100)),
                ('total', models.IntegerField(default=0)),
                ('succeed', models.IntegerField(default=0)),
                ('done', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(blank=True, default='28.06.2022 12:28:31')),
                ('finish_time', models.DateTimeField(blank=True, default='28.06.2022 12:28:31')),
                ('fail', models.IntegerField(default=0)),
                ('remains', models.IntegerField(default=0)),
                ('link_name', models.CharField(default='#', max_length=100)),
                ('user', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Members_View_Format', models.CharField(max_length=100)),
                ('Admin_Setting', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=0, max_length=100)),
                ('DD', models.IntegerField(default=0)),
                ('MM', models.IntegerField(default=0)),
                ('YY', models.IntegerField(default=0)),
                ('string1', models.CharField(default='#', max_length=100)),
                ('string2', models.CharField(default='#', max_length=100)),
                ('string3', models.CharField(default='#', max_length=100)),
                ('string4', models.CharField(default='#', max_length=100)),
                ('string5', models.CharField(default='#', max_length=100)),
                ('string6', models.CharField(default='#', max_length=100)),
                ('string7', models.CharField(default='#', max_length=100)),
                ('string8', models.CharField(default='#', max_length=100)),
                ('string9', models.CharField(default='#', max_length=100)),
                ('string10', models.CharField(default='#', max_length=100)),
                ('result1', models.CharField(default='', max_length=100)),
                ('result2', models.CharField(default='', max_length=100)),
                ('result3', models.CharField(default='', max_length=100)),
                ('result4', models.CharField(default='', max_length=100)),
                ('result5', models.CharField(default='', max_length=100)),
                ('batch_id', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0, help_text='0:In_Queue,1:Processing,2:Fail,3:Success')),
                ('gate_link_name', models.CharField(default='#', help_text='Enter field gate_link_name', max_length=100)),
                ('inserted_text', models.CharField(default='#', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gate1Manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gate_status', models.CharField(choices=[('ol', 'online'), ('um', 'under maintenance')], default='ol', max_length=2)),
                ('uner_mantatince_messge', models.CharField(help_text='Enter field Udermanitain Message', max_length=100)),
                ('About_Gate', ckeditor.fields.RichTextField()),
                ('Gate_Logo_tiny', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gate2Manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gate_status', models.CharField(choices=[('ol', 'online'), ('um', 'under maintenance')], default='ol', max_length=2)),
                ('uner_mantatince_messge', models.CharField(help_text='Enter field Udermanitain Message', max_length=100)),
                ('About_Gate', ckeditor.fields.RichTextField()),
                ('Logo_tiny', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Api_key', models.CharField(max_length=100)),
                ('USDT_ADDRESS', models.TextField()),
                ('Enable_Payment_Option_Tickets', models.CharField(max_length=200)),
                ('Payment_Minium_orther_to_load_account', models.FloatField(default=0.0, help_text='USD')),
                ('Check_for_payment_status_every', models.FloatField(default=0.0, help_text='min')),
            ],
        ),
        migrations.CreateModel(
            name='site_manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Site_Status', models.CharField(choices=[('on', 'Online'), ('off', 'Uner Mantatince')], default='on', max_length=3)),
                ('Uner_Mantatince_Messge', models.CharField(default='', help_text='Enter field Udermanitain Message', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_ID', models.CharField(default='', max_length=100)),
                ('From_Ticket', models.CharField(default='', max_length=100)),
                ('USDT_Reciver_Address', models.CharField(default='', max_length=200)),
                ('Amount_Recived', models.FloatField(default=0)),
                ('Transaction_Status', models.CharField(default='', max_length=20)),
                ('Deposit_Received_At', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 12, 28, 31, 590341))),
                ('User_Balance_updated_At', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 12, 28, 31, 590341))),
                ('User_Name', models.CharField(default='', max_length=100)),
                ('User_Balance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TempFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmpStr', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From_User', models.CharField(default='admin', max_length=100)),
                ('value', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 28, 12, 28, 31, 589342))),
                ('To_User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gate_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link_Name', models.CharField(help_text='Enter Link Name', max_length=100)),
                ('assin_link_to_gateway', models.CharField(choices=[('G1', 'Gate1'), ('G2', 'Gate2')], default='G1', max_length=6)),
                ('Link_price', models.FloatField(null=True)),
                ('Link_Logo_tiny', models.ImageField(null=True, upload_to='images/')),
                ('Link_Logo_large', models.ImageField(null=True, upload_to='images/')),
                ('Link_Status', models.CharField(choices=[('At', 'Active'), ('Hd', 'Hidden')], default='At', max_length=2)),
                ('Link_Selected_Item', models.CharField(default='', max_length=100)),
                ('Link_Fomart', models.ManyToManyField(help_text='Select a Format for this Link', to='home.format')),
            ],
        ),
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
