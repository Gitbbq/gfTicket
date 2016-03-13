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
