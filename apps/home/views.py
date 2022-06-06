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
from .models import AreaCode
from django.core import serializers
import json
import re
import pprint
def mid(str,index,count):
    tmp_str=""
    for i in range(index,index+count):
        tmp_str+=str[i]
    return tmp_str

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
def check_format(format,data):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("__________Check_format_______________")
    context ={}
    
    if len(format) != len(data):
        context ={
            'data':data[:len(format)],
            'error_flag':'true',
            'error':{
                "style":"count error",
                'phone':data[0],
            }
        }
    else:
        tmp_check_dic ={} 
        tmp_error_str = ""
        for i in range(len(format)):
            tmp_check_dic[str(format[i])] = data[i]
        if  int(tmp_check_dic['DD']) == 0 or int(tmp_check_dic['DD']) > 31:
            tmp_error_str+= tmp_check_dic['DD'] + ":is not valid Day value\r\n"
        if int(tmp_check_dic['MM']) == 2 and  int(tmp_check_dic['DD'])>28:
            tmp_error_str+= tmp_check_dic['DD'] + ":is not valid Day value\r\n"
        if int(tmp_check_dic['MM']) ==0 or int(tmp_check_dic['MM']) >12:
            tmp_error_str+= tmp_check_dic['MM'] + ":is not valid Month value\r\n"
        context['data'] = data
        if tmp_error_str != "":
            context['error_flag'] ="true"
            context['error'] = {
                "style":tmp_error_str,
                'phone':data[0],
            }
        else:
            context['error_flag'] ="false"
    pp.pprint(context)
    return context
def convert_format(data):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("Test(convert_format)-------input data----------")
    pp.pprint(data)
    if len(data) <5:  # Check to empty string
        return ""
    
    pb_format_array = re.split('[^a-zA-Z0-9()+-]', data)
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
    news = News.objects.order_by('-publish_date').all()
        #Comment.objects.order_by('-datetime')
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
    pp.pprint("TEST____________Gate ABOUT________STRTE")
    pp.pprint(pk)
    if pk == 1 :
        about = Gate1Manage.objects.all()
    else:
        about =  Gate2Manage.objects.all()
    GateLink = Gate_Link.objects.all()   
    gate = Gate.objects.all()
    batch = Batch.objects.all()
    pp.pprint(GateLink)
    if pk == 1:
        ness_GateLink = Gate_Link.objects.filter(assin_link_to_gateway ='G1')
    else:
        ness_GateLink = Gate_Link.objects.filter(assin_link_to_gateway ='G2') 
    tmp_batch=[]
    tmp_total_count = 0
    for kkk1 in batch:
        for kkk in ness_GateLink:
            if kkk1.link_name == kkk.Link_Name:
                tmp_batch.append(kkk1)
                tmp_total_count+=1
    
    pp.pprint(tmp_total_count)
    context={
        'pk' : pk,
        'about':about,
        "nes_gateLink":ness_GateLink,
        'gateLink':GateLink,
        'batch':tmp_batch,
        'gate':gate,
        'total_batch':tmp_total_count,
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
        tmp_previewData =request.POST.get('gatelink_previewData')
        
        if tmp_previewData != None:
            check_flag =  request.POST.get('status_inserted_format')
            if check_flag != "ok":
                context['segment'] = "gate_link_error_nosel"
            else:
                pp.pprint("_________Arrive signal of gateLink_previewData_________")
                data_arry_line = tmp_previewData.split("\r\n")
                tmp_format_array= str(TempFormat.objects.get(user=request.user)).split('#')
                i=0
                tmp_data_array=[]
                tmp_error_arry = []
                for ii in data_arry_line:
                    r=convert_format(ii)
                    if r != "":
                        tmp_chek= check_format(tmp_format_array,r.split('#'))
                        tmp_data_array.append(tmp_chek['data'])
                        if(tmp_chek['error_flag'] == 'true'):
                            tmp_error_arry.append(tmp_chek['error'])
                if len(tmp_data_array) != 0:
                    if len(tmp_error_arry) == 0:
                        context['error_flag'] = 'no_error'
                    else:
                        context['error_flag'] = 'error'
                        context['error_arry'] = tmp_error_arry
                    context['segment'] = "gate_link_info"   
                    context['data_array']=tmp_data_array
                    context['format_array']=tmp_format_array
                pp.pprint(context)
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
    pp = pprint.PrettyPrinter(indent = 4)
    user = balance.objects.get(user=request.user)
    GateLink = Gate_Link.objects.all()    
    context = {
       'gateLink':GateLink,
       'balance':user.balance,
    }
    if request.method == 'POST': 
        try:
            if request.POST['area_inputData']:
                
                phonenumber_arry = request.POST['area_inputData'].strip().split("\r\n")
                pp.pprint(phonenumber_arry) 
                tmp_area_array =[]
                tmp_find_result=[]
                for pn in phonenumber_arry:
                    tmp_area=""
                    #pp.pprint(mid(pn,i,3).isnumeric)
                    for i in range(len(pn)):
                        tmp_area = mid(pn,i,3)
                        if tmp_area.isnumeric():
                            break
                    tmp_area_array.append(tmp_area)
                    if AreaCode.objects.filter(area_code = tmp_area).exists():
                        ttt= AreaCode.objects.get(area_code = tmp_area)
                        tmp_find_result.append([pn,ttt.area_code,ttt.State,ttt.City,ttt.Country,ttt.Time_Zone,ttt.URL])                                              
                    else:
                        tmp_find_result.append([pn,tmp_area,"NotFound","NotFound","NotFound","NotFound","NotFound"])                                                    
                context['segment']="in(p)_response"
                context['area_array']=tmp_area_array
                context['phonenumber_arry']=phonenumber_arry
                context['in_data']=request.POST['area_inputData'].strip()
                context['find_result']=tmp_find_result
                pp.pprint(tmp_area_array)
                pp.pprint(context['in_data'])
        except:
            pp.pprint("This is execpt:Post[area_inputData]")
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
        'user_name':request.user,
    }
    html_template = loader.get_template('home/onlineSupport.html')
    return HttpResponse(html_template.render(context, request))


def send_message(request):
    pp = pprint.PrettyPrinter(indent = 4)
    message = request.POST['message']
    user_name = request.POST['user']
    pp.pprint(message)
    new_message = Message.objects.create(value = message,user = user_name)
    new_message.save()
    return JsonResponse({"messages":"123"})
def get_message(request):
    pp = pprint.PrettyPrinter(indent = 4)
    messages = Message.objects.filter(user="killer")
    pp.pprint(messages)
    list(messages.values())
    return JsonResponse({"messages": list(messages.values())})
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
def get_area_all(request):
    """
     if AreaCode.objects.filter(area_code = tmp_area).exists():
        ttt= AreaCode.objects.get(area_code = tmp_area)
        tmp_find_result.append([pn,ttt.area_code,ttt.State,ttt.City,ttt.Country,ttt.Time_Zone,ttt.URL])                                              
        else:
        tmp_find_result.append([pn,tmp_area,"NotFound","NotFound","NotFound","NotFound","NotFound"])                                                    
    """
    if request.POST['message'] == 'ALL':
        context ={
            "item":"all"
        }
    elif request.POST['message'] == 'FND':
        context ={
            "item":"FND"
        }
    else:
        context = {
            "item":"NFD"
        }
    return JsonResponse(context)
def Gl_Send_InsertData(request):
    pp = pprint.PrettyPrinter(indent = 4)
           
    selected_format = request.POST.get("seleted_data")
    pp.pprint(selected_format)
    result = convert_format(selected_format)
    if TempFormat.objects.filter(user=request.user).exists(): 
       TempFormat.objects.filter(user=request.user).delete()
    new_TmpFormat = TempFormat.objects.create(user=request.user,tmpStr=result)
    new_TmpFormat.save()   
    return JsonResponse({'item':'ok'})
