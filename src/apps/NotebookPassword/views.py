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
# under the License.# Create your views here.
# Stdlib imports

# Core Django imports
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
# Third-party app imports
from apps.Core.views import BaseView

# Imports from your apps
from .make_password import make_password_list, only_upper_char_and_num
from .forms import SNForm


class Index(BaseView):
    template_name = "NotebookPassword/index.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)

    def get(self, request):
        self.response_dict['form'] = SNForm()
        return self.response()

    def post(self, request):
        form = SNForm(request.POST)
        if form.is_valid():
            sn = form.cleaned_data['sn']
            self.response_dict['password_list'] = make_password_list(sn)
            self.response_dict['clean_sn'] = only_upper_char_and_num(sn)
        else:
            self.response_dict['password_list'] = None
        self.response_dict['form'] = form
        return self.response()
