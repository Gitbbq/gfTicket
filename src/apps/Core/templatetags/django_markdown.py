#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"
# Stdlib imports
import markdown
# Core Django imports
from django import template

# Third-party app imports

# Imports from your apps

register = template.Library()


def markdown_content(content, extension="gfm"):
    if content is None:
        return ""
    return markdown.markdown(content, extensions=[extension])


register.filter('markdown', markdown_content)
