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

# Third-party app imports
from apps.Core.views import BaseView
from apps.Core.views import user2pass
# Imports from your apps
from .forms import LoginForm, VerifiedPasswordForm, LocalLoginForm
from .models import DomainUser
from .decorators import domain_logon_required


class Login(BaseView):
    template_name = "SSO/login.html"

    def get(self, request):
        form = LoginForm()
        # form.fields["domain"] = forms.ModelChoiceField(DomainSetting.objects)
        self.response_dict["form"] = form
        return self.response()

    def post(self, request):
        form = LoginForm(request.POST)
        self.response_dict["form"] = form
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            domain = form.cleaned_data['domain']
            domain_user = domain.get_user(username).entry_get_attributes_dict()

            local_username = "%s@%s" % (username, domain.fqdn)
            local_password = user2pass(local_username)
            local_user, created = User.objects.get_or_create(username=local_username)
            local_user.set_password(local_password)
            local_user.save()

            local_domain_user, created = DomainUser.objects.get_or_create(username=username, domain=domain, user=local_user)
            local_domain_user.cn = domain_user.get("cn", [None])[0]
            local_domain_user.displayName = domain_user.get("displayName", [None])[0]
            local_domain_user.distinguishedName = domain_user.get("distinguishedName", [None])[0]
            local_domain_user.givenName = domain_user.get("givenName", [None])[0]
            local_domain_user.sn = domain_user.get("sn", [None])[0]
            local_domain_user.initials = domain_user.get("initials", [None])[0]
            local_domain_user.mail = domain_user.get("mail", [None])[0]
            local_domain_user.userPrincipalName = domain_user.get("userPrincipalName", [None])[0]
            local_domain_user.save()
            request.session.flush()
            login_user = authenticate(username=local_username, password=local_password)
            login(request, login_user)
            request.session["verified"] = False
            request.session["is_domain_user"] = True
            return self.go_next()

        return self.response()


class VerifiedPassword(BaseView):
    @method_decorator(login_required)
    @method_decorator(domain_logon_required())
    def dispatch(self, *args, **kwargs):
        return super(VerifiedPassword, self).dispatch(*args, **kwargs)

    template_name = "SSO/verified.html"

    def get(self, request):
        form = VerifiedPasswordForm(initial={'domain': request.user.sso_user.domain.NetBIOS, 'username': request.user.sso_user.username})
        # form.fields["domain"] = forms.ModelChoiceField(DomainSetting.objects)
        self.response_dict["form"] = form
        return self.response()

    def post(self, request):
        form = VerifiedPasswordForm(request.POST)
        self.response_dict["form"] = form
        if form.is_valid():
            request.session["verified"] = True
            return self.go_next()
        return self.response()


class LocalLogin(BaseView):
    template_name = "SSO/locallogin.html"

    def get(self, request):
        form = LocalLoginForm()
        self.response_dict["form"] = form
        return self.response()

    def post(self, request):
        form = LocalLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session["verified"] = True
            request.session["is_domain_user"] = False
            return self.go_next()
        self.response_dict["form"] = form
        return self.response()
