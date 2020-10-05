#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/05/13 20:24
@Author  : 彭友
@Version  : 设计数据库中的Users表结构
@File    : models.py
@Software: PyCharm
@Contact : peeeyiii@163.com
"""

from django.db import models
class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=128, unique=True)
    Password = models.CharField(max_length=256)

    class Meta:
        db_table = 'Users'
        ordering = ['UserID']
