#!/usr/bin/python 
#-*- coding: utf-8 -*-
#networkScanner.py

author = "G4LD0R - https://github.com/G4LD0R"

from scapy.all import ARP, Ether, srp
import sys, os
import netifaces
import DragonDOS


#colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
LIGHTBLUE = '\033[0;96m'
DARKYELLOW = '\033[33m'
FLASH = '\033[5m'
DARKGREEN = '\033[92m'
print(DragonDOS._banner_)


def netScanner(target_ip):
	# targetip Address for the destination
	# create ARP packet
	arp = ARP(pdst=target_ip)
	# create the Ether broadcast packet
	# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = ether/arp
	result = srp(packet, timeout=3, verbose=0)[0]

	# a list of clients
	clients = []
	for sent, received in result:
	    # for each response, append ip and mac address to `clients` list
	    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

	# print clients
	print(FAIL+"\t\tAvailable Devices in the Network"+ENDC)
	print("\t\t{1}--------------------------------{0}".format(ENDC, WARNING))
	print("\t\t    {1}IP{0}".format(ENDC, UNDERLINE) + " "*18+"{1}MAC{0}".format(ENDC, UNDERLINE))
	for client in clients:
	    print("\t\t{:16}    {}".format(client['ip'], client['mac']))

	



if __name__ == "__main__":
	
	_interfaces_ = netifaces.interfaces()
	option = 0

	print("\t\t{1}[{3}i{1}]{2} Network Interfaces on the Your System.{0}".format(ENDC, FAIL, LIGHTBLUE, OKGREEN))
	print(WARNING+"\t--------------------------------------------------------------"+ENDC)
	print("\t\t{1}[{3}?{1}]{2} Please Choose One of the Following for Scan.{0}\n".format(ENDC, FAIL, LIGHTBLUE, OKGREEN))

	for interface in _interfaces_:
		print("\t{1}[{0}{2}{1}]{0} {3}".format(ENDC, FAIL, option, interface))
		option +=1

	chs_interface = input("\n{3}[{2}?{3}]{0} Choose{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))


	try:
		addrsHead = netifaces.ifaddresses(_interfaces_[int(chs_interface)])
		own_ipAdress = addrsHead[netifaces.AF_INET][0]['addr']
		netmask = addrsHead[netifaces.AF_INET][0]['netmask']
	except:
		print("\n{1}[{0}!{1}]{2} This interface is not available.{0}".format(ENDC, FAIL, HEADER))
		sys.exit()


	if netmask == "255.255.255.0":
		scan_ip = own_ipAdress+"/24"
	elif netmask == "255.255.0.0":
		scan_ip = own_ipAdress+"/16"
	elif netmask == "255.0.0.0":
		scan_ip = own_ipAdress+"/8"
	os.system("clear")
	print(DragonDOS._banner_)
	netScanner(scan_ip)







