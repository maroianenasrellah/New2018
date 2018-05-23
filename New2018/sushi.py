#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import MFRC522
import smbus
import datetime
import MySQLdb


##print ("\nid     	Nom		Prenom		Societe")
##print ("===========================================================")


def Prive_keyA():
    keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74]  
    return keyA_Prive

def h2str(entree):
    sortie=str(chr(entree))
    return sortie


def write_card(secteur,uid,maxseau,conso,date):

    ##keyA_Prive=Prive_keyA()
    print("passage_1")
    if status == MIFAREReader.MI_OK:
        keyA_Prive = [0x59,0x61,0x50,0x6F,0x54,0x74] #"YaPoTt"
        print("passage_2")
        

 #       MIFAREReader.MFRC522_SelectTag(uid)   
        
 #       status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, secteur,keyA_Prive, uid)
        
        # If we have the UID, continue
##        if status == MIFAREReader.MI_OK:
##            backData = MIFAREReader.MFRC522_Read(secteur)
##            # Print UID
##            
##            print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
##            ##lcd_string(""+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]),LCD_LINE_2)
##            maxseau=0
##            conso=0
##            s = b"X" + str(date) + (conso).to_bytes(2, byteorder='big') + (maxseau).to_bytes(1, byteorder='big') + b"YAPO"                     
##            MIFAREReader.MFRC522_Write(secteur,s)
##            #print("s : ",hexdump.dump(s,sep=":"))
##            print("Ecriture terminée")
##
##            
##            backData = MIFAREReader.MFRC522_Read(secteur)
##            
##            print(h2str(backData[0]),end="")
##            c=1
##            while (c<9):
##                if(backData[c]!=0) :
##                    try :
##                        print(h2str(backData[c]),end="")
##                    except :
##                        print("Contenu Illisible")
##                c+=1
##            print(int(backData[9])*256+int(backData[10]),end="")
##            print(int(backData[11]),end="")
##            print("YAPO")
            
##   else:
##        print("statut n'est pas ok")
            
######################################################################################################################
#################################################FONCTIONS#################################################
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
    time.sleep(0.5)
    GPIO.output(GPIO_relais, GPIO.HIGH)
    ##GPIO.cleanup()
    lcd_init()
 
 #
def turnOn(pin,time_sleep_led):
    GPIO.output(pin,1)
    time.sleep(time_sleep_led)
    GPIO.output(pin,0)
    
def bouton():
    b=0
    while True:
        
        b=b+1
        state = True
        print("Attente bouton :"+str(b))
        time.sleep(0.5)
        confirm =input("voulez vous recuperer les Balles?\nReponse: ")
##
        if confirm == 'O' or confirm == 'o':
            state = False
            
        if not state:
            # on a appuye sur le bouton connecte sur la broche 19
            print("Bouton appuyé")
            time.sleep(0.5)

        break
    
    return state


def recup_date_val(dlv):
				Date_TEMP=""	
				Date_TEMP_OUT=""	
				c= 1
				while (c<9):
								if(dlv[c]!=0) :
												try :
																Date_TEMP=str(chr(dlv[c]))
																Date_TEMP_OUT=Date_TEMP_OUT+Date_TEMP
												except :
																print(" Contenu Illisible")
								c+=1
				return Date_TEMP_OUT

def msg(L1,L2):
	lcd_string(L1,LCD_LINE_1)
	lcd_string(L2,LCD_LINE_2)


db = MySQLdb.connect("192.168.1.11", "SDA", "SDAsda124816", "practice_golf")
curs=db.cursor()	#time.sleep(2)

def insert_passage(nom,prenom,societe,date,uid):

    curs.execute ("SELECT * FROM clients")
    cursor.execute ("""
           UPDATE clients
           SET NOM=%s, PRENOM=%s, SOCIETE=%s, DATE=%s, UID=%s
           WHERE Server=%s
        """, (nom, prenom, societe, date, uid))
