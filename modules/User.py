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

import sys
from common import *
from winreg import *

def main(reg_key):
	username=putty_read_value(reg_key, "UserName")
	if username:
		print("\tUser " + username);