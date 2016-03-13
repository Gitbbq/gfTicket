#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"

# Stdlib imports


# Core Django imports
from django.apps import AppConfig


# Third-party app imports


# Imports from your apps


# Create your models here.


class SsoConfig(AppConfig):
    name = 'apps.SSO'
    label = 'sso'
    verbose_name = '统一登录模块'
