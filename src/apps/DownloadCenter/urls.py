#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.conf.urls import url

# Third-party app imports

# Imports from your apps


# from .views import Error, Myself, AdminView, InitializeUser
# from .views import OnDuty
from .views import AttachmentView, DriverView, BusinessSoftwareView

app_name = 'DownloadCenter'
urlpatterns = [
    url(regex=r'^attachment$',
        view=AttachmentView.as_view(),
        name="attachment",
        ),
    url(regex=r'^driver$',
        view=DriverView.as_view(),
        name="driver",
        ),
    url(regex=r'^business_software',
        view=BusinessSoftwareView.as_view(),
        name="business_software",
        ),
    # url(regex=r'^on_duty$',
    #     view=OnDuty.as_view(),
    #     name="on_duty",
    #     ),
    # url(regex=r'^initialize_user$',
    #     view=InitializeUser.as_view(),
    #     name="initialize_user",
    #     ),
    # url(regex=r'^admin_view$',
    #     view=AdminView.as_view(),
    #     name="admin_view",
    #     ),
    # url(regex=r'^my$',
    #     view=Myself.as_view(),
    #     name="my",
    #     ),
    # url(regex=r'^check_in$',
    #     view=Myself.as_view(),
    #     name="check_in",
    #     ),
    # url(regex=r'^check_out$',
    #     view=Myself.as_view(),
    #     name="check_out",
    #     kwargs={"check_out": True}
    #     ),
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
