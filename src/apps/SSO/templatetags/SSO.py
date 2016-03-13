#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"
# Stdlib imports

# Core Django imports
from django import template

# Third-party app imports

# Imports from your apps

register = template.Library()


def nickname(user):
    if isinstance(user, str):
        return user
    try:
        result = user.sso_user.displayName
        if result is None:
            result = user.username
    except:
        result = user.username
    return result


def short_name(user):
    if isinstance(user, str):
        return user
    try:
        result = user.sso_user.displayName
        result = result.split("/")[0]
        if result is None:
            result = user.get_full_name()
    except:
        result = user.get_full_name()
    return result


register.filter('nickname', nickname)
register.filter('short_name', short_name)
