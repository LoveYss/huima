#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django import forms


class UserModifyForm(forms.Form):
    nick_name = forms.CharField(required=True, max_length=30)
    sex = forms.CharField(required=True)
    email_name = forms.CharField(required=True)
    domain_name = forms.CharField(required=True)
    birthday = forms.DateTimeField(required=True)
    qq_num = forms.CharField(required=True)
    description = forms.CharField(required=True, max_length=2048)
