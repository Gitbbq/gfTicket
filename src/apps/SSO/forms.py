#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian@188.com"
# Stdlib imports
import logging

from ldap3.utils.log import set_library_log_detail_level, EXTENDED

# Core Django imports

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

# Third-party app imports


# Imports from your apps
from .models import ADServer

logger = logging.getLogger(__name__)
set_library_log_detail_level(EXTENDED)


class LoginForm(forms.Form):
    domain = forms.ModelChoiceField(queryset=ADServer.objects, to_field_name="fqdn", required=True, label=_('域'))
    username = forms.CharField(label=_('用户名'), help_text=_(""), required=True, max_length=24, min_length=4)

    def clean_domain(self):
        data = self.cleaned_data.get('domain')
        try:
            ADServer.objects.get(NetBIOS=data)
            return data
        except ObjectDoesNotExist:
            raise forms.ValidationError("domain not Find")

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        domain = cleaned_data.get('domain')

        if domain.get_user(username) is None:
            raise forms.ValidationError(_("用户名错误"))
        else:
            return cleaned_data


class VerifiedPasswordForm(forms.Form):
    domain = forms.CharField(label=_('域'), widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(label=_('用户'), widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    password = forms.CharField(label=_('密码'), help_text=_("认证以获得完整权限"), max_length=24, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(VerifiedPasswordForm, self).clean()
        username = cleaned_data.get('username')
        domain = cleaned_data.get('domain')
        password = cleaned_data.get('password')

        ad = ADServer.objects.get(NetBIOS=domain)

        if not ad.test_user_password(username, password):
            raise forms.ValidationError(_("密码错误"))
        else:
            return cleaned_data


class LocalLoginForm(forms.Form):
    username = forms.CharField(label=_('用户名'), help_text=_(""), required=True, max_length=24, min_length=4)
    password = forms.CharField(label=_('密码'), help_text=_(""), max_length=24, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LocalLoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return cleaned_data
            else:
                raise forms.ValidationError(_("用户已禁用"))
        else:
            raise forms.ValidationError(_("密码错误"))
