import SocketServer
import threading
import socket
import time

authstr = "AUTH"
authvalue = str(authstr)
liststr = "LIST"
listvalue = str(liststr)
response = ""


def auth(user,address, password):
	response = ""
	response = "{} logged in from {} with password {} on {} {}\n".format(user,address,password,time.strftime("%H:%M:%S"),time.strftime("%d/%m/%Y"))
	return response


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)

#split the input into multiple words broken by spaces - first word will be an uppercase command. or not.
	parser = data.split(' ')
	command = str(parser[0])
	cmd=command.rstrip('\r\n')
	
#authentication
	if cmd == authvalue:
#they're doing it wrong
		if len(parser) < 3:
			response = 'USAGE: Auth <USERNAME> <PASSWORD>\r\n'
			self.request.sendall(response)
			print 'USAGE: Auth <USERNAME> <PASSWORD>\r\n'
#they're doing it right. 
		else:
#DATABASE INTERACTION CODE GOES HERE
			output=auth(parser[1], self.client_address[0], parser[2])
			self.request.sendall(output)
			print(output)
#we want to list our potential client contacts
	elif cmd == listvalue:
		print'list of contacts goes here\r\n'
		response = 'list of contacts goes here\r\n'
		self.request.sendall(response)
	else:
		response = "{}: {}".format(self.client_address[0], data)
	        self.request.sendall(response)
		print(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
	command = parser[0]
        print "{} wrote:".format(self.client_address[0])
        print self.data
	parser = self.data
	print parser[0]
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
