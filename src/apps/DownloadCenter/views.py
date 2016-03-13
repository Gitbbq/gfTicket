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

from .forms import AttachmentForm
from .models import Attachment
from .models import Driver, BusinessSoftware


class AttachmentView(BaseView):
    template_name = "DownloadCenter/attachment.html"

    def get(self, request):
        self.response_dict["form"] = AttachmentForm()
        self.response_dict["attachments"] = Attachment.objects.all()
        return self.response()

    def post(self, request):
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.go(viewname="DownloadCenter:attachment")
        else:
            self.response_dict["form"] = form
            return self.response()


class DriverView(BaseView):
    template_name = "DownloadCenter/driver.html"

    def get(self, request):
        self.response_dict["drivers"] = Driver.objects.all()
        return self.response()


class BusinessSoftwareView(BaseView):
    template_name = "DownloadCenter/business_software.html"

    def get(self, request):
        self.response_dict["entries"] = BusinessSoftware.objects.all()
        return self.response()
