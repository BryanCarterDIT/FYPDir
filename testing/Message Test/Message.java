/*
	Bryan Carter 	c03697673
		Message.java
		A basic message object to simplify passing information between endpoints.

 */
package MessageTest;															// package declaration.

public class Message
{
    /* variable declaration block begins */
    Object payload;                                                             // Plain old superclass to ensure anything can fit in the payload.
    int DHModulus;                                                              // Modulus for Diffie-Hellman.
    int DHBase;                                                                 // Base for Diffie-Hellman.
    int DHNumber;                                                               // Transmitted valuefor Diffie-Hellman.
    /* variable declaration block ends */
    
    public Message(Object initialPayload, int initialDHModulus,int initialDHBase, int initialDHNumber)
    /* class constructor for Message objects begins. */
    {
    	payload = initialPayload;
    	DHModulus = initialDHModulus;
    	DHBase = initialDHBase; 
    	DHNumber = initialDHNumber;
    }
    /* class constructor for Message objects ends. */
    
    public Object setPayload(Object newPayload)
    /* method to set message payload begins. */
    {
        payload = newPayload;                                                   // set payload equal to passed value.
        return payload;                                                         // return payload.
    }
    /* method to set message payload ends. */
    
    public void setDiffieHellman(int newModulus, int newBase, int DHNumber)
    /* method to set Diffie-Hellman variables begins. */
    {
        this.setModulus(newModulus);                                            // call method to setModulus.
        this.setBase(newBase);                                                  // call method to setBase.
        this.setDHNumber(DHNumber);                                             // call method to setSecret.
    }
    /* method to set Diffie-Hellman variables ends. */
    
    public int setModulus(int newModulus)
    /* method to set Diffie-Hellman Modulus begins. */
    {
        DHModulus = newModulus;                                                 // det DHModulus value to passed newModulus value..
        return newModulus;                                                      // return DHModulus.
    }
    /* method to set Diffie-Hellman Modulus begins. */
    
    
    public int setBase(int newBase)
    /* method to set Diffie-Hellman Base begins. */
    {
        DHBase = newBase;                                                       // set DHBase equal to passed newBase value.
        return newBase;                                                         // return newBase.
    }
    /* method to set Diffie-Hellman Base ends. */
    
    public int setDHNumber(int newDHNumber)
    /* method to set Diffie-Hellman number begins. */
    {
        DHNumber = newDHNumber;													// set DHnumber equal to passed newBase value.
        return newDHNumber;                                                     // return newDHNumber.
    }
    /* method to set Diffie-Hellman number ends. */
}   
