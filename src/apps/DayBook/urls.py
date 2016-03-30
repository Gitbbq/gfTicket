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
from .views.InternetPC import Index as InternetPC_Index
from .views.InternetPC import DepartmentView as InternetPC_DepartmentView
from .views.InternetPC import PCEdit as InternetPC_PCEdit
from .views.InternetPC import DepartmentPCAdd as InternetPC_DepartmentPCAdd
from .views.InternetPC import PCInactive as InternetPC_PCInactive

app_name = 'DayBook'
urlpatterns = [
    url(regex=r'^InternetPC/$',
        view=InternetPC_Index.as_view(),
        name="InternetPC_Index",
        ),
    url(regex=r'^InternetPC/Department/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        view=InternetPC_DepartmentView.as_view(),
        name="InternetPC_DepartmentView",
        ),
    url(regex=r'^InternetPC/Department/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/PC/add$',
        view=InternetPC_DepartmentPCAdd.as_view(),
        name="InternetPC_Department_PC_add",
        ),
    url(regex=r'^InternetPC/PC/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/edit$',
        view=InternetPC_PCEdit.as_view(),
        name="InternetPC_PC_edit",
        ),
    url(regex=r'^InternetPC/PC/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/inactive$',
        view=InternetPC_PCInactive.as_view(),
        name="InternetPC_PC_inactive",
        ),

    # url(regex=r'^list',
    #     view=DocumentList.as_view(),
    #     name="list",
    #     ),
    # url(regex=r'^list/all',
    #     view=DocumentList.as_view(),
    #     name="list_all",
    #     kwargs={"show_all": True}
    #     ),
    # url(regex=r'^initialize_user$',
    #     view=InitializeUser.as_view(),
    #     name="initialize_user",
    #     ),
    # url(regex=r'^tag/list',
    #     view=TagList.as_view(),
    #     name="tag_list",
    #     ),
    # url(regex=r'^view/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
    #     view=DocumentView.as_view(),
    #     name="view",
    #     ),

]
