# DragonDOS & IP Spoof Tool

#IP Spoofing :

IP spoofing refers to the process of creating and sending an IP packet for a certain destination using a different src address, then the actual source IP address.
Spoofing the source IP address can be possibly used for,
1. the purpose of concealing the identity of the sender or
2. impersonating another computing system (misleading the destination)
3. defeating network security measures, such as authentication based on IP addresses

Implemented attacks(mostly on Internet Protocol):

1. Denial Of Service attack (DOS attack)
   Goal          : To flood the victim with overwhelming amounts of traffic, without considering the responses to the attack packets.
   Prerequisites : No service/response is expected from the targeted machine, thus it makes up to the most basic form of attack.
   Strategy      : Saturating the target machine with external communications requests, such that it cannot respond to legitimate traffic, or 		   	           responds so slowly as to be rendered essentially unavailable (Server overload).
   Consequence   : Makes the network resource unavailable to its intended users.
                   Forces the targeted computer(s) to reset, or consume its resources so that it can no longer provide its intended service 		 	                Obstructing the communication media between the intended users and the victim so that they can no longer communicate adequately
                   
   - Implemented ICMP Flooding, 
     Source code : dos_attack.py
                 ICMP pacekts contained in IP packets are forwarded to the target, by using many different IP addresses along many threads           	              simultaneously, and each thread sends the IP packets indefinitely
	 Test command : sudo python dos_attack.py "target_IP_address"
	 Note : "impacket" module needed beforehand

**Author** = ["Hasan Baskın"](https://www.hasanbaskin.com/)

#### `Screenshots of Script`

![Image](https://i.ibb.co/tsh0wTx/dos.png)

### Manuel

`$ sudo apt-get install git`<br />
`$ git clone https://github.com/G4LD0R/DragonDOS.git`<br />
`$ cd DragonDOS`<br />
`$ sudo chmod +x DragonDOS.py` <br />
`$ sudo chmod +x ip_generators.py`<br />
`$ sudo chmod +x networkScanner.py`<br />


