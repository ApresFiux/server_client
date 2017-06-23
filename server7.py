import os
import sys
import socket
try:
	def WriteDATA(data,MC):
		jar = {}
		parameter = input("enter a parameter")
		jar[data] = parameter
		MainCounter = (MainCounter + 1)
	def DATA(addr,sock,c,MC):
		while True:
			print("works")
			data = c.recv(1024)
			if not data:
				print(str(addr) + "Client Disconnected")
				break
			print ("reveived data: " + str(data))
			c.send()
			WriteDATA(data,MC)
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
			port = input("Please enter port: ")
			try:
				port = int(port)
				socketing(port, MC)
				break
			except ValueError:
				print ("please enter numbers only")
	except KeyboardInterrupt:
		print(" user-quit")
except KeyboardInterrupt:
	print(" user-quit")
