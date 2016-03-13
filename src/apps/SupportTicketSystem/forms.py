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

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps

from apps.BranchManager.models import Department
from .models import Ticket, Project, TicketFile, ProjectFile, ProjectEventFile


class CreateProjectForm2(forms.Form):
    department = forms.ModelMultipleChoiceField(queryset=Department.objects, required=True, label=_('网点/部门*'), help_text=_("输入行所或缩写快速查找。"))
    # contact = forms.CharField(label=_('报障人姓名*'), required=True, widget=forms.TextInput(attrs={'placeholder': _("必填")}))
    # telephone = forms.CharField(label=_('联系方式*'), required=True, max_length=11, min_length=4, widget=forms.TextInput(attrs={'placeholder': _("必填")}))
    # troubles = forms.ModelMultipleChoiceField(queryset=Trouble.objects.filter(db_active=True), required=True, label=_('故障现象*'), help_text=_("必须且多选"))
    # tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(db_active=True), required=False, label=_('标签'))
    # relevant_business = forms.ModelMultipleChoiceField(queryset=BusinessSystem.objects.filter(db_active=True), required=False, label=_("涉及系统"))
    # relevant_equipment = forms.ModelMultipleChoiceField(queryset=EquipmentModel.objects.filter(db_active=True), required=False, label=_("涉及硬件"))
    # detail = forms.CharField(widget=forms.Textarea, label=_("其他描述"), required=False, help_text=_("支持Markdown格式。"))


class CreateProjectForm1(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'scheduled_time', 'detail', 'level', 'tag', 'relevant_business', 'relevant_equipment']


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['department', 'contact_name', 'contact_telephone', 'troubles', 'tag', 'responsible_person']


class ReplenishTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['relevant_business', 'relevant_equipment', 'incidence', 'detail', 'scheduled_time']


class AppointTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['responsible_person']


class TicketFileForm(ModelForm):
    class Meta:
        model = TicketFile
        fields = ['orig_file', 'ticket']
        widgets = {'ticket': forms.HiddenInput()}


class ProjectFileForm(ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['orig_file', 'project']
        widgets = {'project': forms.HiddenInput()}


class ProjectEventFileForm(ModelForm):
    class Meta:
        model = ProjectEventFile
        fields = ['orig_file', 'project_event']
        widgets = {'project_event': forms.HiddenInput()}
