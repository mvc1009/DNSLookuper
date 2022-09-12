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
	import json
except:
	print('[!] json is not installed. Try "pip install json"')
	sys.exit(0)
try:
	import csv
except:
	print('[!] cvs is not installed. Try "pip install csv"')

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
		
def readFile():
	try:
		with open(args.list, 'r') as f:
			queries = f.read().split()
		if args.verbose:
			print('\n')
			if args.color:
				print(RED + '[+] List of Domains to resolve: ' + RESET + args.list )
			else:
				print('[+] List of Domains to resolve: ' + args.list)
		return queries
	except:
		if args.color:
			print(RED + '[!] File not found' + RESET)
		else:
			print('[!] File not found"')
		lsys.exit(0)
def exportResults(results, fileformat):
	# CSV fileformat

	filename = str(args.output) + '.' + str(fileformat)
	if args.verbose:
		if args.color:
			print(RED + '[+] Exporting results to: ' + RESET + filename)
		else:
			print('[+] Exporting results to: ' + filename)
	if fileformat == 'csv':
		with open(filename, mode='w+') as csv_file:
			fieldnames = ['DNS', 'IP']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for i in results:
				writer.writerow(i)
	# JSON fileformat
	elif fileformat == 'json':
		with open(filename, mode='w+') as json_file:
			json.dump(results, json_file)
	
def main():
	
	# Parsing arguments
	parser = argparse.ArgumentParser(description='DNSLookuper is used for resolve DNS Queries.\n\t\t\n Example: $ python3 dnslookuper.py -D example.txt -o example_output --format json -v -c ', epilog='Thanks for using me!')
	parser.add_argument('-v', '--verbose', action='store_true', help='Turn verbose output on')
	parser.add_argument('-c', '--color', action='store_true', help='Colorize DNSLookup output')
	group1 = parser.add_mutually_exclusive_group()
	group1.add_argument('-d', '--domain', action='store', dest='domain', help='Target domain', type=str)
	group1.add_argument('-D', '--list-domains', action='store', dest='list', help='List of target domains', type=str)
	parser.add_argument('-s', '--server', action='store', dest='server', help='DNS server to query', default='8.8.8.8', type=str)
	group2 = parser.add_mutually_exclusive_group()	
	group2.add_argument('-o', '--output', action='store', dest='output', help='Export results to a file', type=str)
	parser.add_argument('-f', '--format', action='store', dest='format', help='Fileformat to export results', choices = ['csv' ,'json'], default = 'csv', type=str)
	group2.add_argument('-oA', '--output-all-formats', action='store', dest='outputallformats', help='Export results with all formats (csv and json)', type=str)
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
		results = list()
		queries = list()
		if args.domain:
			queries.append(args.domain)
		elif args.list:
			queries = readFile()

		# Making DNS resolutions for all queries
		for query in queries:
			response, answer = dnsQuery(query)
			if response != 'None':
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
				results.append({'DNS':query, 'IP':response})
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
		
		# Export RESULTS
		if args.output:
			exportResults(results, args.format)
		elif args.outputallformats:
			exportResults(results, 'cvs')
			exportResults(results, 'json')

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
