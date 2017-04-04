/*
	Bryan Carter - C03697673
	clienttest.java
	Simple CLI based java client to test python server.
*/

/* import block begins */
import java.io.*;																// import all of java's IO functions.
import java.net.*;																// import all of java's networking functions.
import java.util.Scanner;														// import the Command Line Scanner.		
/* import block ends */

public class clienttest
{
	public static void main (String[] args])	
	{
		int chatPort = 12345;													// port to make peer-to-peer connections.
		int serverPort = 9999;													// port is same as server.
		option menuChoice = -1;													// create menuchoice variable, initialise to negative value.
		Scanner textScanner = new Scanner(System.in);							// creates a scanner object to read text input from the command line.
		
		white(true)
		{
			if (file config set has server)
			// if the configuration file has been created...
			{
				normalOperation();													// run normally.
			}
			else
			// otherwise...
			{ 
				setupOperation();													// run setup.
				break;
			}
		}
	}
	
	public static int exitProgram(int exitCode)
	{
		System.exit(exitCode);
		return 1;
	}
	
	public static int normalOperation()
	{
		System.out.println("Please choose an option:");
		System.out.println("1: List Contacts.");	
		System.out.println("2: Add Contact.");
		System.out.println("3: Message Contact.");
		System.out.println("0: exit");
		menuChoice = textScanner.readInt();
		
		if (menuChoice == 1)
		{
				
		}
		else if (menuChoice == 2)
		{
			
		}
		else if (menuChoice == 3)
		{
			
		}
		else if (menuChoice == 0)
		{
			exitProgram(0);
		}
		else
		{
			System.out.println("Invalid choice, please try again.");
		}
		
	}
	
	public static int setupOperation()
	{
		System.out.println("Please choose an option:");
		System.out.println("1: add account");
		System.out.println("")
		System.out.println("0: exit");
		menuChoice = textScanner.readInt();
		
		if (menuChoice == 1)
		{
			
		}
		else if (menuChoice == 2)
		
		else if (menuChoice == 0)
		{
			exitProgram(0);
		}
		else
		{
			System.out.println("Invalid choice, please try again.");
		}
	}
}