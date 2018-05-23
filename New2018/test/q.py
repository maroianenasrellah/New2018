#!/usr/bin/env python
#-*- coding: utf-8 -*-
try:
    
    while True:
        confirm =input("voulez vous recuperer les Balles?\nReponse: ")

        if confirm == 'yes' or confirm == 'YES' or confirm == 'Yes' or confirm =='Y' or confirm == 'y':
            print(confirm)
            print("Data written ...")
        else:
            print("NO DATA WRITTEN",confirm)
            
except KeyboardInterrupt:
    print("terminated")
    
