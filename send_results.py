#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#send_results.py

import sys
import smtplib


with open('last_test.txt', 'r') as testfile:
    status = testfile.readlines()[-1].decode()
testfile.close()
with open('secrets.txt', 'r') as secrets:
    lines = secrets.readlines()
    username = lines[1]
    password = lines[2]
    recipient = lines[3]
secrets.close()

if status == "OK":
    result = "passed"
else:
    result = "failed"
body = "Your last commit " + result + "."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username, recipient, body)
server.quit()
