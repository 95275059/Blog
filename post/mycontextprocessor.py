#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/8/12 15:21
@Author  : CXY
"""
from django.db.models import Count

from post.models import Post

# 全局上下文
def getRightInfo(request):

    # 获取分类信息
    right_cate_post = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 获取近期文章
    right_rec_post = Post.objects.all().order_by('-created')[:3]

    # 获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created, COUNT('*') FROM t_post GROUP BY DATE_FORMAT(created, '%Y-%m') ORDER BY created desc;")
    right_arch_post = cursor.fetchall()

    return {'right_cate_post': right_cate_post, 'right_rec_post': right_rec_post, 'right_arch_post': right_arch_post}
