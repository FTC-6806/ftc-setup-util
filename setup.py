#!/usr/bin/env python

import os
import sys
import platform
import subprocess

def has_admin():
    if platform.system() == 'Windows':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
        except:
            return False
        else:
            return True
    else:
    	if os.geteuid() == 0:
    		return True

def apt_install_package(package_name):
	print("> apt-get install {pack}...".format(pack=package_name))
	proc = subprocess.Popen('apt-get install -y {pack}'.format(pack=package_name), shell=True, stdin=None,
			stdout=subprocess.STDOUT, stderr=subprocess.STDOUT)
	proc.wait();
	print("done.")

print("=======<FTC Java Autoconfigurator>=======")
print("= written by @archimedespi of Team 6806 =")
