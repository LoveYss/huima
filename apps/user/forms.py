#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django import forms


class UserSetting(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

