#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liantian'
__email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Third-party app imports

# Imports from your apps


def verified_required(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if not request.session.get("verified", False):
                return HttpResponseRedirect(reverse(viewname="SSO:verified") + "?next=" + request.path)
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def domain_logon_required(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if not request.session.get("is_domain_user", False):
                return HttpResponseRedirect(reverse(viewname="SSO:login") + "?next=" + request.path)
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
