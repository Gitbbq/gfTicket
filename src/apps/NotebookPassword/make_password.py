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
import string
import hashlib

# Core Django imports

# Third-party app imports


# Imports from your apps


CryptKey = "GDBBJ@123"


def only_upper_char_and_num(s):
    s = s.upper()
    fomart = string.ascii_uppercase + string.digits
    for c in s:
        if not c in fomart:
            s = s.replace(c, '')
    return s


def make_upper_eight_md5(s):
    s = hashlib.md5((s.encode()))
    s = s.hexdigest()
    s = s[0:8]
    return s.upper()


def make_notebook_password(sn, times=1):
    sn = only_upper_char_and_num(sn)
    sn_p = sn + CryptKey + str(times)
    pw = make_upper_eight_md5(sn_p)
    return pw


def make_password_list(sn, times=4):
    l = []
    for i in list(range(1, times)):
        l.append(make_notebook_password(sn, times=i))
    return l
