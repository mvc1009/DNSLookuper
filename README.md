# DNSLookuper
DNSLookuper is a python tool to resolve DNS querys.

>This tool is made for educational purpose!  A bad usage of this tool is not allowed...

<p align="center">
<img src="src/banner_dnslookuper.png">
</p>

## Description &  Purpose
Once obtain a list of subdomains, for a Red Team assessment is useful to discover which subdomain is associated to which host.

Reconnaissance is one of the most important part in a Red Team assessment, so this tool helps you to "traduce" or resolve all DNS queries in an automatic way. Also DNSLookuper provides you the opportunity to export the result data in `json` or `csv` fileformat.

DNSLookuper uses `dnspython`

<p align="center">
<img src="https://media.giphy.com/media/Zdl1PYZw4kz1dSuP61/giphy.gif">
</p>

## Help
```
usage: dnslookuper.py [-h] [-v] [-c] [-d DOMAIN | -D LIST] [-s SERVER]
                      [-o OUTPUT] [-f {csv,json}] [-oA OUTPUTALLFORMATS]

DNSLookuper is used for resolve DNS Queries. Example: $ python3 dnslookuper.py
-D example.txt -o example_output --format json -v -c

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Turn verbose output on
  -c, --color           Colorize DNSLookup output
  -d DOMAIN, --domain DOMAIN
                        Target domain
  -D LIST, --list-domains LIST
                        List of target domains
  -s SERVER, --server SERVER
                        DNS server to query
  -o OUTPUT, --output OUTPUT
                        Export results to a file
  -f {csv,json}, --format {csv,json}
                        Fileformat to export results
  -oA OUTPUTALLFORMATS, --output-all-formats OUTPUTALLFORMATS
                        Export results with all formats (csv and json)


```

## Requirements

Phython 3.7 or higher is needed. Some python packages are needed such us `dnspython` or `argparse`.

All required packages are inside `requierements.txt`

## Installation

1. Download my repo:

`$ git clone https://github.com/mvc1009/DNSLookuper.git`

2. Install the dependencies:

`$ pip install -r requirements.txt`

3. Use:

`$ python3 dnslookuper.py -D example.txt -o example_output --format json -v -c`



