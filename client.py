import os
import socket
try:
#	def GetData():
	
#		print(sock.recv(1024))
#		message = raw_input("<-- ")
#		sock.send
	def Client(port):
		host = '192.168.100.50'
		sock = socket.socket()
		sock.connect((host, port))
		#message = raw_input("<-- ")
		print ('Connected to ,"host",')
		message = raw_input("-> ")
		while message != "quit":
			sock.send(message)
			data = sock.recv(1024)
			print ("Recived from server: ") + str(data)
			message = raw_input("-> ")
		#	if message == "get":       ##########
		#		GetData()				
						########
		sock.close()
	try:
		try:
        	        while True :
                	        try:
                        	        port = input("Please enter port: ")
                                	try:
                                        	port = int(port)
	                                        Client(port)
        	                                break
                	                except ValueError:
                        	                print ("please enter numbers only")
	                        except OSError:
        	                        print ("binding server on this port not found")
		except KeyboardInterrupt:
        	        print(" user-quit")
	except socket.error:
		print(" Wrong port - RTO")
except KeyboardInterrupt:
        print(" user-quit")
