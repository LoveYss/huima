# Author:Loveyss
# -*-coding:utf-8 -*-
# @Time     :2019/5/31   14:50
# @Author   :Loveyss
# @Site     :
# @File     :forms.py
# @Software :PyCharm

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    Username = forms.EmailField(required=True)
    Password = forms.CharField(required=True)
    Nickname = forms.CharField(required=True)

    Sex = forms.CharField(required=True)
    Birthday = forms.DateField(required=True)
    Signature = forms.CharField(required=True)
