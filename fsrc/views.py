# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import threading
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import  fsrc_tools
from ymail.common.common import YolaMail

# Create your views here.

# Create your views here.
def demo(request):
    respone_text = "API模块正在开发中..."
    return HttpResponse(respone_text)

def cookis_save(request):
    respone_text = "API模块- cookis_save 正在开发中..."
    my_cookies_dict = {}
    try:
        # print "1->  ", request.is_ajax()
        if request.method == 'POST':
            for key in request.POST:
                # print "2->  ", key
                my_cookies_dict[key] = request.POST.getlist(key)[0]
                # print "3->  ", request.POST.getlist(key)[0]
        if my_cookies_dict:
            string = json.dumps(my_cookies_dict)
        else:
            string =""
        t = threading.Thread(target=domail, args=(string, ""))
        t.start()
        if fsrc_tools.save_remote_cookies(string,settings.COOKIES_PATH,"cookies_json3.txt"):
            print "4->  ", u"成功"
        else:
            print "4->  ", u"失败"

    except UnboundLocalError as e:
        print ">>>    ", e.message
    return HttpResponse(str(string))

def cookis_save_json(request):
    respone_text = "API模块- cookis_save 正在开发中..."
    u_cookie = request.GET['u_cookie']
    u_appVersion = request.GET['u_appVersion']
    
    cookies_dict = {}
    cookies_dict['u_cookie'] = u_cookie 
    cookies_dict['u_appVersion'] = u_appVersion 
    string = json.dumps(cookies_dict)
    return HttpResponse(str(string))

def domail(text_content, html_content):
    print u"发送邮件"
    yolaMail = YolaMail(["yulikui@made-in-china.com",], "cookies do.js", text_content, html_content)
    respone_text = yolaMail.post_mail()
    return