#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`filters.py`
==================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2014-09-11, 15:37

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from bankidexampleapp import app

@app.template_filter('swedate')
def swedate(s):
    return s.strftime("%Y-%m-%d %H:%M:%S")
