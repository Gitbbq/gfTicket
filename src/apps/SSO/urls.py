#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.conf.urls import url
from django.contrib.auth.views import logout
# Third-party app imports

# Imports from your apps

from .views import Login, VerifiedPassword, LocalLogin

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
