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
    all_messages = UserMessage.objects.filter(name='cuixiaozhao')  # Django的QuerySet类型；
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html', {'message': message})
