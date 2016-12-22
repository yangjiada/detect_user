#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 10:36:16
# @Author  : Jan Yang
# @Software : Sublime Text


# import requests

class Phone:
    """Create a mobile class"""
    def __init__(self, number):
        self.number = number

    def is_phone(self):
        if self.number<10 and self.number>11:
            return False
        else:
            return True

    def info(self):
        print self.number


if __name__ == '__main__':
    pass
