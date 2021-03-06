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


from .views import Error, Myself, AdminView, InitializeUser
from .views import OnDuty, AdminCover

app_name = 'AttendanceSystem'
urlpatterns = [
    url(regex=r'^$',
        view=Error.as_view(),
        name="error",
        ),
    url(regex=r'^on_duty$',
        view=OnDuty.as_view(),
        name="on_duty",
        ),
    url(regex=r'^initialize_user$',
        view=InitializeUser.as_view(),
        name="initialize_user",
        ),
    url(regex=r'^admin_view$',
        view=AdminView.as_view(),
        name="admin_view",
        ),
    url(regex=r'^my$',
        view=Myself.as_view(),
        name="my",
        ),
    url(regex=r'^check_in$',
        view=Myself.as_view(),
        name="check_in",
        ),
    url(regex=r'^check_out$',
        view=Myself.as_view(),
        name="check_out",
        kwargs={"check_out": True}
        ),
    url(regex=r'^admin_cover/(?P<worker_db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/in$',
        view=AdminCover.as_view(),
        name="admin_cover_in",
        kwargs={"action": "in"}
        ),
    url(regex=r'^admin_cover/(?P<worker_db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/out$',
        view=AdminCover.as_view(),
        name="admin_cover_out",
        kwargs={"action": "out"}
        ),
    # url(regex=r'^verified$',
    #     view=VerifiedPassword.as_view(),
    #     name="verified",
    #     ),
    # url(regex=r'^locallogin$',
    #     view=LocalLogin.as_view(),
    #     name="locallogin",
    #     ),
    # url(regex=r'^logout$',
    #     view=logout,
    #     name="logout",
    #     kwargs={'next_page': '/'}
    #     ),
    # url(regex=r'^add_region/$',
    #     view=AddRegion.as_view(),
    #     name="add_parent_region",
    #     # kwargs={'parent_uuid': None}
    #     ),
    # url(regex=r'add_region/(?P<parent_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
    #     view=AddRegion.as_view(),
    #     name="add_child_region",
    #     ),
    # url(regex=r'add_network/(?P<region_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
    #     view=AddNetwork.as_view(),
    #     name="add_network",
    #     ),
    # url(r'^api/', include('IPAM.api')),
]
