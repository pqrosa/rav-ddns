#!/usr/bin/env python

import socket
import requests

DynDNS_username = '<YOUR DYNDNS USERNAME>'
DynDNS_password = '<YOUR DYNDNS PASSWORD>'

DynDNS_hostname = '<YOUR DYNDNS HOSTNAME>'
OtherDNS_hostname = '<THE THIRD PARTY DDNS HOSTNAME>'

DynDNS_IP = socket.gethostbyname(DynDNS_hostname)
OtherDNS_IP = socket.gethostbyname(OtherDNS_hostname)

if (DynDNS_IP != OtherDNS_IP):
	r = requests.get('http://' + DynDNS_username + ':' + DynDNS_password + '@members.dyndns.org/nic/update?hostname=' + DynDNS_hostname + '&myip=' + OtherDNS_IP)
