# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import News
from .models import Gate1Manage
from .models import Gate2Manage
from .models import Gate_Link
from .models import balance
import pprint
@login_required(login_url="/login/")
def index(request):
    num_news = News.objects.all().count()
    news = News.objects.all()
    GateLink = Gate_Link.objects.all()    
    user = balance.objects.get(user=request.user)
    
    context = {
        'num_news':num_news,
        'news':news,
        'gateLink':GateLink,
        'balance':user.balance
    }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
   
@login_required(login_url="/login/")
def depositFunds(request):
    GateLink = Gate_Link.objects.all()
    user = balance.objects.get(user=request.user)
    context={
        'segmment':'depositFunds',
        'gateLink':GateLink,
        'balance':user.balance,
    }
    html_template = loader.get_template('home/depositFunds.html')
    return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def gate_about(request,pk):
    user = balance.objects.get(user=request.user)
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(pk)
    if pk == 1 :
        about = Gate1Manage.objects.all()
    else:
        about =  Gate2Manage.objects.all()
    GateLink = Gate_Link.objects.all()    

    context={

        'segmment':'gate_about',
        'pk' : pk,
        'about':about,
        "gateLink":GateLink,
        'balance':user.balance,
        
    }
    html_template = loader.get_template('home/gate_about.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")
def gate_link(request,pk):
    GateLink = Gate_Link.objects.all()  
    user = balance.objects.get(user=request.user)
    context={
        'segmment':'gate_link',
        "gateLink":GateLink,
        'balance':user.balance,

    }
    html_template = loader.get_template('home/gate_link.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def area_code(request):
    user = balance.objects.get(user=request.user)
    GateLink = Gate_Link.objects.all()    
    context = {
       'gateLink':GateLink,
       'balance':user.balance,
    }
    html_template = loader.get_template('home/area_code.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def history(request):
    user = balance.objects.get(user=request.user)
    GateLink = Gate_Link.objects.all()    
    context = {
       'gateLink':GateLink,
       'balance':user.balance,
    }
    html_template = loader.get_template('home/history.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def onlineSupport(request):
    user = balance.objects.get(user=request.user)
    GateLink = Gate_Link.objects.all()    
    context = {
       'gateLink':GateLink,
       'balance':user.balance,
    }
    html_template = loader.get_template('home/onlineSupport.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
