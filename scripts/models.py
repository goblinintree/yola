# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class jsscript(models.Model):
    #  rid, name, url, description, context, updatetime
    rid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    context = models.TextField()
    updatetime = models.DateTimeField(auto_now_add=True)
