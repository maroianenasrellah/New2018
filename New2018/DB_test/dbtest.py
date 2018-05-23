#!/usr/bin/env python
import MySQLdb
#import mysqldb


db = MySQLdb.connect("192.168.1.11", "SDA", "SDAsda124816", "practice_golf")
curs=db.cursor()

curs.execute ("SELECT * FROM clients")

print ("\nid     	Nom		Prenom		Societe")
print ("===========================================================")

for reading in curs.fetchall():
    print (reading[1],str(reading[2]),str(reading[3]),str(reading[4]),str(reading[4]))

def insert_passage(nom, prenom, societe, date, uid):

    cursor.execute ("""
       UPDATE clients
       SET NOM=%s, PRENOM=%s, SOCIETE=%s, DATE=%s, UID=%s
       WHERE Server=%s
    """, (nom, prenom, societe, date, uid))
