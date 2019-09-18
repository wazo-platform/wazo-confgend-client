#!/usr/bin/env python3
# Copyright 2016-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup

setup(
    name='wazo-confgend-client',
    version='0.1',
    description='wazo-confgend CLI client',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo-platform.org',
    license='GPLv3',
    scripts=['bin/wazo-confgen'],
)
