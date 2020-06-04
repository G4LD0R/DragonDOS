# DragonDOS & IP Spoof Tool

**Author** = ["Hasan Baskın"](https://www.hasanbaskin.com/)

### IP Spoofing 

IP spoofing refers to the process of creating and sending an IP packet for a certain destination using a different source address, then the actual source IP address.
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
                   



### Screenshots of Script

![Image](https://i.ibb.co/tsh0wTx/dos.png)


### Installation

`$ sudo apt-get install git`<br />
`$ git clone https://github.com/G4LD0R/DragonDOS.git`<br />
`$ cd DragonDOS`<br />
`$ sudo chmod +x DragonDOS.py` <br />
`$ sudo chmod +x ip_generators.py`<br />
`$ sudo chmod +x networkScanner.py`<br />


### Usage

https:www.youtube.com/


### Warning

*This script only created to uses on penetration tests.*<br />
*Only the users be responsible when occurred an abuse.*<br />
*This script consist of volume-based dos attacks and protocol attacks.*<br />
*You can choose one of two options. Those are options 1 or option 2.*<br />
*This program performs IP Spoofing also. (You must use the second option for this)*<br />

- Basic Attack Type <br />
*This Attack type performs with random IP addresses and TCP packets.* <br />
*it takes simply destination IP address and destination port number from the user. Then it start the attack.*<br />

- Specific Attack Type<br />

*This attack-type contains different options. You can use wordlist files, random IP addresses, your own IP address for the*<br /> *source IP address.*<br /> 
*Additionally, you can use real IP addresses toke from free proxy websites. This program can perform all of them for you.*<br />
*You can choose the protocol type according to how you want between TCP packets and UDP packets.*<br />

*This version is only a start-up.*<br />
*I continue developing this script.*<br />
*I hope this usefully for you.*<br />

*If you want to contact me, you should send a mail : info@hasanbaskin.com*<br />
