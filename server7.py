import os
import sys
import socket
try:
#	def GetData():
#		while True:
#			while data != 'exit':
#				c.send("get mode")
#				readfile = open(datafile, 'r')
#				lines = readfile.readlines()
#				victor = c.recv(1024)
#					
#				c.send()
	def DATA(datafile,addr,sock,c,COUNT):
		while True:
			print("works")
			data = c.recv(1024)
			if not data:
				print(str(addr) + socket.gethostbyaddr(str(addr)) + "Client Disconnected")
				break
			#if data == "get":                ##########
			#	GetData()
							########
			print ("reveived data: " + str(data))
			c.send(data)
			#WriteDATA(datafile,c,data,COUNT)
#			return (data) 	
			jer = {}
			jer[data] = COUNT
			print(jer)
			jeb = jer.items()
			jert = str(jeb)
			COUNT =str(COUNT)
			#datafile.write(jeb)
			print(jeb, os.linesep, file=datafile)
			jer = {}
			COUNT = int(COUNT)
			COUNT = (COUNT + 1)
			#return(COUNT)
	def serverconnection(sock,addr):
		while True:
			c, addr = sock.accept()
			countfile = open("count.art", 'r')
			countline = countfile.readline()
			count = str(countline)
			datafile = open("data." + count, 'w')
			print("Client Conneted from: " + socket.gethostbyaddr(str(addr)) + str(addr))
			COUNT = 0
			DATA(datafile,addr,sock,c,COUNT)
			count = int(count)
			count = count + 1
			count = str(count)
			countfilewrite = open("count.art", 'w')
			countfilewrite.write(count)
			countfilewrite.close()
			c.close()
	def socketing(port):
		addr = '0.0.0.0'
		sock = socket.socket()
		sock.bind((addr, port))
		sock.listen(5)
		print("binding on port: " +str(port))	
		serverconnection(sock,addr)	

	try:
		while True :
			try:
				port = input("Please enter port: ")
				try:
					port = int(port)
					socketing(port)
					break
				except ValueError:
					print ("please enter numbers only")
			except OSError:
				print ("please use another port as this port is alread in use")
	except KeyboardInterrupt:
		print(" user-quit")
except KeyboardInterrupt:
	print(" user-quit")
