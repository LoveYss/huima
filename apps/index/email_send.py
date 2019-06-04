# Author:Loveyss
# -*-coding:utf-8 -*-
# @Time     :2019/6/3   14:39
# @Author   :Loveyss
# @Site     :
# @File     :email_send.py
# @Software :PyCharm
from random import Random
from django.core.mail import send_mail
from index.models import EmailVerifyRecord
from huima.settings import EMAIL_FROM


def random_str(randomlength=8):
    ran_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        ran_str += chars[random.randint(0, length)]
    return ran_str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "<h2>慧码时代</h2>|<h4>注册激活链接</h4>"
        email_body = "请在一个小时内点击下面的链接激活你的账号: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "<h2>慧码时代</h2>|<h4>密码重置链接</h4>"
        email_body = "请点击下面的链接重置密码: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "<h2>慧码时代</h2>|<h4>邮箱修改验证码</h4>"
        email_body = "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
