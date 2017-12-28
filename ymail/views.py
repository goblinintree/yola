# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import json

from django.core.urlresolvers import reverse  
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from common.common import YolaMail

# Create your views here.



def send_mail(request):
    respone_text = "API模块- cookis_save 正在开发中..."
    if 'mail_to' in request.GET:#get传参，变量名为mail_to
        mail_to = request.GET['mail_to']
        subject = '来自yola的问候 send_mail'
        text_content = '这是一封重要的邮件 send_mail.'
        html_content = '<p>这是一封<strong>重要的</strong>邮件. send_mail</p>'
        yolaMail = YolaMail([mail_to,], subject, text_content, html_content)
        respone_text = yolaMail.post_mail()
        print "1### ", respone_text.decode("UTF-8")
    return HttpResponse(respone_text)

def mail_todo(request):
    message = "API模块- mail_todo 正在开发中..."
    error_code = 0
    # print ">>>>>>>>>>>>", request.POST
    if request.method == 'POST':
        mail_to_list = ["yulikui@made-in-china.com",]
        if 'mail_to' in request.POST: 
            mail_to_list = re.split(',','%s'% request.POST.get('mail_to'))
        mail_subject = '[默认主题]来自yola的问候mail_todo'
        if 'subject' in request.POST:
            mail_subject = request.POST.get('subject')

        mail_text_content = '[默认内容]你好，yola的朋友.mail_todo'
        if 'content' in request.POST: 
            mail_text_content = request.POST.get('content')
        mail_html_content = ""
        if 'html_content' in request.POST: 
            mail_html_content = request.POST.get('html_content')

        mail_validate = True
        for mail_to in mail_to_list:
            if mail_to:
                if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9|-]+\.+[a-zA-Z]", mail_to) == None:
                    mail_validate = False
                    message = "收件人邮件 ["+ mail_to +"] 不合法！！"
                    error_code = -1
            else:
                message = "收件人不能为空！！"
                error_code = -2
        #     return_context = "获取参数错误！！" + ae.message
        if mail_validate:
            try:
                from_email = settings.DEFAULT_FROM_EMAIL
                msg = EmailMultiAlternatives(mail_subject, mail_text_content, from_email, mail_to_list)
                if mail_html_content:
                    msg.attach_alternative(mail_html_content, "text/html")
                msg.send()
                message = "邮件发送成功！！"
            except Exception as e:
                message = "邮件发送失败！！<br>" + e.message 
                error_code = -3
                print ">>>    ", e.message
    else:
        message = "邮件API调用方式错误，非POST"
        error_code = -4
    data_result = {}
    data_result["error_code"] = error_code
    data_result["message"] = message

    result_data = json.dumps(data_result,ensure_ascii=False).encode('UTF-8')
    # print "DEBUG   ", str(result_data).decode("UTF-8")
    return HttpResponse(result_data, content_type="application/json")