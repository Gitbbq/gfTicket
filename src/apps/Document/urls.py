#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
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
