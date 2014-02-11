# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('project.apps.uploader.views',
    url(r'^list/$', 'list', name='list'),
)