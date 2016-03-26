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

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
# Third-party app imports
from apps.Core.views import BaseView
from apps.SSO.decorators import verified_required
from apps.BranchManager.models import Department

# Imports from your apps

from ..models import InternetPC, InternetPCLog
from ..forms.InternetPC import InternetPCForm


class Index(BaseView):
    template_name = "DayBook/InternetPC/index.html"

    def get(self, request):
        self.response_dict["department_list"] = Department.objects.filter(db_active=True).all()
        return self.response()


# @method_decorator(login_required, name='dispatch')
# @method_decorator(verified_required, name='dispatch')

class DepartmentView(BaseView):
    template_name = "DayBook/InternetPC/department.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        department = Department.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["department"] = department
        self.response_dict["pc_list"] = InternetPC.objects.filter(department=department).filter(db_active=True).all()
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class PCEdit(BaseView):
    template_name = "DayBook/InternetPC/edit.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        pc = InternetPC.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["pc"] = pc
        self.response_dict["form"] = InternetPCForm(instance=pc)
        return self.response()

    def post(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        pc = InternetPC.objects.get(db_uuid=self.response_dict["db_uuid"])
        form = InternetPCForm(data=request.POST, instance=pc)
        if form.is_valid():
            pc.save()
            InternetPCLog.objects.create(user=request.user, pc=pc, history=serializers.serialize('json', [pc, ]))
            return self.go_self()
        self.response_dict["form"] = form
        self.response_dict["pc"] = pc
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class DepartmentPCAdd(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        department = Department.objects.get(db_uuid=self.response_dict["db_uuid"])
        new_pc = InternetPC.objects.create(department=department)
        return self.go(viewname="DayBook:InternetPC_PC_edit", kwargs={"db_uuid": new_pc.db_uuid})


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class PCInactive(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        pc = InternetPC.objects.get(db_uuid=self.response_dict["db_uuid"])
        pc.db_active = False
        pc.save()
        InternetPCLog.objects.create(user=request.user, pc=pc, history=serializers.serialize('json', [pc, ]))
        return self.go_back()
