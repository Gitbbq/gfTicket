#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports


# Core Django imports
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Third-party app imports

# Imports from your apps
from apps.Core.models import CommonModel, DownloadModel
from apps.BusinessSystem.models import System as BusinessSystem
from apps.BranchManager.models import Department, Area
from apps.Equipment.models import EquipmentModel

# Create your models here.

INCIDENCE_CHOICES = (
    (0.0, _(u"一个人")),
    (1.0, _(u"多个人")),
    (2.0, _(u"一个部门")),
    (3.0, _(u"一个网点/多个部门")),
)


class SupportTicketSystemUser(CommonModel):
    user = models.OneToOneField(User, verbose_name=_("对应用户"), related_name="support_ticket_system_user")
    is_watcher = models.BooleanField(default=False, verbose_name=_('是值班员（有登记权限）'))
    is_worker = models.BooleanField(default=False, verbose_name=_('员工'))
    is_admin = models.BooleanField(default=False, verbose_name=_('完全管理员'))
    precinct = models.ManyToManyField(Area, blank=True, verbose_name=_("管辖区域"), related_name="responsible_person")

    def __unicode__(self):
        try:
            result = self.user.sso_user.displayName
            result = result.split("/")[0]
            if result is None:
                result = self.user.get_full_name()
        except:
            result = self.user.get_full_name()
        return result

    class Meta:
        verbose_name = _("工单系统用户")
        verbose_name_plural = verbose_name


class Trouble(CommonModel):
    title = models.CharField(max_length=127, verbose_name=_("现象"))
    for_short = models.CharField(max_length=24, default=" ", verbose_name=_("缩写"))
    detail = models.TextField(verbose_name=_("详细信息"), blank=True, null=True, help_text=_("任何其他重要信息"))

    need_completed_by_admin = models.BooleanField(default=False, verbose_name=_("是否必须由管理员完成"))
    responsible_person = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("指定责任人"), blank=True, null=True)
    relevant_business = models.ManyToManyField(BusinessSystem, verbose_name=_("涉及系统"), blank=True)
    relevant_equipment = models.ManyToManyField(EquipmentModel, verbose_name=_("涉及硬件"), blank=True)

    def __unicode__(self):
        return '%s[%s]' % (self.title, self.for_short)

    class Meta:
        verbose_name = _("故障现象")
        verbose_name_plural = verbose_name


class Tag(CommonModel):
    title = models.CharField(max_length=127, verbose_name=_("标签"))
    for_short = models.CharField(max_length=24, default=" ", verbose_name=_("缩写"))
    detail = models.TextField(verbose_name=_("详细信息"), blank=True, null=True, help_text=_("任何其他重要信息"))

    def __unicode__(self):
        return '%s[%s]' % (self.title, self.for_short)

    class Meta:
        verbose_name = _("标签")
        verbose_name_plural = verbose_name


class Ticket(CommonModel):
    start_time = models.DateTimeField(auto_now_add=True, verbose_name=_("登记时间"))
    creator = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("创建者"), related_name="created_ticket")

    # 登记信息，必须的
    department = models.ForeignKey(Department, verbose_name=_("网点/部门"), related_name="responsible_ticket", limit_choices_to={'db_active': True}, )
    # contact = JSONField(verbose_name=_("联系人"), default={"name": None, "telephone": None})
    contact_name = models.CharField(max_length=127, verbose_name=_("联系人"))
    contact_telephone = models.CharField(max_length=127, verbose_name=_("电话"))
    # troubles = ArrayField(models.CharField(max_length=200), verbose_name=_("故障现象"))
    troubles = models.ManyToManyField(Trouble, verbose_name=_("故障现象"), related_name="ticket", limit_choices_to={'db_active': True}, )
    # tag = ArrayField(models.CharField(max_length=200), blank=True, verbose_name=_("标签"))
    tag = models.ManyToManyField(Tag, verbose_name=_("标签"), related_name="ticket", blank=True, limit_choices_to={'db_active': True},
                                 help_text=_("选择项目或特殊事件，默认留空即可"), )

    # 登记信息，不必须
    detail = models.TextField(verbose_name=_("详细信息"), blank=True, null=True, help_text=_("设备序列号、用户帐号、任何其他重要信息"))

    responsible_person = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("责任人"), related_name="responsible_ticket", blank=True, null=True,
                                           help_text=_("一般事件留空即可，会自动根据区域安排"), limit_choices_to={'is_worker': True})

    # 相关
    relevant_business = models.ManyToManyField(BusinessSystem, verbose_name=_("涉及系统"), related_name="relevant_ticket", blank=True,
                                               help_text=_('涉及的业务系统，没有请留空'))
    # relevant_business = ArrayField(models.CharField(max_length=200), verbose_name=_("涉及系统"), blank=True)
    relevant_equipment = models.ManyToManyField(EquipmentModel, verbose_name=_("涉及硬件"), related_name="relevant_ticket", blank=True,
                                                help_text=_('涉及的硬件设备类型，请尽量准确，没有请留空'))
    # relevant_equipment = ArrayField(models.CharField(max_length=200), verbose_name=_("涉及硬件"), blank=True)

    # 级别设置
    level = models.FloatField(default=0.0, verbose_name=_("故障级别"), db_index=True)
    incidence = models.FloatField(default=0.0, verbose_name=_("影响范围"), choices=INCIDENCE_CHOICES)

    # 过程信息
    process = JSONField(verbose_name=_("处理信息"), default={"workflow": [], "log": []}, editable=False)

    # 完成统计
    completed = models.BooleanField(default=False, verbose_name=_("是否已完成"))
    completed_time = models.DateTimeField(verbose_name=_("完成事件"), null=True, blank=True)
    completed_person = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("完成人"), related_name="completed_ticket", blank=True, null=True)

    # 预约功能
    scheduled_time = models.DateTimeField(default=timezone.now, verbose_name=_("计划开始日期"), help_text=_("默认为当前时间立即开始"), db_index=True)

    after_sale_protection = models.BooleanField(default=False, verbose_name=_("是否交维保处理"))

    need_completed_by_admin = models.BooleanField(default=False, verbose_name=_("是否必须由管理员完成"))
    push_to_admin = models.BooleanField(default=False, verbose_name=_("提交给管理员"))

    @staticmethod
    def related_objects():
        return Ticket.objects.prefetch_related("creator").prefetch_related("department").prefetch_related("responsible_person").prefetch_related("tag").prefetch_related(
            "relevant_business").prefetch_related("relevant_equipment").prefetch_related("completed_person").prefetch_related("troubles")

    def __unicode__(self):
        return str(self.db_uuid)

    class Meta:
        verbose_name = _("工单")
        verbose_name_plural = verbose_name

    def who_can_handle(self):
        return self.department.area.responsible_person.all()

    def working_days(self):
        from_date = self.scheduled_time
        to_date = timezone.datetime.now()
        from_weekday = from_date.weekday()
        to_weekday = to_date.weekday()
        # If start date is after Friday, modify it to Monday
        if from_weekday > 5:
            from_weekday = 0
        day_diff = to_weekday - from_weekday
        whole_weeks = ((to_date - from_date).days - day_diff) / 7
        workdays_in_whole_weeks = whole_weeks * 5
        beginning_end_correction = min(day_diff, 5) - (max(to_date.weekday() - 4, 0) % 5)
        working_days = workdays_in_whole_weeks + beginning_end_correction
        return working_days

    def urgency(self):
        return float(self.working_days()) + self.level

    def transfer_attr(self):
        for trouble in self.troubles.all():
            self.relevant_business.add(*trouble.relevant_business.all())
            self.relevant_equipment.add(*trouble.relevant_equipment.all())
            if trouble.need_completed_by_admin:
                self.need_completed_by_admin = True
            if trouble.responsible_person:
                self.responsible_person = trouble.responsible_person
        self.save()


class Project(CommonModel):
    title = models.CharField(max_length=127, verbose_name=_("标题"))
    detail = models.TextField(verbose_name=_("详细信息"), blank=True, null=True, help_text=_("任何其他重要信息"))
    level = models.FloatField(default=0.0, verbose_name=_("级别"), db_index=True, help_text=_("0-1普通，2-3急，4+特级"))

    start_time = models.DateTimeField(auto_now_add=True, verbose_name=_("登记时间"))
    creator = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("创建者"), related_name="created_project_event")

    tag = models.ManyToManyField(Tag, verbose_name=_("标签"), related_name="project", blank=True, limit_choices_to={'db_active': True},
                                 help_text=_("选择项目或特殊事件，默认留空即可"), )
    relevant_business = models.ManyToManyField(BusinessSystem, verbose_name=_("涉及系统"), related_name="relevant_project", blank=True,
                                               help_text=_('涉及的业务系统，没有请留空'))
    relevant_equipment = models.ManyToManyField(EquipmentModel, verbose_name=_("涉及硬件"), related_name="relevant_project", blank=True,
                                                help_text=_('涉及的硬件设备类型，请尽量准确，没有请留空'))

    completed = models.BooleanField(default=False, verbose_name=_("是否已完成"))
    completed_time = models.DateTimeField(verbose_name=_("完成事件"), null=True, blank=True)
    scheduled_time = models.DateTimeField(default=timezone.now, verbose_name=_("计划开始日期"), help_text=_("默认为当前时间立即开始"), db_index=True)

    def complete_count(self):
        return self.events.filter(completed=True).count()

    def incomplete_count(self):
        return self.events.filter(completed=False).count()

    class Meta:
        verbose_name = _("项目")
        verbose_name_plural = verbose_name

    @staticmethod
    def related_objects():
        return Project.objects.prefetch_related("creator").prefetch_related("relevant_business").prefetch_related("relevant_equipment")


class ProjectEvent(CommonModel):
    department = models.ForeignKey(Department, verbose_name=_("网点/部门"), related_name="responsible_project_event", limit_choices_to={'db_active': True}, )
    project = models.ForeignKey(Project, verbose_name=_("项目"), related_name="events")
    completed = models.BooleanField(default=False, verbose_name=_("是否已完成"))
    completed_time = models.DateTimeField(verbose_name=_("完成事件"), null=True, blank=True)
    process = JSONField(verbose_name=_("处理信息"), default={"workflow": [], "log": []}, editable=False)
    level = models.FloatField(default=0.0, verbose_name=_("级别"), db_index=True, help_text=_("0-1普通，2-3急，4+特级"))
    completed_person = models.ForeignKey(SupportTicketSystemUser, verbose_name=_("完成人"), related_name="completed_project_event", blank=True, null=True)

    @staticmethod
    def related_objects():
        return ProjectEvent.objects.prefetch_related("department").prefetch_related("project").prefetch_related("completed_person").prefetch_related(
            "project__creator").prefetch_related("project__tag").prefetch_related("project__relevant_business").prefetch_related("project__relevant_equipment")

    class Meta:
        verbose_name = _("项目事件")
        verbose_name_plural = verbose_name

    def who_can_handle(self):
        return self.department.area.responsible_person.all()


class TicketFile(DownloadModel):
    save_path = 'ticket'
    ticket = models.ForeignKey(to=Ticket, related_name="files")

    class Meta:
        verbose_name = _("工单附件")
        verbose_name_plural = verbose_name


class ProjectFile(DownloadModel):
    save_path = 'project'
    project = models.ForeignKey(to=Project, related_name="files")

    class Meta:
        verbose_name = _("项目附件")
        verbose_name_plural = verbose_name


class ProjectEventFile(DownloadModel):
    save_path = 'project_event'
    project_event = models.ForeignKey(to=ProjectEvent, related_name="files")

    class Meta:
        verbose_name = _("项目事件附件")
        verbose_name_plural = verbose_name
