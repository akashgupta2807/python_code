#! /usr/bin/env python3

import subprocess

svc = "sshd"

service_check = subprocess.call(['ps','-C',svc])

if service_check == 0:
    print('Service running')
else:
    print('Service not running')

