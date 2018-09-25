# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoStart.settings")  # project_name 项目名称
django.setup()

from django.shortcuts import render, redirect
from django.http import HttpResponse
from message.models import UserMessage


# Create your views here.
def getform(request):
    all_messages = UserMessage.objects.filter(name='cuixiaozhao', address='北京')  # Django的QuerySet类型；
    for message in all_messages:
        message.delete()
        #print message.name

    # # 数据的创建：
    # if request.method == "POST":
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'HelloDjango1'
    #     user_message.save()


    # Debug模式；
    # user_message = UserMessage()
    # user_message.name = 'cuixiaosi'
    # user_message.message = 'HelloDjango'
    # user_message.address = '上海'
    # user_message.email = 'tqtl911@163.com'
    # user_message.object_id = 'HelloDjango'
    # user_message.save()

    return render(request, 'message_form.html', )
