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

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from apps.Core.views import BaseView
from apps.SSO.decorators import verified_required
from apps.BranchManager.models import Department, DepartmentType
from .forms import CreateTicketForm, ReplenishTicketForm, AppointTicketForm, CreateProjectForm1, CreateProjectForm2, TicketFileForm, ProjectFileForm, ProjectEventFileForm
from .models import SupportTicketSystemUser, Ticket, ProjectEvent, Project
from .decorators import has_support_ticket_system_user, verified_support_ticket_system_user_is_watcher, verified_support_ticket_system_user_is_admin


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class InitializeUser(BaseView):
    template_name = "SupportTicketSystem/initialize_user.html"

    def get(self, request):
        support_ticket_system_user, created = SupportTicketSystemUser.objects.get_or_create(user=request.user)
        support_ticket_system_user.save()
        return self.go_next()


class Error(BaseView):
    template_name = "SupportTicketSystem/error.html"

    def get(self, request):
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
@method_decorator(verified_support_ticket_system_user_is_watcher, name='dispatch')
class CreateTicket(BaseView):
    template_name = "SupportTicketSystem/create_ticket.html"

    def get(self, request):
        form = CreateTicketForm()
        self.response_dict["form"] = form
        return self.response()

    def post(self, request):
        form = CreateTicketForm(request.POST)
        self.response_dict["form"] = form
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user.support_ticket_system_user
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Create"})
            ticket.save()
            form.save_m2m()
            ticket.transfer_attr()
            messages.add_message(request, messages.INFO, _('请补充信息'))
            return self.go("SupportTicketSystem:replenish_ticket", kwargs={"db_uuid": ticket.db_uuid})

        messages.add_message(request, messages.ERROR, _('提交失败'))
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
@method_decorator(verified_support_ticket_system_user_is_watcher, name='dispatch')
class ReplenishTicket(BaseView):
    template_name = "SupportTicketSystem/replenish_ticket.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        form = ReplenishTicketForm(instance=ticket)
        self.response_dict["form"] = form
        return self.response()

    def post(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        form = ReplenishTicketForm(data=request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.level = ticket.incidence
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Replenish"})
            ticket.save()
            form.save_m2m()
            messages.add_message(request, messages.SUCCESS, _('提交成功'))
            return self.go("SupportTicketSystem:create_ticket")
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class Me(BaseView):
    template_name = "SupportTicketSystem/me.html"

    def get(self, request):
        my_user = request.user.support_ticket_system_user
        my_area = my_user.precinct.filter().all()
        my_department = Department.objects.filter(area__in=my_area).filter(db_active=True).all()

        # ticket_related_query = Ticket.objects.prefetch_related("department").prefetch_related("project").prefetch_related("completed_person")

        self.response_dict["my_department"] = my_department
        my_department_ticket = Ticket.related_objects().filter(department__in=my_department).filter(db_active=True).filter(completed=False).order_by('-level',
                                                                                                                                                     "scheduled_time").all()
        self.response_dict["my_department_ticket"] = my_department_ticket
        my_responsible_ticket = Ticket.related_objects().filter(responsible_person=my_user).filter(db_active=True).filter(completed=False).order_by('-level',
                                                                                                                                                    "scheduled_time").all()
        self.response_dict["my_responsible_ticket"] = my_responsible_ticket
        my_completed_ticket = Ticket.related_objects().filter(completed_person=my_user).filter(db_active=True).filter(completed=True).order_by("-completed_time").all()[0:15]
        self.response_dict["my_completed_ticket"] = my_completed_ticket
        self.response_dict["my_ticket"] = my_responsible_ticket | my_department_ticket

        my_department_event = ProjectEvent.related_objects().filter(department__in=my_department).filter(db_active=True).filter(completed=False).all()
        self.response_dict["my_department_event"] = my_department_event
        self.response_dict["my_event"] = my_department_event

        my_department_completed_event = ProjectEvent.related_objects().filter(department__in=my_department).filter(db_active=True).filter(completed=True).order_by(
            "-completed_time").all()
        self.response_dict["my_completed_event"] = my_department_completed_event

        my_completed_event = ProjectEvent.related_objects().filter(completed_person=my_user).filter(db_active=True).filter(completed=True).order_by("-completed_time").all()
        self.response_dict["my_completed_event"] = my_completed_event

        self.response_dict["completed_event"] = (my_completed_event | my_department_completed_event)[0:10]

        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class Admin(BaseView):
    template_name = "SupportTicketSystem/admin.html"

    def get(self, request):
        self.response_dict["not_complete_ticket"] = Ticket.related_objects().filter(db_active=True).filter(completed=False).all()
        self.response_dict["not_complete_project"] = Project.related_objects().filter(db_active=True).filter(completed=False).all()
        self.response_dict["complete_project"] = Project.related_objects().filter(db_active=True).filter(completed=True).order_by("-completed_time").all()[0:5]
        self.response_dict["all_completed_ticket"] = Ticket.related_objects().filter(db_active=True).filter(completed=True).order_by("-completed_time").all()[0:50]
        return self.response()


@method_decorator(login_required, name='dispatch')
class ViewTicket(BaseView):
    template_name = "SupportTicketSystem/view_ticket.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["ticket"] = ticket
        self.response_dict["appoint_ticket_form"] = AppointTicketForm(instance=ticket, prefix="appoint")
        self.response_dict["file_form"] = TicketFileForm(initial={"ticket": ticket})

        return self.response()

    def post(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        appoint_ticket_form = AppointTicketForm(data=request.POST, instance=ticket, prefix="appoint")
        file_form = TicketFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
        if appoint_ticket_form.is_valid():
            ticket = appoint_ticket_form.save(commit=False)
            ticket.process.setdefault("log", []).append(
                {"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Appoint : %s" % ticket.responsible_person})
            ticket.save()
        return self.go_self()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class PickTicket(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        ticket.responsible_person = request.user.support_ticket_system_user
        ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Pick"})
        ticket.save()
        self.response_dict["ticket"] = ticket
        return self.go_back()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class CompleteTicket(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        if not ticket.completed:
            ticket.completed_person = request.user.support_ticket_system_user
            ticket.completed_time = timezone.datetime.now()
            ticket.completed = True
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Complete"})
        elif ticket.completed:
            ticket.completed_person = None
            ticket.completed_time = None
            ticket.completed = False
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Incomplete"})
        ticket.save()
        self.response_dict["ticket"] = ticket
        return self.go_back()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
@method_decorator(verified_support_ticket_system_user_is_admin(), name='dispatch')
class SetLevel(BaseView):
    def get(self, request, db_uuid, up):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        if up:
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "UpLevel"})
            ticket.level += 2.0
        else:
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "DownLevel"})
            ticket.level += -2.0
        ticket.save()
        return self.go_back()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
@method_decorator(verified_support_ticket_system_user_is_admin, name='dispatch')
class CreateProject(BaseView):
    template_name = "SupportTicketSystem/create_project.html"

    def get(self, request):
        form1 = CreateProjectForm1(prefix="form1")
        form2 = CreateProjectForm2(prefix="form2")
        department_types = DepartmentType.objects.filter(db_active=True).all()
        self.response_dict["form1"] = form1
        self.response_dict["form2"] = form2
        self.response_dict["department_types"] = department_types
        return self.response()

    def post(self, request):
        form1 = CreateProjectForm1(data=request.POST, prefix="form1")
        form2 = CreateProjectForm2(data=request.POST, prefix="form2")

        if form1.is_valid() and form2.is_valid():
            project = form1.save(commit=False)
            project.creator = request.user.support_ticket_system_user
            project.save()
            for department in form2.cleaned_data['department']:
                event, created = ProjectEvent.objects.get_or_create(department=department, project=project, level=project.level)
            form1 = CreateProjectForm1(prefix="form1")
            form2 = CreateProjectForm2(prefix="form2")
        self.response_dict["form1"] = form1
        self.response_dict["form2"] = form2
        return self.response()


@method_decorator(login_required, name='dispatch')
class ViewProjectEvent(BaseView):
    template_name = "SupportTicketSystem/view_project_event.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        event = ProjectEvent.related_objects().get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["event"] = event
        self.response_dict["file_form"] = ProjectEventFileForm(initial={"project_event": event})
        return self.response()

    def post(self, request, db_uuid):
        file_form = ProjectEventFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
        return self.go_self()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class CompleteProjectEvent(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        event = ProjectEvent.objects.get(db_uuid=self.response_dict["db_uuid"])
        if not event.completed:
            event.completed_person = request.user.support_ticket_system_user
            event.completed_time = timezone.datetime.now()
            event.completed = True
            event.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Complete"})
        elif event.completed:
            event.completed_person = None
            event.completed_time = None
            event.completed = False
            event.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Incomplete"})
        event.save()
        self.response_dict["event"] = event
        return self.go_back()


@method_decorator(login_required, name='dispatch')
class ViewProject(BaseView):
    template_name = "SupportTicketSystem/view_project.html"

    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        project = Project.related_objects().get(db_uuid=self.response_dict["db_uuid"])
        self.response_dict["project"] = project
        self.response_dict["file_form"] = ProjectFileForm(initial={"project": project})
        return self.response()

    def post(self, request, db_uuid):
        file_form = ProjectFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
        return self.go_self()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class AfterSaleProtectionTicket(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        if not ticket.after_sale_protection:
            ticket.after_sale_protection = True
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Set AfterSaleProtection"})
        elif ticket.after_sale_protection:
            ticket.after_sale_protection = False
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "unSet AfterSaleProtection"})
        ticket.save()
        self.response_dict["ticket"] = ticket
        return self.go_back()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_support_ticket_system_user, name='dispatch')
class PushAdminTicket(BaseView):
    def get(self, request, db_uuid):
        self.response_dict["db_uuid"] = db_uuid
        ticket = Ticket.objects.get(db_uuid=self.response_dict["db_uuid"])
        if not ticket.push_to_admin:
            ticket.push_to_admin = True
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "Set PushAdmin"})
        elif ticket.push_to_admin:
            ticket.push_to_admin = False
            ticket.process.setdefault("log", []).append({"time": timezone.datetime.now().isoformat(), "user": request.user.username, "action": "unSet PushAdmin"})
        ticket.save()
        self.response_dict["ticket"] = ticket
        return self.go_back()
