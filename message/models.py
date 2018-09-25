# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default="", primary_key=True, verbose_name=u"主键")
    name = models.CharField(max_length=32, null=True, blank=True, default="", verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言信息')
    """
    Django中其他的字段类型：
    models.ForeignKey
    models.DateTimeField
    models.IntegerField
    models.IPAddressField
    models.FileField
    models.ImageField
    """

    class Meta:
        verbose_name = u'用户留言信息'
        verbose_name_plural = verbose_name

        # db_table = "user_message"
        # ordering = "-object_id"
        # ordering = "object_id"
