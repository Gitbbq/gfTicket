#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian@188.com"
# Stdlib imports
import logging

# Core Django imports

from django.forms import ModelForm

# Third-party app imports


# Imports from your apps
from .models import Attachment

logger = logging.getLogger(__name__)


class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
        fields = ['orig_file']
