#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+code@gmail.com"
#
# Copyright 2015-2016 liantian
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
# Stdlib imports

# Core Django imports
from django.conf.urls import include, url
from django.contrib.auth.views import logout
# Third-party app imports

# Imports from your apps

from .views import Login, VerifiedPassword, LocalLogin
from .api.controller import GetTadinPassword

app_name = 'SSO'
urlpatterns = [
    url(regex=r'^login$',
        view=Login.as_view(),
        name="login",
        ),
    url(regex=r'^verified$',
        view=VerifiedPassword.as_view(),
        name="verified",
        ),
    url(regex=r'^locallogin$',
        view=LocalLogin.as_view(),
        name="locallogin",
        ),
    url(regex=r'^logout$',
        view=logout,
        name="logout",
        kwargs={'next_page': '/'}
        ),
    url(regex=r'^api/getTadminPassword/(?P<domain_fqdn>.*)$',
        view=GetTadinPassword.as_view(),
        name="getTadminPassword",
        ),

]
