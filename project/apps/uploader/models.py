# coding: utf-8
from django.db import models

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

# ViewSets define the view behavior.
class PhotoViewSet(viewsets.ModelViewSet):
    model = Document