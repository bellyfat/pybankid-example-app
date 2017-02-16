#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`views.py`
==================

.. module:: views.py
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2014-09-09, 15:08

"""

from __future__ import division
from __future__ import print_function
#from __future__ import unicode_literals
from __future__ import absolute_import

import json
import datetime

from flask import render_template

from bankidexampleapp import app
from bankidexampleapp.forms import BankIdSignForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BankIdSignForm()
    return render_template('form_page.html',
                           title='BankIdExampleApp Start Page',
                           form=form)


@app.route('/collect_page', methods=['POST'])
def collect_page():
    form = BankIdSignForm()

    # Make no form.validate_on_submit.
    doc = json.loads(form.collect_results.data)
    doc['personalNumber'] = form.personal_number.data
    doc['orderRef'] = form.order_ref.data
    doc['userInfo']['notAfter'] = datetime.datetime.strptime(
        doc['userInfo']['notAfter'], '%a, %d %b %Y %H:%M:%S GMT')
    doc['userInfo']['notBefore'] = datetime.datetime.strptime(
        doc['userInfo']['notBefore'], '%a, %d %b %Y %H:%M:%S GMT')

    return render_template('results_page.html',
                           title='BankIdExampleApp Collect Page',
                           results=doc)


@app.route('/error')
def error_page():
    return render_template('info_page.html',
                           title='BankIdExampleApp Error Page',
                           info_text="No order reference or personal number!")
