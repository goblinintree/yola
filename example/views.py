# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def example_list(request):
    return render(request, 'list.html')

# u"测试 反射型 XSS"
def example_xss01(request):
    u_name = request.GET['name']

    return render(request, 'test_xss01.html',{'u_name': u_name})


# u"测试 存储型 XSS"
def example_xss02(request):
    u_fname = ""
    u_lname = ""
    try:
        if request.POST['fname']:
            u_fname = request.POST['fname']
            u_lname = request.POST['lname']
            print u_fname, u_lname
    except (UnboundLocalError,Exception):
        print "e.message"
    if u_fname and u_lname:
        u_name = {"u_fname": u_fname, "u_lname": u_lname}
    else:
        u_name = {"u_fname": u"u_fname 返回参数", "u_lname": u"u_lname 返回参数"}
    return render(request, 'test_xss02.html',{'u_name': u_name})

def example_found_404(request):
    respone_text = "前端正在开发中..."
    return HttpResponse(respone_text)


