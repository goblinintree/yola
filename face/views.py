# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def found_404(request):
    respone_text = "前端正在开发中..."
    return HttpResponse(respone_text)

