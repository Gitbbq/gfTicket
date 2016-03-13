#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.conf.urls import url

# Third-party app imports

# Imports from your apps


from .views import BSView
from .views import BusinessSystemView

app_name = 'BusinessSystem'
urlpatterns = [
    url(regex=r'^bs$',
        view=BSView.as_view(),
        name="bs_view",
        ),
    url(regex=r'^system/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        view=BusinessSystemView.as_view(),
        name="system_view",
        ),
]
