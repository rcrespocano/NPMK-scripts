# -*- coding: utf-8 -*-
"""Utilities module."""

import sys


def check_python_version():
    if sys.version_info[0] < 3:
        raise TypeError('This program must be executed with Python 3')
