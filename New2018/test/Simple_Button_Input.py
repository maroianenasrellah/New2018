#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
##button program
GPIO_bouton = 40
GPIO_relais = 40
GPIO_LEDr = 7
GPIO_LEDv = 11
GPIO.setmode(GPIO.BOARD) # comme la librairie MFRC522
GPIO.setwarnings(False)
GPIO.setup(GPIO_bouton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_relais, GPIO.OUT)
GPIO.setup(GPIO_LEDr, GPIO.OUT)
GPIO.setup(GPIO_LEDv, GPIO.OUT)

try:
    while True:
        #if(GPIO.input(GPIO_bouton)== 1):
        if(GPIO.input(GPIO_relais)== 1):
           
            #GPIO.output(GPIO_LEDr,0)
            GPIO.output(GPIO_LEDv,1)
            time.sleep(1)
            GPIO.output(GPIO_LEDv,0)
            time.sleep(1)
        else:
            GPIO.output(GPIO_LEDr,1)
##            GPIO.output(GPIO_LEDv,0)
##            GPIO.output(GPIO_LEDr,0)
            #GPIO.output(GPIO_LEDr,1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    
