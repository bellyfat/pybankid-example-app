#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`forms`
==================

.. module:: forms
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2014-09-09, 15:48

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class BankIdSignForm(Form):
    personal_number = StringField(label='Personnummer på formen YYYYMMDDXXXX', validators=[DataRequired()])
    order_ref = StringField(label='Order Reference (orderRef)',)
    collect_results = StringField(label="Collect Progress Response")
