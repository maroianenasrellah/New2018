##					j = 10
##					while j > 0:
####                                            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 12,keyA_Prive, uid)
##                                            if status == MIFAREReader.MI_OK:
##                                                print(j-1,"seconde Reste")
##                                                print("veuillez retirer votre Carte")
##                                                j = j - 1
##                                                time.sleep(1)
##                                            if j == 0:
##                                                MIFAREReader.MFRC522_StopCrypto1()
##                                                time.sleep(2)