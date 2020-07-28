#!/usr/bin/env python

#FI = open ('./dataFile.txt','r')
#print(FI.read())
#FI.close()

 
#FI = open ('./dataFile.txt','r')
#print (FI.readlines())
#FI.close()


FI = open ('dataFile.txt', 'r')
print(FI.readline().strip())
FI.close()
