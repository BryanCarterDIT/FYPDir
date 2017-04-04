# import block begins #
import socket
import SocketServer
import threading
import time
# import block ends #

# variable declaration block begins #
authstr = "AUTH"
authvalue = str(authstr)
liststr = "LIST"
listvalue = str(liststr)
response = ""
# variable declaration block ends #


# function to auth user begins #
def auth(user,address, password):
	response = ""
	response = "{} logged in from {} with password {} on {} {}\n".format(user,address,password,time.strftime("%H:%M:%S"),time.strftime("%d/%m/%Y"))
	return response
# function to auth user ends #

# TCP request handling thread class begins #
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)

#split the input into multiple words broken by spaces - first word will be an uppercase command. or not.
	parser = data.split(' ')
	command = str(parser[0])
	cmd=command.rstrip('\r\n')

	# if the command recieved is for authentication...
	if cmd == authvalue:
                # if they're doing it wrong...
		if len(parser) < 3:
                        # tell them how to do it right
			response = 'USAGE: Auth <USERNAME> <PASSWORD>\r\n'
			self.request.sendall(response)
			print 'USAGE: Auth <USERNAME> <PASSWORD>\r\n'
                # or they're doing it right...
		else:
                # TODO: DATABASE INTERACTION CODE GOES HERE
			output=auth(parser[1], self.client_address[0], parser[2])
			self.request.sendall(output)
			print(output)
        # or if we want to list our potential client contacts...
	elif cmd == listvalue:
		print'list of contacts goes here\r\n'
		response = 'list of contacts goes here\r\n'
		self.request.sendall(response)
        # otherwise...
	else:
		response = "{}: {}".format(self.client_address[0], data)
	        self.request.sendall(response)
		print(response)
# TCP request handling thread class ends #

# TCP threaded server class begins #
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
# TCP threaded server class ends #

# if the context is main run the program #
if __name__ == "__main__":
    # set host to 0.0.0.0 to allow all IP addresses to connect, port to 9999 #
    HOST, PORT = "0.0.0.0", 9999

    # create new TCP SocketServer bound to HOST on PORT as defined above #
    server = SocketServer.TCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    # run the server until killed with Ctrl+C #
    server.serve_forever()
# end of main #
