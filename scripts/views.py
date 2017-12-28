# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json
import tools
# from tools import *

# Create your views here.
def pylist(request):
    respone_text = "API模块 已OK "

    scripts_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"scripts")
    file_type_list = [".py",]
    fileList = []
    fileList = tools.list_file(scripts_path,file_type_list)
    # fileList = json.dumps(fileList) 
    # print str(fileList).encode("UTF-8")
    fileList_box = {}
    fileList_box["fileList"] = fileList
    fileList_box["fileList_dict"] = json.dumps(fileList) 
    return render(request, 'py_scripts.html', {'fileList_box': fileList_box})


def pydo(request):
    respone_text = "API模块 已OK "
    print request.POST
    if 'py' in request.POST:
        py_script_name = request.POST['py']
        respone_text = py_script_name
        print respone_text
        result_dict = {}
        result_dict["code"] = 0
        result_dict["result"] = respone_text.encode("UTF-8")
    return JsonResponse(result_dict)


def do_csrf(request):
    return render(request, 'do_scrf.html') 

def jsbox(request):
    respone_text = "javascript box模块 已OK "
    jsscriptList =[]
    for index in range(10):
        jsscript = {}
        jsscript['rid'.encode("UTF-8")] = ("A1111111" + str(index) ).encode("UTF-8")
        jsscript['jname'.encode("UTF-8")] =  ("B1111111" + str(index) ).encode("UTF-8")
        jsscript['jurl'.encode("UTF-8")] =  ("C1111111" + str(index) ).encode("UTF-8")
        jsscript['jdis'.encode("UTF-8")] =  ("D1111111" + str(index) ).encode("UTF-8")
        jsscript['jcontext'.encode("UTF-8")] =  ("E1111111" + str(index) ).encode("UTF-8")
        jsscriptList.append(jsscript.copy())
    print jsscriptList
    return render(request, 'jsbox.html', {'jsscriptList': jsscriptList
    })


 
@csrf_exempt
def ajaxdosave(request):
    if request.is_ajax() and request.method == 'POST':
        jsscript_dict = {}
        for key in request.POST:
            jsscript_dict[key] = request.POST.getlist(key)[0]
    
    jsscript_dict['rid'] = 1
    jsscript_dict['jurl'] = 'http://sssssssssssss'

    json.dumps(jsscript_dict)
    return JsonResponse(jsscript_dict)

