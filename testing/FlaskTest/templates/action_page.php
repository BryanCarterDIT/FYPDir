<?php
	/*
		Bryan Carter C03697673
		action_page.php
		PHP script handling account creation and insertion into database for flask application.
		Provides user with their unique userID and the server's public key upon successful creation.
		Points user to instructions for creating a new account.
	*/	

	/* php variable declaration block begins */
	
	/* html variables begin */
	$htmlDoctype = "<!DOCTYPE html>";
	$htmlLang = "<html lang='en'>";
	$htmlHead = "<head><title>Account Creation</title><link href='http://getbootstrap.com/dist/css/bootstrap.min.css' rel='stylesheet'><link href='http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css' rel='stylesheet'><link href='../static/css/signup.css' rel='stylesheet'></head>";
	$htmlBodyStart = "<body><div class='container'><div class='header'><h3 class='text-muted'>Create Account</h3></div>";
	$htmlJumbotronStart = "<div class='jumbotron'><h2>Tinfoil cHat Account Creation</h2><p align=center>";
	$htmlJumbotronEnd = "</div>";
	$htmlFoot = "<footer class='footer'><p>&copy; Tinfoil Industries International 2017 - <img src='./static/images/shrug.gif'></p></footer>"
	$htmlTidyUp = "</body></html>";
	/* html variables end */
	
	/* database variables begin */
	$hostname = "localhost";
	$username = "username";
	$password = "password";
	$generatedID = "";
	$publickeypath = "./static/key/server_private_key.pem";
	/* database variables end */

	// Create connection
	$DBconnection = new mysqli($hostname, $username, $password);

	// Check connection
	if (!$DBconnection) 
	{
    	die("Connection failed: " . mysqli_connect_error());
	}
	// perhaps remove these echo statements about connections.
	echo "Connected successfully";
	
	// prepare our SQL query
	$sql = "INSERT INTO users(UserID, Public_Key_N, Public_Key_E, IP_Address) VALUES ('', '<READ FROM>', '<UPLOADED FILE>','300.300.300.300')";

	if (mysqli_query($conn, $sql)) 
	// run our query, and if it has succeeded...
	{
		// print the start of the HTML page...
		echo $htmlDoctype;
		echo $htmlLang;
		echo $htmlHead;
		echo $htmlBodyStart;
		echo $htmlJumbotronStart;
		// then give us the account details...
    	echo "Account created successfully!";
    	echo "Your account ID is: " .$generatedID;
    	echo "Please save the following <a href ='" .$publickeypath "'>Public Key File</a> to your ";
    	// and finally finish off the page by closing everything up.
    	echo $htmlJumbotronEnd;
    	echo $htmlFoot;
    	echo $htmlTidyUp;
	}
	else
	// or if it failed...
	{
		// print the start of the HTML page...
		echo $htmlDoctype;
		echo $htmlLang;
		echo $htmlHead;
		echo $htmlBodyStart;
		echo $htmlJumbotronStart;
		// let us know that it failed...
    	echo "Error: " . $sql . "<br>" . mysqli_error($conn);		// print the error message.
    	echo "Account not created. Please try again.";
    	// and finally finish off the page by closing everything up.
    	echo $htmlJumbotronEnd;
    	echo $htmlFoot;
    	echo $htmlTidyUp;
	}

	mysqli_close($conn);		// close the connection.
?> 