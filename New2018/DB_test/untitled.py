#! /usr/bin/python
import MySQLdb
 
db= MySQLdb.connect(host="localhost",
user="pi",
passwd="PIpi124816",
db="mydb")
 
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
data = cursor.fetchone()
print  ("Resultat: ", data)
db.close()
