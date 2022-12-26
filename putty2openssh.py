# PuTTy2OpenSSH
#
# This program exports PuTTY sessions from the Windows registry to OpenSSH 
# configuration format.
#
# Copyright (C) 2022  Schedek, s.r.o.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Author: Pavel Sedek <pavel.sedek@schedek.com>
# Website: https://schedek.com

PUTTY2OPENSSH_VERSION="1.0-SNAPSHOT";

import sys
import os
#from modules import HostName

from common import *
from winreg import *

# List of modules, one module generates a line in openssh config
openssh_section_modules = ["User","HostName","Port","ProxyJump","ForwardAgent","X11Forward","PortForwardings"]
		
# Test for session minimal requirements to be placed to output
def putty_is_session_valid(k):
	protocol = putty_read_value(k, "Protocol")
	if protocol != "ssh":
		return "Not a SSH session, protocol ["+protocol+"] ignored."
		
	if not putty_read_value(k, "HostName"):
		return "Host name not found"
	return True

# Read all settings from windows registry, vaidate and process one-by-one
def putty_process_settings():
	reg = ConnectRegistry(None, HKEY_CURRENT_USER)
	key = OpenKey(reg, r"Software\SimonTatham\Putty\Sessions")
	i = 0
	e = 0
	try:
		while True:
			sub_key_name = EnumKey(key, i)
			sub_key = OpenKey(key, sub_key_name)
			i+=1
			
			session_valid = putty_is_session_valid(sub_key)
			if not session_valid == True:
				print(sub_key_name+": "+session_valid, file=sys.stderr)
				e+=1
				continue;
			
			print("HOST "+sub_key_name)
			
			for mod in openssh_section_modules:
				__import__('modules.'+mod,fromlist=["*"]).main(sub_key)
			
			print("")
			
			
	except OSError:
		pass
		
	print(""+str(i-e)+"/"+str(i)+" sessions exported successfully, "+str(e)+" sessions failed to export ")

def print_help():
	print("Usage: python "+__file__+" > .ssh/config");
	
# Possible support for some command-line attributes...
def main():
	args = sys.argv[1:]
	if len(args)==0:
		putty_process_settings()
	elif len(args)==1:
		if args[0]=="--version":
			print("PuTTY2OpenSSH "+PUTTY2OPENSSH_VERSION)
			print("Copyright (C) 2022 Schedek, s.r.o.")
			print("License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.")
			print("This is free software: you are free to change and redistribute it.")
			print("There is NO WARRANTY, to the extent permitted by law.")
			print("")
			print("Written by Pavel Sedek.")
		else:
			print_help()
	else:
		print_help()

if __name__ == '__main__':
	main()