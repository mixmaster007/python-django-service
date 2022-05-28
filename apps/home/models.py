# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField 

class News(models.Model):
   
    title = models.CharField(max_length=200)
    content =  RichTextField()
    publish_date = models.DateField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])
class Gate1Manage(models.Model):
    STA = ''
    Gate_1_status =  models.BooleanField(null=True)
    uner_mantatince_messge = models.CharField(max_length = 100,help_text = "Enter field Udermanitain Message")
    About_Gate_1 = RichTextField()
    Gate_1_Logo_tiny = models.ImageField(max_length = 100)
    Format_Item = models.ForeignKey('Format', on_delete=models.SET_NULL, null=True)
    def __str__(self):
       return "Gate 1 Manage"
class Gate2Manage(models.Model):
     Gate_2_status =  models.BooleanField(null=True)
     uner_mantatince_messge = models.CharField(max_length = 100,help_text = "Enter field Udermanitain Message")
     About_Gate_2 = RichTextField()
     Gate_2_Logo_tiny = models.ImageField(max_length = 100)
     Format_Item = models.ForeignKey('Format', on_delete=models.SET_NULL, null=True)
     def __str__(self):
        return "Gate 2 Manage"
class Format(models.Model):
    phone =models.IntegerField(null=True)
    DD = models.IntegerField(null=True)
    MM = models.IntegerField(null=True)
    YY = models.IntegerField(null=True)
    disits1 = models.IntegerField(null=True)
    disits2 = models.IntegerField(null=True)
    string1 =  models.CharField(max_length =100 , help_text = "Enter String")
    string2 = models.CharField(max_length= 100 )
    string3 = models.CharField(max_length= 100)
    string4 = models.CharField(max_length= 100)
    string5 = models.CharField(max_length= 100)
    string6 = models.CharField(max_length= 100)
    string7 = models.CharField(max_length= 100)
    string8 = models.CharField(max_length= 100)
    string9 = models.CharField(max_length= 100)
    string10 = models.CharField(max_length= 100)
    result1 = models.CharField(max_length= 100)
    result2 = models.CharField(max_length= 100)
    result3 = models.CharField(max_length= 100)
    result4 = models.CharField(max_length= 100)
    batch_id = models.IntegerField(null=True)
    gate_link_name = models.CharField(max_length = 100,help_text = "Enter field gate_link_name")
    def __str__(self):
        return str(self.phone)
class Gate_Link(models.Model):
    GateOne = 'Go'
    GateTwo = 'Gt'
    StOne = "At"
    StTwo  = "Hd"
    Link_Name = models.CharField(max_length = 100,help_text = "Enter Link Name")
    assin_link_status = [
        (StOne, 'Active'),
        (StTwo, 'Hidden'),
    ]
    assin_link_to_gateway_choices = [
        (GateOne, 'Gate 1'),
        (GateTwo, 'Gate 2'),
    ]
    assin_link_to_gateway = models.CharField(
        max_length=2,
        choices=assin_link_to_gateway_choices,
        default=GateOne,
    )
    
    Link_price = models.IntegerField(null=True)
    Link_Logo_tiny=models.ImageField(max_length = 100,null = True)
    Link_Logo_large = models.ImageField(max_length = 100,null= True)
    Link_Status =  models.CharField(
        max_length=2,
        choices=assin_link_status,
        default=StOne,
    )


  
