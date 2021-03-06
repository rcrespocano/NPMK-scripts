# -*- coding: utf-8 -*-
"""Utilities module."""

import sys
import datetime
import os


def check_python_version():
    if sys.version_info[0] < 3:
        raise TypeError('This program must be executed with Python 3')


def get_datetime():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def get_name_from_dataset(dataset_path):
    return os.path.basename(dataset_path)
