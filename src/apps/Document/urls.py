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
from django.conf.urls import url
# Third-party app imports

# Imports from your apps


from .views import InitializeUser
from .views import Error
from .views import DocumentList
from .views import DocumentView
from .views import TagList
from .views import TagView

# from .views import OnDuty

app_name = 'Document'
urlpatterns = [
    url(regex=r'^error$',
        view=Error.as_view(),
        name="error",
        ),
    url(regex=r'^list',
        view=DocumentList.as_view(),
        name="list",
        ),
    url(regex=r'^list/all',
        view=DocumentList.as_view(),
        name="list_all",
        kwargs={"show_all": True}
        ),
    url(regex=r'^initialize_user$',
        view=InitializeUser.as_view(),
        name="initialize_user",
        ),
    url(regex=r'^tag/list',
        view=TagList.as_view(),
        name="tag_list",
        ),
    url(regex=r'^view/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        view=DocumentView.as_view(),
        name="view",
        ),
    url(regex=r'^tag/view/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        view=TagView.as_view(),
        name="tag_view",
        ),

]
