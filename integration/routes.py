#!/usr/bin/env python
# -*- coding: utf-8 -*-
# routes.py

from integration import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'ASDF'
