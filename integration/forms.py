#!/usr/bin/env python                                                                                             
# -*- coding: utf-8 -*-                                                                                           
# forms.py                                                                                                        

from flask.ext.wtf import Form                                                                                    
from wtforms import validators                                                                                    
from flask_wtf.file import FileField, FileAllowed                                                                 
from integration import images                                                                                

class UploadImageForm(Form):                                                                                      
    image = FileField('Upload Image', [FileAllowed(images)])
