# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import News
from .models import Gate1Manage
from .models import Gate2Manage
from .models import Gate2Manage
from .models import Format
from .models import Gate_Link
from .models import balance
from .models import Message
from .models import Gate
from .models import Batch
from .models import TempFormat
from .models import AreaCode
from .models import Transaction
from .models import PaymentManage
# Register your models here
#admin.site.register(News)
admin.site.site_header = "DataFlair Django Tutorials"

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','content','publish_date')
class FomartAdmin(admin.ModelAdmin):
    list_display = ('id','Members_View_Format','Admin_Setting')
class GateLinkAdmin(admin.ModelAdmin):
    list_display = ('Link_Name','assin_link_to_gateway','Link_price','Link_Logo_tiny','Link_Logo_large','Link_Status')
    def Link_Logo_tiny_preview(self, obj):
        return obj.Link_Logo_tiny_preview

    Link_Logo_tiny_preview.short_description = 'Link_Logo_tiny_preview'
    Link_Logo_tiny_preview.allow_tags = True
class MessageAdmin(admin.ModelAdmin):
     list_display=('user','value','date')
class GateAdmin(admin.ModelAdmin):
    list_display=('phone','YY','MM','DD','batch_id','status','gate_link_name')   
class BatchAdmin(admin.ModelAdmin):
    list_display=('batch_id','status','total','start_time','finish_time','link_name')  
class AreacodehAdmin(admin.ModelAdmin):
    list_display=('area_code','State','City','Country','Time_Zone','URL') 
class AreacodehAdmin(admin.ModelAdmin):
    list_display=('area_code','State','City','Country','Time_Zone','URL') 
class TransactionAdmin(admin.ModelAdmin):
    list_display=('Transaction_ID','From_Ticket','USDT_Reciver_Address','Amount_Recived','Transaction_Status','Deposit_Received_At','User_Balance_updated_At','User_Name','User_Balance') 
class PaymentManageAdmin(admin.ModelAdmin):
    list_display=('Api_key','USDT_ADDRESS','Enable_Payment_Option_Tickets','Payment_Minium_orther_to_load_account','Check_for_payment_status_every') 
#class Gate1Admin(admin.ModelAdmin):
  #  form = Gate1Form
admin.site.register(News, NewsAdmin)
admin.site.register(Gate,GateAdmin)
admin.site.register(Gate1Manage)
admin.site.register(balance)
admin.site.register(Gate2Manage)
admin.site.register(Format,FomartAdmin)
admin.site.register(Gate_Link,GateLinkAdmin)
admin.site.register(Message,MessageAdmin)
#admin.site.register(TempFormat)
admin.site.register(Batch,BatchAdmin)
admin.site.register(AreaCode,AreacodehAdmin)
admin.site.register(PaymentManage,PaymentManageAdmin)
admin.site.register(Transaction,TransactionAdmin)



