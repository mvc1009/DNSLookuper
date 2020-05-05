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
	#print('\n')
	print("\t\t\t\t\t\t\t\tVersion 0.1")
	print("\t\t\t\t\t\t\t\tBy: @mvc1009")
	print('\n\n')

def main():
	banner()
	
	parser = argparse.ArgumentParser(description='DNSLookuper is used for resolve DNS Queries.\n\t\t\n Example: $ python3 dnslookuper.py ', epilog='Thanks for using me!')

	global args
	args =  parser.parse_args()

try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")
