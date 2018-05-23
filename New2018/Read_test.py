import MFRC522
import time
MIFAREReader = MFRC522.MFRC522()

i=0

# This loop checks for chips. If one is near it will get the UID
try:

    while True:
        
		# Display Message


        print("Attente Carte : ",i)
		# Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
		
            # If a card is found
        if status == MIFAREReader.MI_OK:

            print ("Carte detectée")
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
		# If we have the UID, continue
            print(status,uid)
 


        time.sleep(1)
                    
except KeyboardInterrupt:
	lcd_string("MACHINE ARRETEE",LCD_LINE_1)
	lcd_string("ESSAYEZ + TARD",LCD_LINE_2)