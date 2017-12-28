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
from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from django.contrib import admin

import views
import www.urls
import api.urls
import face.urls
import ymail.urls
import scripts.urls
import fsrc.urls

urlpatterns = [
    url(r'^$', views.home),
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/favicon.ico')),

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls)),
    url(r'^face/', include(face.urls)),
    url(r'^mail/', include(ymail.urls)),
    url(r'^script/', include(scripts.urls)),
    url(r'^fsrc/', include(fsrc.urls)),

    url(r'^', include(www.urls)),

]