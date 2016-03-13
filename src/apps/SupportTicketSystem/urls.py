#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.conf.urls import url
# Third-party app imports

# Imports from your apps
from .views import CreateTicket
from .views import InitializeUser
from .views import Error
from .views import ReplenishTicket
from .views import Me
from .views import Admin
from .views import ViewTicket
from .views import PickTicket
from .views import CompleteTicket
from .views import SetLevel
from .views import CreateProject
from .views import ViewProjectEvent
from .views import CompleteProjectEvent
from .views import ViewProject
from .views import AfterSaleProtectionTicket, PushAdminTicket

app_name = 'SupportTicketSystem'
urlpatterns = [
    url(regex=r'^create_project$',
        view=CreateProject.as_view(),
        name="create_project",
        ),
    url(regex=r'^create_ticket$',
        view=CreateTicket.as_view(),
        name="create_ticket",
        ),
    url(regex=r'^me$',
        view=Me.as_view(),
        name="me",
        ),
    url(regex=r'^admin$',
        view=Admin.as_view(),
        name="admin",
        ),
    url(regex=r'^initialize_user$',
        view=InitializeUser.as_view(),
        name="initialize_user",
        ),
    url(regex=r'^$',
        view=Error.as_view(),
        name="error",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/replenish$',
        view=ReplenishTicket.as_view(),
        name="replenish_ticket",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/view$',
        view=ViewTicket.as_view(),
        name="view_ticket",
        ),
    url(regex=r'^project_event/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/view$',
        view=ViewProjectEvent.as_view(),
        name="view_project_event",
        ),
    url(regex=r'^project/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/view$',
        view=ViewProject.as_view(),
        name="view_project",
        ),
    url(regex=r'^project_event/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/complete$',
        view=CompleteProjectEvent.as_view(),
        name="complete_project_event",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/pick$',
        view=PickTicket.as_view(),
        name="ticket_pick",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/complete$',
        view=CompleteTicket.as_view(),
        name="complete_ticket",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/up$',
        view=SetLevel.as_view(),
        name="ticket_up",
        kwargs={"up": True}
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/down$',
        view=SetLevel.as_view(),
        name="ticket_down",
        kwargs={"up": False}
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/after_sale_protection$',
        view=AfterSaleProtectionTicket.as_view(),
        name="after_sale_protection",
        ),
    url(regex=r'^ticket/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/push_admin$',
        view=PushAdminTicket.as_view(),
        name="push_admin",
        ),
]
