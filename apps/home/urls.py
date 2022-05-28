# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path ('index/' ,views.index,name='index'),
    path ('depositFunds' ,views.depositFunds,name='depositFunds'),
    #path ('gate_about/<int:pk>' ,views.gate_about,{id:pk},name='gate_about'),
    #path ('gate_link/<int:pk>' ,views.gate_link,{'id':pk},name='gate_link'),
    
    #re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
