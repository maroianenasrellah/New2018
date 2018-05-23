#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO_relais = 40# le relais est branche sur la pin 40 / GPIO21
GPIO_LEDR = 36
GPIO_LEDV = 32
GPIO.setmode(GPIO.BOARD) # comme la librairie MFRC522
GPIO.setwarnings(False)
GPIO.setup(GPIO_relais, GPIO.OUT)# Define some device parameters
GPIO.setup(GPIO_LEDR, GPIO.OUT)
GPIO.setup(GPIO_LEDV, GPIO.OUT)


##GPIO.output(GPIO_LEDR, GPIO.LOW)
##time.sleep(0.25)
##GPIO.output(GPIO_LEDR, GPIO.HIGH)

GPIO.output(GPIO_LEDR,1)
time.sleep(1)
GPIO.output(GPIO_LEDR, 0)

GPIO.output(GPIO_LEDV,1)
time.sleep(1)
GPIO.output(GPIO_LEDV, 0)