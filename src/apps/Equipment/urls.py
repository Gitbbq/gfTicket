#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.conf.urls import url

# Third-party app imports

# Imports from your apps


from .views import EquipmentModelView

app_name = 'Equipment'
urlpatterns = [
    url(regex=r'^equipment_model/(?P<db_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        view=EquipmentModelView.as_view(),
        name="equipment_model_view",
        ),
]
