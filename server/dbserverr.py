# Bryan Carter - C03697673
# Server test for FYP.
# 14/03/2017
# based on tutorial found at: https://pymotw.com/2/socket/tcp.html

# import block begins
import socket									# importing socket functions
import sys									# importing system call functions
from sql import *
#import block ends

# variable declaration block begins
server_ip = '0.0.0.0'								# set server IP address.
server_port = 12345								# set server port.
server_details =(server_ip, server_port)					# set server details.
message_size = 1024								# set message size to 1024 bytes.
print_message = 'Starting socket on port'		                        # create print message.
listen_message = 'Listening for a connection.' 					# create listen message.
connection_message = 'Connection recieved from '                                # create connection message.
EOS_message = 'EOS recieved from '                                              # create end-of-stream message.
# variable declaration block ends

sockpuppet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)			# socket created.
sockpuppet.bind(server_details)							# socket bound.
sockpuppet.listen(100)								# start listening for connections, buffer of 100.
print('Listening for a connection on port ', server_port)			# let us know it's listening.

while True:
	print('Still waiting...')						# print while waiting.
	connection,client_address = sockpuppet.accept()			# accept incomming connections.

	try:
		print (connection_message, client_address)			# let us know a connection was made.
		message = connection.recv(message_size)
		userID = message.userID
		make accountArray of incoming account names
		make tupleArray of account name/IP tuples
		cursor = mysql.connect().cursor()
		cursor.execute("UPDATE UserTable SET '" + client_address + "WHERE userID= " + message.userID)	
		
		while control > numberOfQueries:
			cursor.execute("SELECT " + ipAddress + " FROM UserTable WHERE " + username = accountArray[control])
			data = cursor.fetchone()
			tupleArray[control] = accountArray[control] + data
			control++
			break
		returnMessage = tupleArray
		connection.sendall(returnMessage)
		connection.close()							# clean up the connection.
		
		#while True:
		#	message = connection.recv(message_size)			# message is the data received.
		#	print('Recieved message: ', message, )			# print the message.
		#	if message:
			# if there is a message to print...
		#		print('Echoing message.')			# ...tell us and...
		#		connection.sendall(message)			# ...echo it back.
		#	else:
			#otherwise...

		#		print(EOS_message, client_address)		# ...tell us that and...
		#		print('Listening again.')			# ...let us know it's listening again and then...
		#		break						# ...exit.

	#finally:
	#	connection.close()							# clean up the connection.

