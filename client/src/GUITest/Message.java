/*
	Bryan Carter 	c03697673
        Message.java
        A basic message object to simplify passing information between endpoints.
        Also performs the "A = g^a mod p" portion of the Diffie-Hellman key exchange.
           (Will later fix above, current version breaks protocol, should not transmit DHSecret).
 */
package GUITest;                                                                // package declaration.

public class Message 
{
    /* variable declaration block begins */
    Object payload;                                                             // Plain old superclass to ensure anything can fit in the payload.
    int DHModulus;                                                              // Modulus for Diffie-Hellman.
    int DHBase;                                                                 // Base for Diffie-Hellman.
    int DHSecret;                                                               // Secret value for Diffie-Hellman.
    int DHNumber;                                                               // Transmitted valuefor Diffie-Hellman.
    /* variable declaration block ends */
    
    public Message()
    /* class constructor for Message objects begins. */
    {
    
    }
    /* class constructor for Message objects ends. */
    
    public Object setPayload(Object newPayload)
    /* method to set message payload begins. */
    {
        payload = newPayload;
        return payload;
    }
    /* method to set message payload ends. */
    
    public int setDiffieHellman(int newModulus, int newBase, int newSecretA)
    /* method to set Diffie-Hellman variables begins. */
    {
        this.setModulus(newModulus);
        this.setBase(newBase);
        this.setSecret(newSecretA);
        DHNumber = (DHBase ^ DHSecret) % DHModulus;
        return DHNumber;
    }
    /* method to set Diffie-Hellman variables ends. */
    
    public int setModulus(int newModulus)
    /* method to set Diffie-Hellman Modulus begins. */
    {
        DHModulus = newModulus;
        return newModulus;
    }
    /* method to set Diffie-Hellman Modulus begins. */
    
    /* method to set Diffie-Hellman Base begins. */
    public int setBase(int newBase)
    {
        DHBase = newBase;
        return newBase;
    }
    /* method to set Diffie-Hellman Base ends. */
    
    /* method to set Diffie-Hellman Secret begins. */
    public int setSecret(int newSecretA)
    {
        DHSecret = newSecretA;
        return DHSecret;
    }
    /* method to set Diffie-Hellman Secret ends. */
            
}
