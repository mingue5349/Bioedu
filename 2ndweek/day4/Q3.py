#!/usr/bin/env python

#fibolist = [0,1]
#
#def fibonachi(n_th_fivo):
#    for i in range(int(n_th_fivo)):
#        f0 = fibolist[i]
#        f1 = fibolist[i+1]
#        f2 = int(f0) + int(f1)
#        fibolist.append(f2)
#    result = fibolist[-3]
#    return result
#
#print (fibonachi(8))

fib_l = [0,1]

def fibolist(n_th_fibo):
    i = 2
    while i < int(n_th_fibo):
        f0 = fib_l[i-2]
        f1 = fib_l[i-1]
        f2 = f0 + f1
        fib_l.append(f2)
        i += 1
    result = fib_l
    return result

print (fibolist(0))
#l_pivo = [0,1]
#
#pivoIn = input('n_th pivo:')
#pivoIn = int(pivoIn)
#
#for i in range (pivoIn -2):
#    l_pivo.append(l_pivo[-1] + l_pivo[-2])
#print (l_pivo[-1])        
    

