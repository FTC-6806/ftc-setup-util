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

def run_command(cmd):
	subprocess.check_call(cmd, shell=True, stdin=None, stdout=open(os.devnull, 'wb'))

def apt_install_package(package_name):
	print("> apt-get install {pack}".format(pack=package_name))
	run_command('apt-get install -y {pack}'.format(pack=package_name))

def add_apt_repository(repo):
	print("> add-apt-repository {repo}".format(repo=repo))
	run_command('add-apt-repository -y {repo}'.format(repo=repo))

def apt_update():
	print("> apt-get update")
	run_command("apt-get update")

def brew_install(package_name):
	print("> brew install {pack}".format(pack=package_name))
	run_command('brew install {pack}'.format(pack=package_name))

def brew_cask_install(cask_name):
	print("> brew cask install {pack}".format(pack=cask_name))
	run_command('brew cask install {pack}'.format(pack=cask_name))

print("=======<FTC Java Autoconfigurator>=======")
print("= written by @archimedespi of Team 6806 =")
if not has_admin():
	print("User does not have admin privileges!")
	print("Please run as an admin.")
	print("on Windows, this right click cmd.exe and select \"run as admin\"")
	print("on Mac or Linux, this means run with sudo")
	raise PermissionError("User does not have root/admin privileges")

if platform.system() == "Linux":
	if platform.dist()[0] == "Ubuntu":
		# make sure we have add-apt-repository
		apt_install_package("python-software-properties software-properties-common")
		# grab oracle java ppa
		add_apt_repository("ppa:webupd8team/java")
		# pull the new repo lists
		apt_update()
		# preaccept the Oracle license
		run_command("echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections")
		run_command("echo oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections")
		# install Java 8
		apt_install_package("oracle-java8-installer")
		apt_install_package("oracle-java8-set-default")

elif platform.system() == "Darwin":
	brew_install("caskroom/cask/brew-cask")
	brew_install("git")
	brew_cask_install("java")
	brew_cask_install("android-studio")
else:
	raise RuntimeError("System not supported by script")

print("Done!")