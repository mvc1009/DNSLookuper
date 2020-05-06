#!/bin/python3

#
#
#	This tools is made for educational purpose!
#	A bad usage of this tool is not allowed...
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
	import dns.resolver
except:
	print('[!] dnspython is not installed. Try "pip install dnspython"')
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
	print(' _____  _______ _______ _____                __                	')
	print('|     \|    |  |     __|     |_.-----.-----.|  |--.--.--.-----.-----.----.')
	print('|  --  |       |__     |       |  _  |  _  ||    <|  |  |  _  |  -__|   _|')
	print('|_____/|__|____|_______|_______|_____|_____||__|__|_____|   __|_____|__|  ')
	print('                                                        |__|  ')
	print("\t\t\t\t\t\t\t\tVersion 0.1")
	print("\t\t\t\t\t\t\t\tBy: @mvc1009")

	print('\n\n')

def dnsQuery(query):
	my_resolver = dns.resolver.Resolver()
	my_resolver.nameservers = [args.server]
	try:
		answer = my_resolver.query(query)
		for data in answer:
			return str(data), str(answer)
	except:
		return 'None', 'None'
		
def readFile(file):
	try:
		f = open(file, 'r')
		queries = f.read().split()
		f.close()
		if args.verbose:
			print('\n')
			if args.color:
				print(BLUE + '[+] List of Domains to resolve: ' + RESET + file )
			else:
				print('[+] List of Domains to resolve: ' + file)
		return queries
	except:
		if args.color:
			print(RED + '[!] File not found' + RESET)
		else:
			print('[!] File not found"')
	

def main():

	# Parsing arguments
	parser = argparse.ArgumentParser(description='DNSLookuper is used for resolve DNS Queries.\n\t\t\n Example: $ python3 dnslookuper.py ', epilog='Thanks for using me!')
	
	parser.add_argument('-v', '--verbose', action='store_true', help='Turn verbose output on')
	parser.add_argument('-c', '--color', action='store_true', help='Colorize DNSLookup output')
	group2 = parser.add_mutually_exclusive_group()
	group2.add_argument('-d', '--domain', action='store', dest='domain', help='Target domain', type=str)
	group2.add_argument('-D', '--list-domains', action='store', dest='list', help='List of target domains', type=str)
	parser.add_argument('-s', '--server', action='store', dest='server', help='DNS server to query', default='8.8.8.8', type=str)
	parser.add_argument('-o', '--output', action='store', dest='file', help='Write results to a file', type=str)
	parser.add_argument('-f', '--format', action='store', dest='format', help='Fileformat to export results', choices = ['csv' ,'json'], default = 'csv' type=str)

	
	global args
	args =  parser.parse_args()

	#Presentation
	banner()

	#Usage
	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(0)

	# Initial message
	if args.color:
		print(RED + '[!] Start resolving DNS queries' + RESET)
	else:
		print('[!] Start resolving DNS queries')

	# DNS Server message
	if args.verbose:
		if args.color:
			print(BLUE + '[+] DNS Server' + RESET)
		else:
			print('[+] DNS Server')
		print('\t' + args.server)

	# DOMAIN / SUBDOMAINS
	if args.domain or args.list:
		# Defining a list with all the queries
		queries = list()
		if args.domain:
			queries.append()
		elif args.list:
			queries = readFile(args.list)

		# Making DNS resolutions for all queries
		for query in queries:
			response, answer = dnsQuery(query)
			if response is not 'None':
				if args.verbose:
					if args.color:
						print(BLUE + '[+] Query to resolve: ' + YELLOW + query + RESET)
						print('\t' + str(answer))
						print('\t' + YELLOW + query + RESET + ' -> ' + GREEN + response + RESET)
					else:
						print('[+] Query to resolve: ' + query)
						print('\t' + str(answer))
						print('\t' + query + ' -> ' + response)
				else:
					if args.color:
						print(YELLOW + query + RESET + ' -> ' + GREEN + response + RESET)		
					else:
						print(query + ' -> ' + response)
			else:
				if args.verbose:
					if args.color:
						print(BLUE + '[+] Query to resolve: ' + YELLOW + query + RESET)
					else:
						print('[+] Query to resolve: ' + query)
					print('\t No response for this query')
				else:
					if args.color:
						print(YELLOW + query + RESET + ' -> ' + GREEN + response + RESET)		
					else:
						print(query + ' -> ' + response)


	else:
		parser.print_help()
		# ERROR MESSAGE, need a entry or a list of entries
		if args.color:
			print(RED + '[!] Introduce a domain (-d, --domain) or a list of domains (-D, --list-domains)' + RESET)
		else:
			print('[!] Introduce a domain (-d, --domain) or a list of domains (-D, --list-domains)')
	




try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")
