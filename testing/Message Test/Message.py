#
# 	Bryan Carter 	c03697673
#	Message.py
#	A basic message object to simplify passing information between endpoints.
#	Also performs the "A = g^a mod p" portion of the Diffie-Hellman key exchange.
#		(Will later fix above, current version breaks protocol, should not transmit DHSecret).
#
 

class Message:
'A basic message object to simplify passing information between endpoints.
Also performs the "A = g^a mod p" portion of the Diffie-Hellman key exchange.
	(Will later fix above, current version breaks protocol, should not transmit DHSecret).' 
{
	# variable declaration block begins #
	payload;																# Plain old superclass to ensure anything can fit in the payload.
	DHModulus;																# Modulus for Diffie-Hellman.
	DHBase;																	# Base for Diffie-Hellman.
	DHNumber;																# Transmitted valuefor Diffie-Hellman.
	# variable declaration block ends #
	
	def _init_(self, payload, DHModulus, DHBase, DHSecret):
	# class constructor for Message objects begins. #
		self.payload = payload
		self.DHModulus = DHModulus 
		self.DHBase = DHBase
		self.DHSecret = DHSecret
		self.DHNumber = setDiffieHellman(DHModulus, DHBase, DHSecret)
	# class constructor for Message objects ends. #
	
	def setPayload(newPayload)
	# method to set message payload begins. #
		payload = newPayload;													# set payload equal to passed value.
		return payload;															# return payload.
	# method to set message payload ends. #
	
	def setDiffieHellman(newModulus, newBase, newSecretA)
	# method to set Diffie-Hellman variables begins. #
		this.setModulus(newModulus);											# call method to setModulus.
		this.setBase(newBase);													# call method to setBase.
		this.setSecret(newSecretA);											 	# call method to setSecret.
		DHNumber = (DHBase ^ DHSecret) % DHModulus;							 	# calculate DHNumber using "A = g^a mod p".
		return DHNumber;														# return DHNumber.
	# method to set Diffie-Hellman variables ends. #
	
	def setModulus(newModulus):
	# method to set Diffie-Hellman Modulus begins. #
		DHModulus = newModulus;												 	# det DHModulus value to passed newModulus value..
		return newModulus;													  	# return DHModulus.
	# method to set Diffie-Hellman Modulus begins. #
	
	
	def setBase(newBase)
	# method to set Diffie-Hellman Base begins. #
		DHBase = newBase;														# set DHBase equal to passed newBase value.
		return newBase;															# return newBase.
	# method to set Diffie-Hellman Base ends. #
	
	
	def setSecret(newSecretA)
	# method to set Diffie-Hellman Secret begins. #
		DHSecret = newSecretA;													# set DHSecret to passed newSecretA value.
		return DHSecret;														# return DHSecret.
	# method to set Diffie-Hellman Secret ends. #
			
}
