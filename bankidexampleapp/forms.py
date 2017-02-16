#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`forms`
==================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2014-09-09, 15:48

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class BankIdSignForm(FlaskForm):
    personal_number = StringField(label='Personnummer på formen YYYYMMDDXXXX', validators=[DataRequired(), ])
    order_ref = StringField(label='Order Reference (orderRef)',)
    collect_results = StringField(label="Collect Progress Response")
