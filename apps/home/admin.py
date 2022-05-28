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

from .forms import Gate1Form
# Register your models here
#admin.site.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','content','publish_date')
#class Gate1Admin(admin.ModelAdmin):
  #  form = Gate1Form

admin.site.register(News, NewsAdmin)
admin.site.register(Gate1Manage)
admin.site.register(Gate2Manage)
admin.site.register(Format)
