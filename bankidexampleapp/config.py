#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`config.py`
==================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2014-09-09, 15:47

"""

import os

CSRF_ENABLED = True
SECRET_KEY = os.environ.get('PYBANKIDEXAMPLE_APP_SECRET',
                            'notverysecretdefaultkey')

PYBANKID_CERT_PATH = os.path.join(os.path.dirname(__file__), 'keys/cert.pem')
PYBANKID_KEY_PATH = os.path.join(os.path.dirname(__file__), 'keys/key.pem')
PYBANKID_TEST_SERVER = True
