import os
import sys
import socket
try:
	def WriteDATA(data,c,MC):
		jer = {}
		parameter = input("enter a parameter")
		jer[data] = parameter
		MC += 1
		c.send()
		jeb = jer.keys()
		jert = str(jeb)
		MC =str(MC)
		jert2 = jert + MC
		datafile.write(jert + os.linesep)
		jer = {}
	def DATA(addr,sock,c,MC):
		while True:
			print("works")
			data = c.recv(1024)
			if not data:
				print(str(addr) + "Client Disconnected")
				break
			print ("reveived data: " + str(data))
			WriteDATA(data,c,MC)
			return (data) 	
	def serverconnection(sock,addr,MC):
		while True:
			c, addr = sock.accept()
			countfile = open("count.art", 'r')
			countline = countfile.readline()
			count = str(countline)
			datafile = open("data." + count, 'w')
			print("Client Conneted from: " + str(addr))
			DATA(addr,sock,c,MC)
	def socketing(port, MC):
		addr = '0.0.0.0'
		sock = socket.socket()
		sock.bind((addr, port))
		sock.listen(5)
		print("binding on port: " +str(port))	
		serverconnection(sock,addr,MC)	

	try:
		while True :
			MC = 0
			try:
				port = input("Please enter port: ")
				try:
					port = int(port)
					socketing(port, MC)
					break
				except ValueError:
					print ("please enter numbers only")
			except OSError:
				print ("please use another port as this port is alread in use")
	except KeyboardInterrupt:
		print(" user-quit")
except KeyboardInterrupt:
	print(" user-quit")
