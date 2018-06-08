#!/usr/bin/python

import hashlib
import os

# Author: graycatwhiz
# Description: stupid-simple tool for checksum
# Date Created: June 6, 2018
# Last Updated: June 8, 2018
# Script Name: checksummer.py

# June 8, 2018 - Added functions for gui-checksummer.py 

# help.txt - hello world!\n - 4396844b7d183a6f64e8d41a0f03b543
# help.txt - hello world! - c897d1410af8f2c74fba11b1db511e9e

# Example Path 
# for windows full path : C:\Users\{username}\Documents\help.txt
# for linux or mac full path : /home/{username}/Documents/help.txt


class CheckSummer:
	def __init__(self):
		"""
			Stupid-Simple Check Sum Generator
		"""

		#user = os.getlogin()

		#file = raw_input("input file for checksum: ")

		#if(os.name == 'posix'):
		#	if(file[0] == '~'):
		#		file = '/home/' + user + '/' + file[1:]

		#try:
		#	file = open(file,'r')
		#except IOError:
		#	print "[!] There's no such file or directory! "
		#	quit()

		#plain = file.read()

		#print 'MD5 :' , self.getMD5(pl)
		#print 'SHA1 :' , self.getSHA1(pl)
		#print 'SHA256 :' , self.getSHA256(pl)
		#print 'SHA512 :' , self.getSHA512(pl)
	def getMD5(self,plaintext):
		m = hashlib.md5()
		m.update(plaintext)
		return m.hexdigest()

	def getSHA1(self,plaintext):
		s1 = hashlib.sha1()
		s1.update(plaintext)
		return s1.hexdigest()

	def getSHA256(self,plaintext):
		s256 = hashlib.sha256()
		s256.update(plaintext)
		return s256.hexdigest()

	def getSHA512(self,plaintext):
		s512 = hashlib.sha512()
		s512.update(plaintext)
		return s512.hexdigest()


# usage : Uncomment
# checksummer = CheckSummer()
# checksummer

