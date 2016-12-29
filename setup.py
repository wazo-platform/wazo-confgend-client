#!/usr/bin/env python3

from setuptools import setup

setup(
    name='xivo-confgend-client',
    version='0.1',
    description='XIVO Configurations Generator client',
    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',
    url='http://wazo.community',
    license='GPLv3',
    scripts=['bin/xivo-confgen'],
)
