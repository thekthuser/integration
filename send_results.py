#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#send_results.py

import sys
import os
import smtplib
import secrets


last_test_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/last_test.txt'
with open(last_test_path, 'r') as testfile:
    status = testfile.readlines()[-1].decode()
testfile.close()

if "OK" in status:
    result = "passed"
else:
    result = "failed"
body = "Your last commit " + result + "."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(secrets.username, secrets.password)
server.sendmail(secrets.username, secrets.recipient, body)
server.quit()
