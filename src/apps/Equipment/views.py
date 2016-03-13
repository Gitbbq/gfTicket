#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports

# Third-party app imports
from apps.Core.views import BaseView

# Imports from your apps
from .models import EquipmentModel


class EquipmentModelView(BaseView):
    template_name = "Equipment/view.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        equipment_model = EquipmentModel.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["equipment_model"] = equipment_model
        return self.response()
