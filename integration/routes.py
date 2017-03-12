#!/usr/bin/env python
# -*- coding: utf-8 -*-
# routes.py

from flask import render_template, request
from integration import app
from integration.forms import UploadImageForm
from flask import Response

def allowed_file(filename):                                                                          
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in \
    app.config['UPLOADED_IMAGES_ALLOW']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadImageForm(request.form)                                                             
    if request.method == 'POST':
	upload = request.files['image']
	if upload and allowed_file(upload.filename):
	    return Response(upload.read(), mimetype='image')
        else:
            return render_template('index.html', form=form, error=True)
    else:
        return render_template('index.html', form=form, error=False)
