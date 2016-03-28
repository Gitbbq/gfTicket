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
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseBadRequest

# Third-party app imports
from apps.Core.views import BaseView
from apps.Core.views import user2pass

# Imports from your apps

from ..models import DomainSetting


class GetTadinPassword(BaseView):
    def get(self, request, domain_fqdn):
        ua = request.META.get("HTTP_USER_AGENT", "192.168.1.1")
        if not ua == "gfTicket":
            return HttpResponseBadRequest()
        domain = DomainSetting.objects.get(fqdn__icontains=domain_fqdn)
        return HttpResponse("%s\n%s" % (domain.connect_user, domain.connect_pass))
