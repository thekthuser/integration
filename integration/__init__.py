#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __init__.py

from flask import Flask
from flask.ext.uploads import UploadSet, IMAGES 
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

app.config.from_object('dev_settings')
images = UploadSet('images', IMAGES)
csrf = CsrfProtect(app)

import integration.routes
