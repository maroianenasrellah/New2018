#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import MFRC522
import smbus
import datetime
import sushi
exec(open("sushi.py").read())
##execfile("/home/pi/New/sushi.py")


# relais
GPIO_relais = 32 # le relais est branché sur la pin 32 / GPIO12
GPIO.setmode(GPIO.BOARD) # comme la librairie MFRC522
GPIO.setup(GPIO_relais, GPIO.OUT)

# Define some device parameters
##I2C_ADDR = 0x27 ou 0x3f #Afficheur de Xavier I2C device address, if any error, change this address to 0x3f
I2C_ADDR = 0x27
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command
  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def declencher_relais():
    GPIO.output(GPIO_relais, GPIO.LOW)
    time.sleep(1)
    GPIO.output(GPIO_relais, GPIO.HIGH)
    
def h2str(entree):
    sortie=str(chr(entree))
    return sortie

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

# Initialise display
lcd_init()
##keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74] #"YaPoTt"
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")
 
# This loop checks for chips. If one is near it will get the UID
try:
   
  while True:
      
    # Date
    stoday = datetime.datetime.today()
    # Display Message
    lcd_string(stoday.strftime("%d-%m-%Y %H:%M"),LCD_LINE_1)
    lcd_string("Attente Cartine",LCD_LINE_2)
    
    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # If a card is found
    keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74] #"YaPoTt"   

    if status == MIFAREReader.MI_OK:
        print ("Carte detectee")
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

     # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74] #"YaPoTt"
        
        MIFAREReader.MFRC522_SelectTag(uid)   
        
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 12,keyA_Prive, uid)
    
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            backData = MIFAREReader.MFRC522_Read(12)
            # Print UID
            

            
            print(h2str(backData[0]),end = "")
            c=1
            while (c<9):
                if(backData[c]!=0) :
                    try :
                        print(h2str(backData[c]),end="")
                    except :
                        print("Contenu Illisible")
                c+=1
            print(int(backData[9])*256+int(backData[10]),end="")
            print(int(backData[11]),end="")
            print("YAPO")



        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8,keyA_Prive, uid)
    
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            backData = MIFAREReader.MFRC522_Read(8)
            # Print UID

            
            print(h2str(backData[0]),end="")
            c=1
            while (c<9):
                if(backData[c]!=0) :
                    try :
                        print(h2str(backData[c]),end="")
                    except :
                        print("Contenu Illisible")
                c+=1

            print(int(backData[9])*256+int(backData[10]),end="")
            print(int(backData[11]),end="")
            print("YAPO")



            MIFAREReader.MFRC522_StopCrypto1()

          # Déclencher relais
            declencher_relais()

          # Attendre 2 secondes
            time.sleep(2)
 
except KeyboardInterrupt:
    lcd_string("MACHINE ARRETEE",LCD_LINE_1)
    lcd_string("ESSAYEZ + TARD",LCD_LINE_2)
    GPIO.cleanup()

