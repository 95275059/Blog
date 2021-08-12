#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/8/11 22:30
@Author  : CXY
"""

from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)