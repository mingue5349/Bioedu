#!/usr/bin/env python

d_reg = {'regNum0':'951213-0000000', 'regNum1':'960125-0000000', 'regNum2':'970705-0000000'}

d_month = {'12':"Dec",'01':"Jan",'07':"Jul"}
#
#reg0month = d_reg['regNum0'][2:4]
#reg1month = d_reg['regNum1'][2:4]
#reg2month = d_reg['regNum2'][2:4]
#
#reg0date = d_reg['regNum0'][4:6]
#reg1date = d_reg['regNum1'][4:6]
#reg2date = d_reg['regNum2'][4:6]
#
#print (d_month[reg0month] +'-'+reg0date)
#print (d_month[reg1month] +'-'+reg1date)
#print (d_month[reg2month] +'-'+reg2date)

month = {}
date = {}

#{'regNum0': '12', 'regNum1': '01', 'regNum2': '07'}
for keys in d_reg.keys():
    month[keys] = d_reg[keys][2:4]

for vals in month.values():
    if vals in d_month[keys]:


print (month)
print (date)
