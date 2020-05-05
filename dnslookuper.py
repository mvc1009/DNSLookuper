#!/bin/python3

#
# _____  _______ _______ _____                __                
#|     \|    |  |     __|     |_.-----.-----.|  |--.--.--.-----.-----.----.
#|  --  |       |__     |       |  _  |  _  ||    <|  |  |  _  |  -__|   _|
#|_____/|__|____|_______|_______|_____|_____||__|__|_____|   __|_____|__|  

#                                                        |__|  
#
#


#Imports
import sys, os
try:
	import struct
except:
	print('[!] struct is not installed. Try "pip install struct"')
	sys.exit(0)
try:
	import argparse
except:
	print('[!] argparse is not installed. Try "pip install argparse"')
	sys.exit(0)
try:
	import socket
except:
	print('[!] socket is not installed. Try "pip install socket"')


#COLOR CODES
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'


# Display DNSLookuper Banner
def banner():
	print('\n\n')
	print(' _____  _______ _______ _____                __                ')
	print('|     \|    |  |     __|     |_.-----.-----.|  |--.--.--.-----.-----.----.')
	print('|  --  |       |__     |       |  _  |  _  ||    <|  |  |  _  |  -__|   _|')
	print('|_____/|__|____|_______|_______|_____|_____||__|__|_____|   __|_____|__|  ')
	print('                                                        |__|  ')
	print("\t\t\t\t\t\t\t\tVersion 0.1")
	print("\t\t\t\t\t\t\t\tBy: @mvc1009")
	print('\n\n')

def dnsquery(domain):
	d=''
	for a in domain.split('.'):
		s = struct.Struct('!b'+str(len(a))+'s')
		packed_data = s.pack(len(a),a.encode('utf-8')).decode('utf-8')
		d = d + packed_data
	l1 = "\x41\x41"
	l2 = "\x01\x00"
	l3 = "\x00\x01"
	l4 = "\x00\x00"
	l5 = "\x00\x00"
	l6 = "\x00\x00"
	header = l1 +l2 + l3 + l4 + l5 + l6
	q = d + "\x00\x00\x01\x00\x01"
	m = header + q
	print(m)
	print(m.encode())
	return m

def main():
	banner()
	
	#parser = argparse.ArgumentParser(description='DNSLookuper is used for resolve DNS Queries.\n\t\t\n Example: $ python3 dnslookuper.py ', epilog='Thanks for using me!')

	#global args
	#args =  parser.parse_args()

	dnsquery('www.google.es')


try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")
