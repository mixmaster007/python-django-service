# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime
from multiprocessing.dummy import JoinableQueue
# from subprocess import CREATE_NEW_CONSOLE
from . import cnio_api
import logging
import threading
import time
import requests
from django.shortcuts import redirect
from posixpath import split
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
from .models import PaymentManage
from .models import Transaction
from django.core import serializers
from django.db.models import Q
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
def check_format(format,data,format_user):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("__________Check_format_______________")
    tmp_check_dic ={} 
    tmp_check_dic['error']=""
    pp.pprint(format)
    pp.pprint(data)
    pp.pprint(format_user)
    tmp_format ="#".join(format)
    pp.pprint(tmp_format)
    if len(format) != len(data):
        if len(format) >len(data):
            for i in range(len(format)):
                if i >= len(data):
                    tmp_check_dic[str(format[i])] = ""
                else:
                    tmp_check_dic[str(format[i])] = data[i]
                tmp_check_dic['error']="count error\r\n"
        else:
            for i in range(len(format)):
                tmp_check_dic[str(format[i])] = data[i]
            tmp_check_dic['error']="count error\r\n"
    else:
        pp.pprint("__________Check_format11_______________")
        for i in range(len(format)):
             tmp_check_dic[str(format[i])] = data[i]

    pp.pprint(tmp_check_dic)
    if tmp_check_dic.get("YYYY") != None :
        tmp_check_dic["YY"] = str(tmp_check_dic.get("YYYY"))[2:]
        tmp_format=tmp_format.replace("YYYY", "YY")
        tmp_check_dic.pop("YYYY")
    if tmp_check_dic.get("YYMMDD") != None :
        tmp_check_dic["YY"] = str(tmp_check_dic.get("YYMMDD"))[:2]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("YYMMDD"))[2:4]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("YYMMDD"))[4:6]
        tmp_format=tmp_format.replace("YYMMDD", "YY#MM#DD")
        tmp_check_dic.pop("YYMMDD")
    if tmp_check_dic.get("YYDDMM") != None :
        tmp_check_dic["YY"] = str(tmp_check_dic.get("YYDDMM"))[:2]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("YYDDMM"))[2:4]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("YYDDMM"))[4:6]
        tmp_format=tmp_format.replace("YYDDMM", "YY#DD#MM")
        tmp_check_dic.pop("YYDDMM")
    if tmp_check_dic.get("MMDDYY") != None :
        tmp_check_dic["MM"] = str(tmp_check_dic.get("MMDDYY"))[:2]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("MMDDYY"))[2:4]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("MMDDYY"))[4:6]
        tmp_format=tmp_format.replace("MMDDYY", "MM#DD#YY")
        tmp_check_dic.pop("MMDDYY")
    if tmp_check_dic.get("MMYYDD") != None :
        tmp_check_dic["MM"] = str(tmp_check_dic.get("MMYYDD"))[:2]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("MMYYDD"))[2:4]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("MMYYDD"))[4:6]
        tmp_format=tmp_format.replace("MMYYDD", "MM#YY#DD")
        tmp_check_dic.pop("MMYYDD")
    if tmp_check_dic.get("DDYYMM") != None :
        tmp_check_dic["DD"] = str(tmp_check_dic.get("DDYYMM"))[:2]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("DDYYMM"))[2:4]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("DDYYMM"))[4:6]
        tmp_format=tmp_format.replace("DDYYMM", "DD#YY#MM")
        tmp_check_dic.pop("DDYYMM")
    if tmp_check_dic.get("DDMMYY") != None :
        tmp_check_dic["DD"] = str(tmp_check_dic.get("DDMMYY"))[:2]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("DDMMYY"))[2:4]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("DDMMYY"))[4:6]
        tmp_format=tmp_format.replace("DDMMYY", "DD#MM#YY")
        tmp_check_dic.pop("DDMMYY")
    if tmp_check_dic.get("DDMM") != None :
        tmp_check_dic["DD"] = str(tmp_check_dic.get("DDMMYY"))[:2]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("DDMMYY"))[2:4]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("DDMMYY"))[4:6]
        tmp_format=tmp_format.replace("DDMM", "DD#MM")
        tmp_check_dic.pop("DDMMYY")
    if tmp_check_dic.get("DDYY") != None :
        tmp_check_dic["DD"] = str(tmp_check_dic.get("DDMYY"))[:2]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("DDMYY"))[2:4]
        tmp_format=tmp_format.replace("DDYY", "DD#YY")
        tmp_check_dic.pop("DDYY")
    if tmp_check_dic.get("MMYY") != None :
        tmp_check_dic["MM"] = str(tmp_check_dic.get("MMYY"))[:2]
        tmp_check_dic["YY"] = str(tmp_check_dic.get("MMYY"))[2:4]
        tmp_format=tmp_format.replace("MMYY", "MM#YY")
        tmp_check_dic.pop("MMYY")
    if tmp_check_dic.get("MMDD") != None :
        tmp_check_dic["MM"] = str(tmp_check_dic.get("MMDD"))[:2]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("MMDD"))[2:4]
        tmp_format=tmp_format.replace("MMDD", "MM#DD")
        tmp_check_dic.pop("MMDD")
    if tmp_check_dic.get("YYDD") != None :
        tmp_check_dic["YY"] = str(tmp_check_dic.get("YYDD"))[:2]
        tmp_check_dic["DD"] = str(tmp_check_dic.get("YYDD"))[2:4]
        tmp_format=tmp_format.replace("YYDD", "YY#DD")
        tmp_check_dic.pop("YYDD")
    if tmp_check_dic.get("YYMM") != None :
        tmp_check_dic["YY"] = str(tmp_check_dic.get("YYMM"))[:2]
        tmp_check_dic["MM"] = str(tmp_check_dic.get("YYMM"))[2:4]
        tmp_format=tmp_format.replace("YYMM", "YY#MM")
        tmp_check_dic.pop("YYMM")
  
    TempFormat.objects.filter(user=format_user).delete()
    new_TmpFormat = TempFormat.objects.create(user=format_user,tmpStr=tmp_format)
    new_TmpFormat.save()  
       
    
    if tmp_check_dic.get("DD") != None and tmp_check_dic.get("DD") != "":
        if tmp_check_dic['DD'].isdigit() == True:
            if  int(tmp_check_dic['DD']) == 0 or int(tmp_check_dic['DD']) > 31:
                tmp_check_dic['error']+= tmp_check_dic['DD'] + ":is not valid Day value\r\n"
            if tmp_check_dic.get('MM') != None:
                if tmp_check_dic['MM'].isdigit() == True:
                    if int(tmp_check_dic['MM']) == 2 and  int(tmp_check_dic['DD'])>28:
                        tmp_check_dic['error']+= tmp_check_dic['DD'] + ":is not valid Day value\r\n"
        else:
            tmp_check_dic['error']+=tmp_check_dic['DD'] + ":is not number\r\n"
    if tmp_check_dic.get("MM") != None and tmp_check_dic.get("MM") != "":
        if tmp_check_dic['MM'].isdigit() == True:
            if int(tmp_check_dic['MM']) ==0 or int(tmp_check_dic['MM']) >12:
                tmp_check_dic['error']+= tmp_check_dic['MM'] + ":is not valid Month value\r\n"
        else:
            tmp_check_dic['error']+=tmp_check_dic['MM'] + ":is not number\r\n"
    if tmp_check_dic.get("YY") != None and tmp_check_dic.get("YY") != "":
        if tmp_check_dic['YY'].isdigit() == False:
            tmp_check_dic['error']+=tmp_check_dic['YY'] + ":is not number\r\n"
        elif len(tmp_check_dic['YY'])>2:
            tmp_check_dic['error']+=tmp_check_dic['YY'] + ":is not valid Year value\r\n"
        
    pp.pprint("__________Check_format12_______________")
    pp.pprint(tmp_check_dic)
    return tmp_check_dic
def convert_format(data):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("Test(convert_format)-------input data----------")
    pp.pprint(data)
    #if len(data) <5:  # Check to empty string
    #    return ""
    
    pb_format_array = re.split('[^a-zA-Z0-9()+-]', data)
   
    pp.pprint("Test(convert_format)-------split data----------")
    pp.pprint(pb_format_array)
    
    x = ""
    cnt = 0
    for kk in pb_format_array:
        if kk != '':
            cnt+=1
            if cnt == 1:
                x=kk
            else :
                x+="#"+kk
    #x = "#".join(pb_format_array)
    pp.pprint("Test(convert_format)-------out data----------")
    pp.pprint(x)
       
    return x
  
    
   
@login_required(login_url="/login/")
def index(request):
    num_news = News.objects.all().count()
    news = News.objects.order_by('-publish_date').all()
    #admin_status 
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
    pp = pprint.PrettyPrinter(indent = 4)
    GateLink = Gate_Link.objects.all()
    cnio = cnio_api.cnio()
    pm = PaymentManage.objects.all()
    apiKey = ""
    m_strTicker=""
    for m_item in pm:
        m_strTicker = m_item.Enable_Payment_Option_Tickets
        apiKey = m_item.Api_key
        min_amount= m_item.Payment_Minium_orther_to_load_account
    m_arrayTicker = m_strTicker.split(';')
    pp.pprint(m_arrayTicker)
    cnio.api_key(apiKey)
    
    tmp_arrayTicker = []
    #for m_tItem in d:
    for tmp_inTicker in m_arrayTicker:
        pp.pprint(str(tmp_inTicker).lower())
        res=cnio.currenciesInfo(str(tmp_inTicker).lower())
        pp.pprint(res)
        new_res = res.decode('utf-8')
        d = json.loads(new_res)
        tmp_dicTiker ={
            'ticker':str(d['ticker']),
            'img':d['image'],
            'name':d['name'],
        }
        tmp_arrayTicker.append(tmp_dicTiker)

    pp.pprint(tmp_arrayTicker)
    user = balance.objects.get(user=request.user)
    context={
        'segmment':'depositFunds',
        'gateLink':GateLink,
        'balance':user.balance,
        'tickers':tmp_arrayTicker,
        'min_amount':min_amount
    }
    html_template = loader.get_template('home/depositFunds.html')
    return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def gate_about(request,item):
    user = balance.objects.get(user=request.user)
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("TEST____________Gate ABOUT________STRTE")
    
    if item == 'q' :
        m_pk = 1
        about = Gate1Manage.objects.all()
    elif item=='z':
        m_pk = 2
        about =  Gate2Manage.objects.all()
    GateLink = Gate_Link.objects.all()   
    gate = Gate.objects.all()
    batch = Batch.objects.all()
    pp.pprint(GateLink)
    if item == 'q':
        ness_GateLink = Gate_Link.objects.filter(assin_link_to_gateway ='G1')
    elif item=='z':
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
        'pk' : m_pk,
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
    seleted_item = GateLink.get(id = pk).Link_Selected_Item
    link_format_tmp  =  GateLink.get(id = pk).Link_Fomart.all()
    tmp_batch = Batch.objects.filter(user = str(request.user)).order_by('start_time').all()
   
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
        'link_format':link_format_tmp,
        'seleted_item':seleted_item

    }
    if request.method == 'POST':
        tmp_realData = request.POST.get('real_data')
        if tmp_realData != None:
            check = request.POST.getlist('check')
            pp.pprint("_______real_data__________")
            pp.pprint(tmp_realData)
            pp.pprint(check)
            tmp_arry = str(TempFormat.objects.get(user=request.user)).split('#')
            tmp_batch_id =tmp_batch.count()+1
            default_array={'phone':'0','DD':'0','MM':'0','YY':'0','string1':'#','string2':'#',
                'string3':'#','string4':'#','string5':'#','string6':'#','string7':'#','string8':'#',
                'string9':'#','string10':'#','batch_id':'0' }
            cnt1=0
            for i in check:
               # tmp_x=i.replace("[","")
               # tmp_x=tmp_x.replace("]","")
               # tmp_x=tmp_x.replace("'","")
                pp.pprint("_______real__REAL___data__________")
                pp.pprint(tmp_realData)
                temp_inserted_data_str = i.split("##")[0]
                temp_inserted_data_list = temp_inserted_data_str.split("*#*")
                temp_inserted_data_str =" ".join(temp_inserted_data_list)
                #____check inlcude space in inserted data format_____#
                      

                tmp_y = i.split("##")[1].split('#')
                pp.pprint(temp_inserted_data_str)
                pp.pprint(tmp_y)
                tmp_xx = 0
                for ii in tmp_y:
                    
                    if ii == "":
                        tmp_y.pop(tmp_xx)
                    tmp_xx +=1
                pp.pprint(tmp_y)
                if len(tmp_y) == len(tmp_arry):
                    pp.pprint("_____________________NO ERROR______________")
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
                        inserted_text = temp_inserted_data_str,
                     
                    )
                    new_gate.save()
                    
                    if Gate.objects.filter(gate_link_name='#').exists(): 
                        Gate.objects.filter(gate_link_name='#').delete()
            pp.pprint("---------Create Batch Test------------")
            if cnt1 != 0:
                if Batch.objects.filter(status = "Running").exists():
                    new_Batch =Batch.objects.create(
                            total = cnt1,
                            batch_id = tmp_batch_id,
                            link_name = name,
                            status = "Stopped",
                            user = str(request.user),
                    )
                else:
                    new_Batch =Batch.objects.create(
                            total = cnt1,
                            batch_id = tmp_batch_id,
                            link_name = name,
                            user = str(request.user),
                    )
                new_Batch.save()
                context['segment'] = "gate_link_result"
                context['Gate'] = Gate.objects.all()
                context['Batch']= Batch.objects.all()
                context['Total_Batch']=Batch.objects.all().count()
            else:
                context['segment'] = "gate_link_result_error"
            pp.pprint(context)
            pp.pprint("___END___")
      
    pp.pprint(context["seleted_item"]);
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
                tmp_find_result_exist=""
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
                        tmp_find_result_exist += pn+";"+ttt.area_code+";"+ttt.State + ";" + ttt.City +";"+ ttt.Country +";"+ttt.Time_Zone +";"+ ttt.URL +"\r\n"
                        tmp_find_result.append([pn,ttt.area_code,ttt.State,ttt.City,ttt.Country,ttt.Time_Zone,ttt.URL])                                              
                    else:
                        tmp_find_result.append([pn,tmp_area,"NotFound","NotFound","NotFound","NotFound","NotFound"])     
                                                               
                pp.pprint(tmp_find_result_exist)
                context['segment']="in(p)_response"
                context['area_array']=tmp_area_array
                context['phonenumber_arry']=phonenumber_arry
                context['in_data']=request.POST['area_inputData'].strip()
                context['find_result'] = tmp_find_result
                context['fnd_result'] =tmp_find_result_exist
                pp.pprint(tmp_area_array)
                pp.pprint(context['in_data'])
        except:
            pp.pprint("This is execpt:Post[area_inputData]")
    html_template = loader.get_template('home/area_code.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def history(request,m_str):
    pp = pprint.PrettyPrinter(indent = 4)
    user = balance.objects.get(user=request.user)
    GateLink = Gate_Link.objects.all()  
    tmp_array = {'Gate1','Gate2','Deposit'}  
    if(m_str == 'hgo'):
        tmp_item = 'Gate1'
    elif(m_str == 'hgt'):
        tmp_item = 'Gate2'
    elif(m_str == 'hd'):
        tmp_item = 'Deposit'
    pp.pprint(tmp_item)
    context = {
       'gateLink':GateLink,
       'balance':user.balance,
       'btn_array':tmp_array,
       'sel_item':tmp_item,
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
    messages = Message.objects.filter(Q(user="request.user") | Q(user_to = request.user))
    return JsonResponse({"messages": list(messages.values())})
def send_gatelink_insertdata(request):
   
    insertdata = request.POST['gatelink_insertdata']
 
    return HttpResponse("Message sent successfull")
def get_link_info(request):
    pp = pprint.PrettyPrinter(indent = 4)
   # datetime.now().strftime('%H:%M:%S')
    gateLink_name = request.POST.get('gateLink_name')
    context ={}
    m_btc  =  Batch.objects.filter(Q(link_name=str(gateLink_name)) and Q(user=str(request.user)) and Q(status="Running")).all()
    batch_array =[]
    gate_array = []
    tmp_status = ""
    for btc in m_btc:
        m_gate = Gate.objects.filter(Q(link_name=str(gateLink_name)) and Q(batch_id= btc.batch_id)).all()
        m_dicBtcItem = {
            'batch_id':btc.batch_id,
            'status':btc.status,
            'total':btc.total,
            'succeed':btc.succeed,
            'done':btc.done,
            'start_time':btc.start_time,
            'finish_time':btc.finish_time,
            'fail':btc.fail,
            'remains':btc.remains,
            'link_name':btc.link_name,
        }
        batch_array.append(m_dicBtcItem)
        for gat in m_gate:
            m_dicGateItem = {
                'inserted_text':gat.inserted_text,
                'result1':gat.result1,
                'result2':gat.result2,
                'result3':gat.result3,
                'result4':gat.result4,
                'result5':gat.result5,
                'status':gat.status,
                'batch_id':gat.batch_id
            }
            tmp_status +=str(gat.status)
            gate_array.append(m_dicGateItem)
    context = {
            "gate": gate_array,
            "batch":batch_array,
            "str_status":tmp_status
        }  
    """  
    if request.POST.get('message') != None:
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
       
        context['status'] = 'OK'
    else:
        context['status']='NO'
   #pp.pprint(context)
   """
    return JsonResponse(context,safe=False)
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
    return JsonResponse(context)
def Gl_Send_InsertData(request):
    pp = pprint.PrettyPrinter(indent = 4)
           
    selected_format = request.POST.get("seleted_data")
    link_name = request.POST.get("name")
    Gate_Link.objects.filter(Link_Name = link_name).update(Link_Selected_Item=selected_format)
    pp.pprint(selected_format)
    result = convert_format(selected_format)
    if TempFormat.objects.filter(user=request.user).exists(): 
       TempFormat.objects.filter(user=request.user).delete()
    new_TmpFormat = TempFormat.objects.create(user=request.user,tmpStr=result)
    new_TmpFormat.save()   
    return JsonResponse({'item':'ok'})
def GateLink_Send_Preview_Data(request):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("___________GateLink_Send_Preview_Data_____________")
    tmp_previewData =request.POST.get("gatelink_previewData_oo")
    tmp_seleted_data=request.POST.get("seleted_data")
    link_name = request.POST.get("page_name")
    Gate_Link.objects.filter(Link_Name = link_name).update(Link_Selected_Item=tmp_seleted_data)
    result = convert_format(tmp_seleted_data)
    if TempFormat.objects.filter(user=request.user).exists(): 
       TempFormat.objects.filter(user=request.user).delete()
    new_TmpFormat = TempFormat.objects.create(user=request.user,tmpStr=result)
    new_TmpFormat.save()   
    pp.pprint(tmp_previewData)
    if tmp_previewData != None:
        data_arry_line = tmp_previewData.split("\n")
        pp.pprint(data_arry_line)
        tmp_format_array= str(TempFormat.objects.get(user=request.user)).split('#')
        tmp_format_user = request.user
        i=0
        tmp_data_array=[]
        for ii in data_arry_line:
            pp.pprint("_______data_array_line_____")
            pp.pprint(ii)
            r=convert_format(ii)
            i += 1
            if r != "":
                tmp_check= check_format(tmp_format_array,r.split('#'),tmp_format_user)
                tmp_data_array.append(tmp_check)
        tmp_format_array= str(TempFormat.objects.get(user=request.user)).split('#')
        pp.pprint(tmp_format_array)
        
        jsonStr = json.dumps(list(tmp_data_array))
    return JsonResponse({'data_array':tmp_data_array,'format_array':tmp_format_array},safe=False)
def df_selected_ticker(request):
    cnio = cnio_api.cnio()
    pm = PaymentManage.objects.all()
    apiKey = ""
    m_amount = request.POST['amount']
    m_ticker = request.POST['ticker']
    for PayMan in pm:
        apiKey = PayMan.Api_key
    
    cnio.api_key(apiKey)
    res=cnio.est_exchange_rate(str(m_amount),"usdttrc20",m_ticker)
    new_res = res.decode('utf-8')
    d = json.loads(new_res)

    pp = pprint.PrettyPrinter(indent = 4)
 
    return JsonResponse(d)
def df_get_history(request):
    pp = pprint.PrettyPrinter(indent = 4)
    m_trans_array = Transaction.objects.filter(User_Name = str(request.user))
    m_tArray=[]
    for mta in m_trans_array:
        tmp_trans_array = {
            'Transaction_ID':mta.Transaction_ID,
            'From_Ticket':mta.From_Ticket,
            'USDT_Reciver_Address':mta.USDT_Reciver_Address,
            'Amount_Recived':mta.Amount_Recived,
            'Transaction_Status':mta.Transaction_Status,
            'Deposit_Received_At':mta.Deposit_Received_At,
            'User_Balance_updated_At':mta.User_Balance_updated_At,
            'User_Name':mta.User_Name,
            'User_Balance':mta.User_Balance
        }
        m_tArray.append(tmp_trans_array)

    pp.pprint(m_tArray)
    context={
        'trans_array':m_tArray
    }
    return JsonResponse(context,safe = False)

def df_deposit_click(request):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint("-----------------start Deposit Click-------------")
    cnio = cnio_api.cnio()
    pm = PaymentManage.objects.all()
    m_address=""
    apiKey = ""
    m_time = 0.0
    for PayMan in pm:
        apiKey = PayMan.Api_key
        m_address =  PayMan.USDT_ADDRESS
        m_time = PayMan.Check_for_payment_status_every * 60
    m_address_array = m_address.split("\r\n")
    m_amount = request.POST['amount']
    m_ticker = request.POST['ticker']
    tmp_trans = Transaction.objects.filter(From_Ticket=m_ticker).all()
    cnt=0
    for k in tmp_trans:
        if k.Transaction_Status != "finished":
            cnt+=1
    if cnt == 0:
        cnio.api_key(apiKey)
        result = cnio.create_transaction(m_amount,m_ticker,"trx",m_address_array[0])
        new_res = result.decode('utf-8')
        d = json.loads(new_res)
        pp.pprint(d)
        if d.get('error') != None:
            pp.pprint("occur error!!")
        else:
            info = {"stop": False}
            user_balance=balance.objects.get(user=request.user).balance

            thread = threading.Thread(target=deposit_status, args=(info,apiKey,d['id'],request.user,m_time,user_balance))
            
            thread.start()
    else:
        d = {
            'error':'Status Error',
            'message':'Runnig exchange of the crypto'
        }
    return JsonResponse(d)

def gl_copy_result(request):
    pp = pprint.PrettyPrinter(indent = 4)
    m_batchID = request.POST.get('batchID')
    m_btType = request.POST.get('btType')
    m_checkArray = str(request.POST.get('seleted_data')).split("#")
    m_resultStr = ""
    m_gate = []
    pp.pprint(m_btType)
    if m_btType == '0' :
        m_gate = Gate.objects.filter(batch_id = m_batchID)
    elif m_btType == '1' or m_btType == '2':
        m_gate = Gate.objects.filter(Q(batch_id = m_batchID) and Q(status = 3))
    elif m_btType == '3':
        m_gate = Gate.objects.filter(Q(batch_id = m_batchID) and Q(status = 2))
    for k in m_gate:
        for kk in m_checkArray:
            if kk =="DI":
                m_resultStr+=k.inserted_text+";"
            elif kk == "SF1":
                m_resultStr+=k.result1+";"
            elif kk == "SF2":
                m_resultStr+=k.result2+";"
            elif kk == "SF3":
                m_resultStr+=k.result3+";"
            elif kk == "SF4":
                m_resultStr+=k.result2+";"
            elif kk == "SF5":
                m_resultStr+=k.result2+";"
            elif kk == "ST":
                if k.status == 0:
                    m_resultStr+="In Queue"+";"
                elif k.status == 1:
                    m_resultStr+="Processing"+";"
                elif k.status == 2:
                    m_resultStr+="Fail"+";"
                elif k.status == 3:
                    m_resultStr+="Success"+";"
        m_resultStr+="\r\n"
    pp.pprint(m_checkArray)
     
    return JsonResponse({'result':m_resultStr})
def history_get_info(request):
    pp = pprint.PrettyPrinter(indent = 4)
    m_type = request.POST.get('type')
    if m_type == 'Gate1':
        tmp_str = 'G1'
    elif m_type == 'Gate2':
        tmp_str = 'G2'
    if m_type == 'Deposit':
        m_trans_array = Transaction.objects.filter(User_Name = str(request.user))
        m_tArray=[]
        for mta in m_trans_array:
            tmp_trans_array = {
                'Transaction_ID':mid(str(mta.Transaction_ID),0,8),
                'From_Ticket':mta.From_Ticket,
                'USDT_Reciver_Address':mta.USDT_Reciver_Address,
                'Amount_Recived':mta.Amount_Recived,
                'Transaction_Status':mta.Transaction_Status,
                'Deposit_Received_At':mta.Deposit_Received_At,
                'User_Balance_updated_At':mta.User_Balance_updated_At,
                'User_Name':mta.User_Name,
                'User_Balance':mta.User_Balance
            }
            m_tArray.append(tmp_trans_array)

        pp.pprint(m_tArray)
        context={
            'trans_array':m_tArray
        }
    else:
        m_gateLink = Gate_Link.objects.filter(assin_link_to_gateway = tmp_str)
        pp.pprint(m_gateLink)
        batch_array=[]
        gate_array = []
        for mgAr in m_gateLink:
            m_btc  =  Batch.objects.filter(link_name =  mgAr.Link_Name)
            m_gate = Gate.objects.filter(gate_link_name = mgAr.Link_Name)
            for btc in m_btc:
                m_dicBtcItem = {
                    'batch_id':btc.batch_id,
                    'status':btc.status,
                    'total':btc.total,
                    'succeed':btc.succeed,
                    'done':btc.done,
                    'start_time':btc.start_time,
                    'finish_time':btc.finish_time,
                    'fail':btc.fail,
                    'remains':btc.remains,
                    'link_name':btc.link_name,
                }
                batch_array.append(m_dicBtcItem)
            for gat in m_gate:
                m_dicGateItem = {
                    'di':gat.inserted_text,
                    'sf1':gat.result1,
                    'sf2':gat.result2,
                    'sf3':gat.result3,
                    'sf4':gat.result4,
                    'sf5':gat.result5,
                    'st':gat.status,
                    'bi':gat.batch_id
                }
                gate_array.append(m_dicGateItem)
        context={
            'batch_array':batch_array,
            'gate_array':gate_array
        }
        #pp.pprint(batch_array)
        
    return JsonResponse(context,safe = False)
def deposit_status(arg,apiKey,t_id,user,m_time,user_balance):
    pp = pprint.PrettyPrinter(indent = 4)
   
    trans_obj = Transaction.objects.create(User_Name=str(user),Transaction_ID=t_id,User_Balance=user_balance)
    trans_obj.save()
    cnio = cnio_api.cnio()
    cnio.api_key(apiKey)
    while not arg["stop"]:
        pp.pprint("worker thread checking status")
        try:
            result = cnio.get_transaction_status(t_id)
            new_res = result.decode('utf-8')
            json_res = json.loads(new_res)
            Transaction.objects.filter(Q(User_Name=str(user)) and Q(Transaction_ID=t_id)).update(Amount_Recived=json_res['expectedReceiveAmount'],Deposit_Received_At=json_res['createdAt'],User_Balance_updated_At=json_res['updatedAt'])
            Transaction.objects.filter(Q(User_Name=str(user)) and Q(Transaction_ID=t_id)).update(From_Ticket=json_res['fromCurrency'],USDT_Reciver_Address=json_res["payinAddress"],Transaction_Status=json_res["status"])
            if(json_res['status'] == "finished"):
                tmp_bb = balance.objects.filter(user=user)
                for kk in tmp_bb:
                   m_balance = float(kk.balance) + float(json_res['expectedReceiveAmount'])
                balance.objects.filter(user=user).update(balance = m_balance)
                Transaction.objects.filter(Q(User_Name=str(user)) and Q(Transaction_ID=mid(t_id,0,8))).update(User_Balance=m_balance)
                return 'end'
        except requests.exceptions.ConnectTimeout:
            pp.pprint("Error ConnectTimeout")
        pp.pprint(json_res)
        time.sleep(m_time)
def gateLink_get_batch_data(request):
    pp = pprint.PrettyPrinter(indent = 4)
    batch_array=[]
    gate_array = []
    m_type = request.POST.get('type')
    pp.pprint(m_type)
    gateLink_name =request.POST.get('name')
    m_batch_id = request.POST.get('batch_id')
    if m_type == '0':
     
        pp.pprint(gateLink_name)
                   
    elif m_type == '1':
       
        Batch.objects.filter(batch_id = int(m_batch_id)).update(status = "Stopped")
        tmp_gate = Gate.objects.filter(batch_id= int(m_batch_id)).all()
        for mm in tmp_gate:
            mm.status =2
    elif m_type == '2':
        Batch.objects.filter(batch_id = int(m_batch_id)).update(status = "Running")
        tmp_gate = Gate.objects.filter(batch_id= int(m_batch_id)).all()
        for mm in tmp_gate:
            mm.status = 0
    elif m_type == '3':
        Batch.objects.filter(batch_id = int(m_batch_id)).update(status = "Running")
        tmp_gate = Gate.objects.filter(batch_id= int(m_batch_id)).all()
        for mm in tmp_gate:
            mm.status = 0
    m_btc  =  Batch.objects.filter(Q(link_name=str(gateLink_name)) and Q(user=str(request.user))).all()
    m_runBath_array = ""
    for btc in m_btc:
        m_gate = Gate.objects.filter(Q(link_name=str(gateLink_name)) and Q(batch_id= btc.batch_id)).all()
        m_dicBtcItem = {
            'batch_id':btc.batch_id,
            'status':btc.status,
            'total':btc.total,
            'succeed':btc.succeed,
            'done':btc.done,
            'start_time':btc.start_time,
            'finish_time':btc.finish_time,
            'fail':btc.fail,
            'remains':btc.remains,
            'link_name':btc.link_name,
        }
        batch_array.append(m_dicBtcItem)
        for gat in m_gate:
            m_dicGateItem = {
                'inserted_text':gat.inserted_text,
                'result1':gat.result1,
                'result2':gat.result2,
                'result3':gat.result3,
                'result4':gat.result4,
                'result5':gat.result5,
                'status':gat.status,
                'batch_id':gat.batch_id
            }
            gate_array.append(m_dicGateItem)
    #m_gate = Gate.objects.filter(gate_link_name = mgAr.Link_Name)
    #m_gateLink = Gate_Link.objects.filter(assin_link_to_gateway = tmp_str)
    #pp.pprint(m_gateLink)
    """
    for mgAr in m_gateLink:
        m_btc  =  Batch.objects.filter(link_name =  mgAr.Link_Name)
        m_gate = Gate.objects.filter(gate_link_name = mgAr.Link_Name)
        for btc in m_btc:
            m_dicBtcItem = {
                'batch_id':btc.batch_id,
                'status':btc.status,
                'total':btc.total,
                'succeed':btc.succeed,
                'done':btc.done,
                'start_time':btc.start_time,
                'finish_time':btc.finish_time,
                'fail':btc.fail,
                'remains':btc.remains,
                'link_name':btc.link_name,
            }
            batch_array.append(m_dicBtcItem)
        for gat in m_gate:
            m_dicGateItem = {
                'di':gat.inserted_text,
                'sf1':gat.result1,
                'sf2':gat.result2,
                'sf3':gat.result3,
                'sf4':gat.result4,
                'sf5':gat.result5,
                'st':gat.status,
                'bi':gat.batch_id
            }
            gate_array.append(m_dicGateItem)
    """
    context={
        'batch_array':batch_array,
        'gate_array':gate_array,
        'runnig_array':m_runBath_array
    }
    pp.pprint(m_runBath_array)
    
    return JsonResponse(context,safe = False)
#class Transaction(models.Model):
 #   Deposit_Received_At = models.DateTimeField(blank=True)
  #  User_Balance_updated_At = models.DateTimeField(blank=True)
