#coding=utf-8

from django.urls import path, re_path
import post.views as views

urlpatterns=[
    re_path(r'^$', views.queryAll),
    re_path(r'^page/(?P<num>\d+)$', views.queryAll),
    re_path(r'^post/(?P<postid>\d+)$', views.postdetail),
    re_path(r'^category/(?P<cid>\d+)$', views.queryPostByCId),
    re_path(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.queryPostByCreated),
]