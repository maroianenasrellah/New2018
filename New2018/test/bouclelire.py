nom =['M','A','R','W','A','N','n','a','s','o','i','ne','r','l','l','a']
c= 0
while (c<16):
    if(nom[c]!=0):
        try :
            print (str(chr(nom[c])),end="")
             # print(str(chr(nomData[c])),end="")
                                                    #print(str(h2str(nomData[c])),end="")
        except :
            print(" Contenu Illisible")
    c+=1
print("\n")