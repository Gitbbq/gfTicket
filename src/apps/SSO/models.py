#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports
import logging

from ldap3 import Connection, SUBTREE, ALL_ATTRIBUTES
from ldap3 import NTLM
from ldap3.utils.log import set_library_log_detail_level, EXTENDED

# Core Django imports
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel

logger = logging.getLogger(__name__)
set_library_log_detail_level(EXTENDED)


# Create your models here.

class DomainSetting(CommonModel):
    fqdn = models.CharField(max_length=128, verbose_name=_("(Fully Qualified Domain Name)完全合格域名"), unique=True)
    NetBIOS = models.CharField(max_length=24, verbose_name=_("NetBios name"), unique=True)
    dc_server = models.CharField(max_length=24, verbose_name=_("DC Server Name/IP"), unique=True)
    search_base = models.TextField(verbose_name=_("搜索限定"), default="dc=home,dc=local")
    connect_user = models.CharField(max_length=128, verbose_name=_("连接用户名"))
    connect_pass = models.CharField(max_length=128, verbose_name=_("连接密码"))

    def __unicode__(self):
        return self.NetBIOS

    class Meta:
        verbose_name = _("域")
        verbose_name_plural = verbose_name


class DomainUser(CommonModel):
    user = models.OneToOneField(User, verbose_name=_("对应用户"), related_name="sso_user")
    username = models.CharField(max_length=642, verbose_name=_("username"))
    domain = models.ForeignKey(to=DomainSetting, verbose_name=_("域"))
    cn = models.CharField(max_length=642, verbose_name=_("Name"), null=True, blank=True)
    displayName = models.CharField(max_length=256, verbose_name=_("Display Name"), null=True, blank=True)
    distinguishedName = models.TextField(verbose_name=_("X500 Distinguished Name"), null=True, blank=True)
    givenName = models.CharField(max_length=256, verbose_name=_("First Name"), null=True, blank=True)
    sn = models.CharField(max_length=256, verbose_name=_("Last Name"), null=True, blank=True)
    initials = models.CharField(max_length=256, verbose_name=_("Initials"), null=True, blank=True)
    mail = models.CharField(max_length=256, verbose_name=_("E-Mail Address"), null=True, blank=True)
    userPrincipalName = models.CharField(max_length=256, verbose_name=_("Logon Name"), null=True, blank=True)

    def __unicode__(self):
        return "%s@%s" % (self.username, self.domain.fqdn)

    class Meta:
        verbose_name = _("AD映射用户")
        verbose_name_plural = verbose_name


class ADServer(DomainSetting):
    class Meta:
        proxy = True

    connection = None
    authentication = NTLM

    def test_user_password(self, username, password):
        self.connection = Connection(self.dc_server,
                                     user=r'%s\%s' % (self.fqdn, username),
                                     password=password,
                                     authentication=self.authentication,
                                     read_only=True)
        result = self.connection.bind()
        self.connection.unbind()
        return result

    def connect_to_server(self, read_only=True, check_names=True):
        self.connection = Connection(self.dc_server,
                                     user=r'%s\%s' % (self.fqdn, self.connect_user),
                                     password=self.connect_pass,
                                     authentication=self.authentication,
                                     read_only=read_only,
                                     check_names=check_names)
        return self.connection

    def search_user(self, logon_name):
        if self.connection is None:
            self.connect_to_server()

        self.connection.bind()

        if logon_name is not None:
            search_filter = '(&(samAccountName=' + logon_name + '))'
            self.connection.search(search_base=self.search_base,
                                   search_filter=search_filter,
                                   search_scope=SUBTREE,
                                   attributes=ALL_ATTRIBUTES,
                                   get_operational_attributes=True)
            result = self.connection.entries
        else:
            result = None

        self.connection.unbind()
        return result

    def get_user(self, logon_name):
        try:
            return self.search_user(logon_name=logon_name)[0]
        except IndexError:
            return None
        except TypeError:
            return None

    def close_connect(self):
        if self.connection is not None:
            self.connection.unbind()
        self.connection = None
