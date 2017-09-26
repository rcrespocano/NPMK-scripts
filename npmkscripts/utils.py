# -*- coding: utf-8 -*-
"""Utilities module."""

import sys
import datetime


def check_python_version():
    if sys.version_info[0] < 3:
        raise TypeError('This program must be executed with Python 3')


def get_datetime():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
