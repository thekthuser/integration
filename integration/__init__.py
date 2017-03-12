#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __init__.py

from flask import Flask

app = Flask(__name__)

app.config.from_object('dev_settings')
import integration.routes
