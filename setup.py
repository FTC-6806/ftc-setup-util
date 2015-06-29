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

