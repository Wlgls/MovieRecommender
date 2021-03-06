#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/05/13 20:24
@Author  : 彭友
@Version  : 设计了前端与用户交互的数据模型，用来收集用户输入
@File    : forms.py
@Software: PyCharm
@Contact : peeeyiii@163.com
"""

from django import forms
from captcha.fields import CaptchaField


class Userform(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label="验证码")

# 表单对象中的各个参数都对应着html中表单的某些元素和属性；且表单类成员变量的声明和Models中数据库列的声明很相似！


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')
