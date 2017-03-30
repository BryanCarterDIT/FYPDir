/*
	Bryan Carter - C03697673
	Java Echo Client test for FYP.
	20/10/2016
	Based on tutorials found at: 
	http://introcs.cs.princeton.edu/java/84network/EchoClient.java.html
		and
	http://docs.oracle.com/javase/tutorial/networking/sockets/examples/EchoClient.java
*/

/* import block begins */
import java.io.*;																									// import all of java's IO functions.
import java.net.*;																									// import all of java's networking functions.
/* import block ends */

public class EchoClient
{
	public static void main(String[] args) throws Exception
	{
		/* usage checking begins */
		if(args.length != 2)
		// check that there are enough args
		{
			System.err.println("Usage: java EchoClient <host name> <message>");										// tell us if there aren't and...					
			System.exit(1);																							// ...exit with error code.
		}
		/* usage checking ends */
		
		/* variable declaration block begins */
		String server_IP = args[1];																					// take the IP from the args.
		String message = args[0];																					// take message from args.
		String reply;																								// declare reply string, left blank here.
		int serverPort = 12345;																						// port is same as server.
		/* variable declaration block ends */
		
		/* trying to make a connection */
		try
		{
			Socket sockpuppet = new Socket(server_IP, serverPort);													// set the socket variables.
			PrintWriter clientMessage =  new PrintWriter(sockpuppet.getOutputStream(), true);						// declare the message stream.
			BufferedReader serverReply = new BufferedReader(new InputStreamReader(sockpuppet.getInputStream()));	// declare the reply stream.
		
				
			System.out.println("Connected to " + server_IP + " on port " + serverPort);								// tell us we've connected.
			System.out.println("Message to be sent is: \"" + message + "\"");										// repeat the message to us.
			System.out.println("Sending message...");																// tell us that it's being sent.
			clientMessage.println(message);																			// send the message.
		
			reply = serverReply.readLine();																			// get the server's reply.
			System.out.println("Server replied! Message is: \"" + message + "\"");									// tell us we've got it and print.
			
			clientMessage.close();																					// close the outward stream.
			serverReply.close();																					// close the inward stream.
			sockpuppet.close();																						// close the socket.
			System.out.println("Connection closed.");																// tell us the connection has been closed.
			System.out.println("Press enter to terminate.");														// tell us how to exit.
			System.in.read();																						// wait for us to do it.
		}
		catch(UnknownHostException E)
		// in case the IP can't be found...
		{
			System.err.println("Can't find server: " + server_IP);													// tell us and...
			System.exit(1);																							// ...exit with error code.
		}
	}
}