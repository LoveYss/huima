#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django import forms


class UserSettingForm(forms.Form):
    nick_name = forms.CharField(required=True, max_length=30)
    sex = forms.CharField(required=True)
    email_name = forms.CharField(required=True)
    domain_name = forms.CharField(required=True)
    birthday = forms.DateTimeField(required=True)
    QQ = forms.CharField(required=True)
    description = forms.CharField(required=True, max_length=2048)
