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
import hashlib
from json import dumps
# Core Django imports
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse


# Third-party app imports

# Imports from your apps

class BaseView(View):
    response_dict = {}
    template_name = "index.html"
    request = None
    status = 200

    def setup(self, request):
        self.response_dict.clear()
        self.request = request

    def dispatch(self, request, *args, **kwargs):
        self.setup(request)
        return View.dispatch(self, request, *args, **kwargs)

    def response(self, template_name=None, content_type="text/html", status=None):
        if template_name is not None:
            self.template_name = template_name
        if status is not None:
            self.status = status
        return render(request=self.request,
                      template_name=self.template_name,
                      context=self.response_dict,
                      content_type=content_type,
                      status=status)

    def go_back(self):
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])

    @staticmethod
    def go(viewname, kwargs={}, ext_url=""):
        return HttpResponseRedirect(reverse(viewname=viewname, kwargs=kwargs) + ext_url)

    def go_self(self):
        return HttpResponseRedirect(self.request.path)

    @staticmethod
    def go_index():
        return HttpResponseRedirect("/")

    def go_next(self):
        return HttpResponseRedirect(self.request.GET.get('next', "/"))

    @staticmethod
    def good():
        # 服务器成功处理了请求，但未返回任何内容。
        return HttpResponse(status=204)

    @staticmethod
    def response_json(data):
        return HttpResponse(dumps(data), content_type="application/json")





def user2pass(username):
    r1 = hashlib.md5(username.encode()).hexdigest()
    r2 = hashlib.sha1(r1.encode()).hexdigest()
    return r2
