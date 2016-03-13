#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian@188.com"
# Stdlib imports

# Core Django imports

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _

# Third-party app imports
from apps.Core.views import BaseView
from apps.SSO.decorators import verified_required
# Imports from your apps

from .models import DocumentUser, Entry
from .models import Tag


class Error(BaseView):
    template_name = "Document/error.html"

    def get(self, request):
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class InitializeUser(BaseView):
    template_name = "Document/initialize_user.html"

    def get(self, request):
        document_user, created = DocumentUser.objects.get_or_create(user=request.user)
        document_user.save()
        return self.go_next()


class DocumentList(BaseView):
    template_name = "Document/list.html"

    def get(self, request, show_all=False):
        entries = Entry.objects
        if not request.user.is_authenticated() or not request.session.get("verified", False):
            entries = entries.filter(require_permission=0)
        elif request.session.get("verified", False):
            entries = entries.filter(require_permission__lte=request.user.document_user.permission)

        if show_all:
            entries = entries.all()
        else:
            entries = entries.all()[0:50]

        self.response_dict['entries'] = entries
        return self.response()


class DocumentView(BaseView):
    template_name = "Document/view.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        entry = Entry.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["entry"] = entry
        if entry.require_permission > 0 and (not request.user.is_authenticated() or not request.session.get("verified", False)):
            return self.go(viewname="Document:error", ext_url="?error=" + _("访客无权浏览这个文档"))
        if entry.require_permission > 0 and (request.user.document_user.permission < entry.require_permission):
            return self.go(viewname="Document:error", ext_url="?error=" + _("权限不足以浏览这个文档"))
        return self.response()


class TagList(BaseView):
    template_name = "Document/tag_list.html"

    def get(self, request):
        tags = Tag.objects.all()
        self.response_dict['tags'] = tags
        return self.response()


class TagView(BaseView):
    template_name = "Document/tag_view.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        tag = Tag.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict['tag'] = tag
        entries = tag.entries
        if not request.user.is_authenticated() or not request.session.get("verified", False):
            entries = entries.filter(require_permission=0)
        elif request.session.get("verified", False):
            entries = entries.filter(require_permission__lte=request.user.document_user.permission)
        entries = entries.all()
        self.response_dict["entries"] = entries

        return self.response()
