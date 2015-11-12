#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_object('bankidexampleapp.config')

from bankidexampleapp import views
from bankidexampleapp import filters
