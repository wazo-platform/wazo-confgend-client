#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='xivo-confgend-client',
    version='0.1',
    description='XIVO Configurations Generator client',
    author='Avencall',
    author_email='xivo-dev@lists.proformatique.com',
    url='http://www.xivo.io/',
    license='GPLv3',
    scripts=['bin/xivo-confgen'],
    data_files=[('/etc/xivo-confgend-client', ['etc/xivo-confgend-client/config.conf'])],
)
