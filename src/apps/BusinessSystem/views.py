#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports

# Third-party app imports
from apps.Core.views import BaseView

# Imports from your apps
from .models import System as BusinessSystem


#

class BSView(BaseView):
    template_name = "BusinessSystem/bs_view.html"

    def get(self, request):
        self.response_dict["bs_system"] = BusinessSystem.objects.filter(bs=True).filter(db_active=True).all()
        return self.response()


class BusinessSystemView(BaseView):
    template_name = "BusinessSystem/view.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        system = BusinessSystem.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["system"] = system
        return self.response()
