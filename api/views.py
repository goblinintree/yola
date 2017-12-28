# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def found_404(request):
    respone_text = "API模块正在开发中..."
    return HttpResponse(respone_text)