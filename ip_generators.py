#!/usr/bin/python3
#-*- coding: utf-8 -*-
#ip_generators.py

from bs4 import BeautifulSoup
import requests
import random
import socket
import os, sys
import re

class generator:
	
	def __cinit__(self):
		self.data=None

	#Generate to random ip addresses according to given sample ip address 
	def random_ip(self, ipaddress="192.168.1.7", netmask="255.0.0.0"):
		try:			
			a,b,c,d = ipaddress.split(".")
			
			k = str(random.randint(0, 255))
			l = str(random.randint(0, 255))
			m = str(random.randint(0, 255))
			
			if netmask == "255.255.255.0":
				ip_address = "{0}.{1}.{2}.{3}".format(a, b, c, k)
			elif netmask == "255.255.0.0":
				ip_address = "{0}.{1}.{2}.{3}".format(a, b, k, l)
			elif netmask == "255.0.0.0":
				ip_address = "{0}.{1}.{2}.{3}".format(a, k, l, m)
			else:
				ip_address = False

			return ip_address
		except:
			return False

	#Return the own ip address
	def own_ip(self):
		try:
			hostname = socket.gethostname()
			ip_address = socket.gethostbyname(hostname)

			return ip_address
		except:
			return False

	#Read the Ip addresses from wordlist path
	def read_from_wordlist(self, path):
		ip_list = []
		if os.path.exists(path):
			with open(path, "r") as wordlist:
				dataCaptured = wordlist.readlines()
				for row in dataCaptured:
					try:							
						a, b = row.split("\n")
						ip_list.append(a)
					except:
						pass

			ip_address = random.choice(ip_list)

			return ip_address
		else:
			return False


	# Fetch Actual Ip Addresses From Free Proxy Portals
	def fetch_actual_ips(self):

		try:
			proxy_list = ["https://www.us-proxy.org/", "https://www.sslproxies.org/", "https://free-proxy-list.net/"]
			code = -1
			while code != 200:				
				url = random.choice(proxy_list)
				response = requests.get(url)
				code = response.status_code 

			soup = BeautifulSoup(response.content,"lxml")
			ipList = []
			trs = soup.find("table", attrs={"id":"proxylisttable"}).find("tbody").find_all("tr")
			for tr in trs:
				ip = tr.find("td").text
				ipList.append(ip)
			
			return ipList

		except:
			return False					






			