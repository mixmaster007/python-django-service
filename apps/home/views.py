# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime
from django.shortcuts import redirect
from posixpath import split
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from .models import News
from .models import Gate1Manage
from .models import Gate2Manage
from .models import Gate_Link
from .models import balance
from .models import Message
from .models import TempFormat
from .models import Gate
from .models import Batch
from django.core import serializers
import json
import pprint
def check_BatchID():
    return Batch.objects.all().count()
    """
    tmp_gl=Gate.objects.all()
    x=0
    for i in tmp_gl:
        if i.batch_id > x:
            x=i.batch_id 
    return x  
    """
def convert_format(data,n):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("Test(convert_format)-------input data----------")
    pp.pprint(data)
    if len(data) <5:  # Check to empty string
        return ""
    pb_format_array= data.split(n)
    pp.pprint("Test(convert_format)-------split data----------")
    pp.pprint(pb_format_array)
    if len(pb_format_array[1])>2:
        if len(pb_format_array[1])<5:
            tmp_str= [pb_format_array[1][:2],pb_format_array[1][2:4]]
            pb_format_array.pop(1)
            pb_format_array.insert(1,tmp_str[0])
            pb_format_array.insert(2,tmp_str[1])
        else:
            tmp_str= [pb_format_array[1][:2],pb_format_array[1][2:4],pb_format_array[1][4:6]]
            pb_format_array.pop(1)
            pb_format_array.insert(1,tmp_str[0])
            pb_format_array.insert(2,tmp_str[1])
            pb_format_array.insert(3,tmp_str[2])
    else:
        if len(pb_format_array[3])>2:
            tmp_str=[pb_format_array[2][:2],pb_format_array[2][2:4]]
            pb_format_array.pop(2)
            pb_format_array.insert(2,tmp_str[0])
            pb_format_array.insert(3,tmp_str[1])
            pb_format_array.insert(4,tmp_str[2])
        
   
   
    x = "#".join(pb_format_array)
    pp.pprint("Test(convert_format)-------out data----------")
    pp.pprint(x)
    return x
  
    
   
@login_required(login_url="/login/")
def index(request):
    num_news = News.objects.all().count()
    news = News.objects.all()
    GateLink = Gate_Link.objects.all() 
    pp = pprint.PrettyPrinter(indent = 4)
    if balance.objects.filter(user=request.user).exists(): 
        pp.pprint("Not Balance!!,so")
        user = balance.objects.get(user=request.user)
    else:
        new_balance = balance.objects.create(user=request.user,balance = 0)
        new_balance.save()
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
    tmp_gate = Gate.objects.filter()
    context={
        'pk' : pk,
        'about':about,
        "gateLink":GateLink,
        'balance':user.balance,
        
    }
    html_template = loader.get_template('home/gate_about.html')
    return HttpResponse(html_template.render(context, request))
pb_format_array=[""]
@login_required(login_url="/login/")
def gate_link(request,pk):
    pp = pprint.PrettyPrinter(indent = 4)
    GateLink = Gate_Link.objects.all()
    tmp_gate = Gate.objects.all()
    name = GateLink.get(id = pk).Link_Name
    cost =  GateLink.get(id = pk).Link_price
    logo = GateLink.get(id = pk).Link_Logo_large
    link_format_tmp  =  GateLink.get(id = pk).Link_Fomart.all()
    tmp_batch = Batch.objects.all()
    
    #for index in range(len(link_format_tmp)):
    #    link_format={"id":index,"key":link_format_tmp[index]}
    #    pp.pprint(index)
    
    user = balance.objects.get(user=request.user)
    context={
        'segment':"gate_link",
        'Name':name,
        'Cost':cost,
        "gateLink":GateLink,
        'Gate':tmp_gate,
        'Batch':tmp_batch,
        'Total_Batch':tmp_batch.count(),
        'logo':logo,
        'balance':user.balance,
        'link_format':link_format_tmp
    }
    if request.method == 'POST':
        try:
            if request.POST['radio']:
                selected_format = request.POST['radio']
                r = convert_format(selected_format,'#')
                if TempFormat.objects.filter(user=request.user).exists(): 
                    TempFormat.objects.filter(user=request.user).delete()
                new_TmpFormat = TempFormat.objects.create(user=request.user,tmpStr=r)
                new_TmpFormat.save()   
        except:
            pp.pprint("This is execpt:Post[radio]")
        try:
            if request.POST['gatelink_previewData']:
                data_arry_line = request.POST['gatelink_previewData'].split("\r\n")
                i=0
                xx=[]
                for ii in data_arry_line:
                    r=convert_format(ii,'#')
                    if r !="":
                        xx.append(r.split('#'))
                context['data_array']=xx    
                context['segment'] = "gate_link_info"
                context['format_array']=str(TempFormat.objects.get(user=request.user)).split('#')
        except:
            pp.pprint("This is execpt:Post[gatelink_inserdata]")
        try:
            if request.POST['real_data']:
                check = request.POST.getlist('check')
                tmp_arry = str(TempFormat.objects.get(user=request.user)).split('#')
                tmp_batch_id =tmp_batch.count()+1
                default_array={
                    'phone':'0',
                    'DD':'0',
                    'MM':'0',
                    'YY':'0',
                    'string1':'#',
                    'string2':'#',
                    'string3':'#',
                    'string4':'#',
                    'string5':'#',
                    'string6':'#',
                    'string7':'#',
                    'string8':'#',
                    'string9':'#',
                    'string10':'#',
                    'batch_id':'0'
                }
                pp.pprint(check)
                cnt1=0
                for i in check:
                    tmp_x=i.replace("[","")
                    tmp_x=tmp_x.replace("]","")
                    tmp_x=tmp_x.replace("'","")
                    tmp_y =tmp_x.split(',')
                    pp.pprint(tmp_y)
                    cnt1+=1
                    cnt = 0
                    for ii in tmp_y:
                        default_array[tmp_arry[cnt]]=ii.strip()
                        cnt += 1
                    new_gate=Gate.objects.create(
                        phone = default_array['phone'],
                        DD=default_array['DD'],
                        MM = default_array['MM'],
                        YY = default_array['YY'],
                        string1 = default_array['string1'],
                        string2 = default_array['string2'],
                        string3 = default_array['string3'],
                        string4 = default_array['string4'],
                        string5 = default_array['string5'],
                        string6 = default_array['string6'],
                        string7 = default_array['string7'],
                        string8 = default_array['string8'],
                        string9 = default_array['string9'],
                        string10 = default_array['string10'],
                        gate_link_name = name,
                        batch_id =tmp_batch_id,
                        inserted_text = tmp_x,
                    )
                    new_gate.save()
                   
                    if Gate.objects.filter(gate_link_name='#').exists(): 
                        Gate.objects.filter(gate_link_name='#').delete()
                pp.pprint("---------Create Batch Test------------")
                new_Batch =Batch.objects.create(
                        total = cnt1,
                        batch_id = tmp_batch_id,
                        link_name = name,
                )
                
                new_Batch.save()
                context['segment'] = "gate_link_result"
                context['Gate'] = Gate.objects.all()
                context['Batch']= Batch.objects.all()
                context['Total_Batch']=Batch.objects.all().count()
                pp.pprint("___END___")
        except:
            pp.pprint("This is execpt:Post[real_data]")
    
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
def send_message(request):
    pp = pprint.PrettyPrinter(indent = 4)
    message = request.POST['message']
    pp.pprint(message)
    new_message = Message.objects.create(value=message, user = request.user)
    new_message.save()
    return HttpResponse("Message sent successfull")
def get_message(request):
    pp = pprint.PrettyPrinter(indent = 4)
    messages = Message.objects.filter(user="killer")
    pp.pprint(messages)
    return JsonResponse({"messages":list(messages.values())})
def send_gatelink_insertdata(request):
   
    insertdata = request.POST['gatelink_insertdata']
 
    return HttpResponse("Message sent successfull")
def get_link_info(request):
    pp = pprint.PrettyPrinter(indent = 4)
    gate = Gate.objects.filter(batch_id =request.POST['message'])

    cnt_queue = 0
    cnt_process = 0
    cnt_fali =0
    cnt_success = 0
    
    for i in gate:
        if i.status == 0:
            cnt_queue +=1
        elif i.status == 1:
             cnt_process +=1
        elif i.status == 2:
            cnt_fali+=1
        elif i.status == 3:  
            cnt_success+=1
    obj_batch =Batch.objects.get(batch_id = request.POST['message'])        
    obj_batch.fail =cnt_fali
    obj_batch.succeed =cnt_success
    obj_batch.done = cnt_fali + cnt_success
    if cnt_queue == 0 and cnt_process == 0:
        if (obj_batch.status !="Finished"):
            obj_batch.finish_time = datetime.now().strftime('%H:%M:%S')
        obj_batch.status = "Finished"
        
    obj_batch.save()
    batch=Batch.objects.filter(batch_id = request.POST['message'])
    context = {
        "gate":list(gate.values()),
        "batch":list(batch.values()),
    }
   #pp.pprint(context)
    return JsonResponse(context)