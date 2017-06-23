import os
import sys
import socket
try:
	def WriteDATA(datafile,c,data,MC,count):
		jer = {}
		jer[data] = count
		jeb = jer.items()
		jert = str(jeb)
		count =str(count)
		#datafile.write(jeb)
		print(jeb, os.linesep, file=datafile)
		jer = {}
		count = int(count)
		count += 1
#		return(MC)
	def DATA(datafile,addr,sock,c,MC):
		while True:
			print("works")
			count = 0
			data = c.recv(1024)
			if not data:
				print(str(addr) + "Client Disconnected")
				break
			print ("reveived data: " + str(data))
			c.send(data)
			WriteDATA(datafile,c,data,MC,count)
#			return (data) 	
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
