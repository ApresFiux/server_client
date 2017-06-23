import os
import sys
import socket
try:
	def WriteDATA(datafile,data,MC):
		jer = {}
		jer[data] = MC
		MC += 1
		jeb = jer.keys()
		jert = str(jeb)
		MC =str(MC)
		jert2 = jert + MC
		datafile.write(jert + os.linesep)
		jer = {}
		return(MC)
	def DATA(datafile,addr,sock,c,MC):
		while True:
			print("works")
			data = c.recv(1024)
			if not data:
				print(str(addr) + "Client Disconnected")
				break
			print ("reveived data: " + str(data))
			WriteDATA(datafile,data,MC)
			c.send(data)
			return (data) 	
	def serverconnection(sock,addr,MC):
		while True:
			c, addr = sock.accept()
			countfile = open("count.art", 'r')
			countline = countfile.readline()
			count = str(countline)
			datafile = open("data." + count, 'w')
			print("Client Conneted from: " + str(addr))
			DATA(datafile,addr,sock,c,MC)
			count = int(count)
			count = count + 1
			count = str(count)
			countfilewrite = open("count.art", 'w')
			countfilewrite.write(count)
			countfilewrite.close()
			c.close()
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
