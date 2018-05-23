import MFRC522
##while :
##      print("veuillez retirer votre Carte")
##      i=i+1
##if i== 5:
##    break
MIFAREReader = MFRC522.MFRC522()

while True:
    # Scan for cards
    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    print("Status: ",status,TagType)
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Carte detectee")
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # This is the private key for authentication
        keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74] #"YaPoTt"
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 12,keyA_Prive, uid)		
        if(status == MIFAREReader.MI_OK):
             print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
 
        i = 10
        while i > 0 and status == MIFAREReader.MI_OK:
            print(i,"seconde Reste")
            print("veuillez retirer votre Carte")
            i = i - 1
            
    
                                                   
                                                    
                                               
                                                    