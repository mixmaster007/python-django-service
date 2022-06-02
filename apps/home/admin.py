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

class GateAdmin(admin.ModelAdmin):
    list_display=('phone','YY','MM','DD','batch_id','gate_link_name')   
class BatchAdmin(admin.ModelAdmin):
    list_display=('batch_id','status','total','start_time','finish_time','link_name')   
#class Gate1Admin(admin.ModelAdmin):
  #  form = Gate1Form

admin.site.register(News, NewsAdmin)
admin.site.register(Gate,GateAdmin)
admin.site.register(Gate1Manage)
admin.site.register(balance)
admin.site.register(Gate2Manage)
admin.site.register(Format,FomartAdmin)
admin.site.register(Gate_Link,GateLinkAdmin)
admin.site.register(Message)
admin.site.register(TempFormat)
admin.site.register(Batch,BatchAdmin)



