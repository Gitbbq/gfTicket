#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liantian'
__email__ = "liantian@188.com"
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


class Index(BaseView):
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)

    def get(self, request):
        return self.response(template_name="index.html")


def user2pass(username):
    r1 = hashlib.md5(username.encode()).hexdigest()
    r2 = hashlib.sha1(r1.encode()).hexdigest()
    return r2
