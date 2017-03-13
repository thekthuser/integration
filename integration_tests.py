#!/usr/bin/env python                                                                                
# -*- encoding: utf-8 -*-                                                                            
#integration_tests.py

import os
import integration
import unittest
from StringIO import StringIO

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
	integration.app.config['TESTING'] = True
	self.app = integration.app.test_client()
	integration.app.config['WTF_CSRF_METHODS'] = []

    def tearDown(self):
	pass

    def test_image(self):
	with open('./integration/static/default_kitty.jpg', 'r') as image:
	    imgString = StringIO(image.read())
	response = self.app.post('/', data = {'image': (imgString, os.path.basename(image.name))})
	self.assertEquals(response.status, '200 OK')
	self.assertEquals(response.mimetype, 'image')
    
    def test_not_image(self):
	with open('./integration/static/testing.txt', 'r') as text:
	    imgString = StringIO(text.read())
	response = self.app.post('/', data = {'image': (imgString, os.path.basename(text.name))})
	assert 'Uploaded file must be an image.' in response.data
	

if __name__ == '__main__':
    unittest.main()
