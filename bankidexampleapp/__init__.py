#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_pybankid import PyBankID

app = Flask(__name__)
app.config.from_object('bankidexampleapp.config')
bankid = PyBankID(app)
