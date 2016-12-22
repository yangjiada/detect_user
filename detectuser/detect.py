#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 10:40:09
# @Author  : Jan Yang
# @Software : Sublime Text

# import requests

from phone import Phone
from email import Email


class Account:
    def __init__(self, phone, email, user):
        self.phone = phone
        self.email = email
        self.user = user
