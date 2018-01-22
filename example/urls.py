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
    url(r'^list$', views.example_list, name='example_list'),
    url(r'^list/xss01', views.example_xss01, name='example_xss01'),
    url(r'^list/xss02', views.example_xss02, name='example_xss02'),
    url(r'^list01', views.example_list, name='example_list'),

    url(r'^', views.example_found_404,name='example_found_404'),

]
