# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.


def found_404(request):
    respone_text = "您好，你访问的页面未找到！！或许正在在发请耐心等待..."
    return HttpResponse(respone_text)