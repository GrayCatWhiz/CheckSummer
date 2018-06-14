#!/usr/bin/env python
import argparse
import sys
import hashlib

try:
	from colorama import Fore as F,Back as B,Style as S
except ImportError:
	print '[!] Err Colorama modules not installed, try installing using `pip install colorama`.'

def banner():
	print F.LIGHTYELLOW_EX + """
\t      _               _        _            _____  _____  ____ 
\t     | |             | |      | |          / __  \|  ___|/ ___|
\t  ___| |__   ___  ___| | _____| |__   __ _ `' / /'|___ \/ /___ 
\t / __| '_ \ / _ \/ __| |/ / __| '_ \ / _` |  / /      \ \ ___ \
 
\t| (__| | | |  __/ (__|   <\__ \ | | | (_| |./ /___/\__/ / \_/ |
\t \___|_| |_|\___|\___|_|\_\___/_| |_|\__,_|\_____/\____/\_____/v1.0
 
	    Checksum generator tool by GrayCatWhiz
	    
	    usage: checksummer.py [OPTIONS] -f filename
	    
	    OPTIONS:
	    -h    help    show this help message
	    -f    filename    filename to be use on checksum
	""" + F.RESET
def parser_error(Errmsg):
	banner() 
	print F.RED + S.BRIGHT+ '[!] Err: ' + Errmsg + S.RESET_ALL
def parse_args():
	parser = argparse.ArgumentParser(description='Stupid-Simple checksum tool.')
	parser.error = parser_error 
	parser.add_argument('-f','--filename',help='File to be checksum',required=True)
	return parser.parse_args()

def sha256_sum(filename,block_size=65536):
	sha256 = hashlib.sha256()
	try:
		with open(filename, 'rb') as f:
			for block in iter(lambda: f.read(block_size), b''):
				sha256.update(block)
		print F.GREEN + sha256.hexdigest() + F.RESET		
	except IOError:
		print F.RED + S.BRIGHT+ '[!] There\'s no such file : ' + filename
def main():
	args = parse_args()
	filename = args.filename
	if(filename != None):
		sha256_sum(filename)
		
if __name__ == '__main__':
	main()
