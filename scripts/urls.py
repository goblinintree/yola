"""yola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
import views

# views

urlpatterns = [
    url(r'^py/list', views.pylist, name='pylist'),
    url(r'^py/do', views.pydo, name='pydo'),

    url(r'^js/list', views.jsbox, name='jsbox'),
    url(r'^ajax/save/$', views.ajaxdosave, name='ajaxdosave'),
    url(r'^fsrc/csrf/', views.do_csrf, name='do_csrf'),

]
