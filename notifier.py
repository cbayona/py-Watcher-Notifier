#!/usr/bin/env python

import smtplib
import os
import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


if os.path.isfile(config.Watcher.log_filename) == False:
    exit(1)

if os.stat(config.Watcher.log_filename).st_size == 0:
    exit(1)

file = open(config.Watcher.log_filename, 'r+')
TEXT = file.read()

# Prepare the message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (config.Notifier.sender, ", ".join(config.Notifier.receivers), config.Notifier.subject, TEXT)

try:

    server = smtplib.SMTP(config.Notifier.host, config.Notifier.port)
    server.ehlo()
    server.starttls()
    server.login(config.Notifier.username, config.Notifier.password)
    server.sendmail(config.Notifier.sender, config.Notifier.receivers, message)
    server.close()

    print "Successfully sent email"

    file.seek(0)
    file.truncate()
    file.close()
except:
   print "Error: unable to send email"