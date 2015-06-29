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
if not has_admin():
	print("User does not have admin privileges!")
	print("Please run as an admin.")
	print("on Windows, this right click cmd.exe and select \"run as admin\"")
	print("on Mac or Linux, this means run with sudo")
	raise PermissionError("User does not have root/admin privileges")

if platform.system() == "Linux":
elif platform.system() == "Windows":
	pass
elif platform.system() == "Darwin":
	pass
else:
	raise RuntimeError("System not supported by script")
