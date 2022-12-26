# PuTTY2OpenSSH

PuTTY2OpenSSH exports PuTTY sessions from the Windows registry to OpenSSH config format. 

This tool helps to migrate large number of saved PuTTY configuration in bulk.

## Install

The script is written in python. You need a python3 to run it.

## Example usage

	python putty2openssh.py > .ssh/config
	
## Limitations

Only PuTTY SSH sessions are supported. Other protocols are ignored. This is not going to change as the output format is OpenSSH config file.

Not all PuTTY/OpenSSH options are supported. Check the modules directory for details. Feel free to contribute by adding support to other options. PRs are welcome.

### Supported configuration directives

- HostName
- Port
- User
- ProxyJump
- LocalForward
- RemoteForward
- DynamicForward
- ForwardAgent
- X11Forward yes/no

