#!/usr/bin/env python


calc = '10 USD, 5 EUR, 7 JPY, 9 CNY'

money = {'USD': '1,203.82', 'EUR':'1,365.73', 'JPY':'11.22', 'CNY':'172.04'}

calc = calc.replace(",", "")

calc = calc.split(" ")

calcdic = {}

for i in range (len(calc)):
    if i%2 != 0:
         calcdic[calc[i]] = int(calc[i-1])
    else:
        continue

for i in money.keys():
    money[i] = float(money[i].replace(",",""))

for i in calcdic.keys():
    print (str(round(calcdic[i]*money[i],2)) + " KRW")

