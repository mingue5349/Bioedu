import sys
n = sys.argv[1]
k = sys.argv[2]

fibo_l = [1,1]

i = 2
while i < int(n):
    f0 = fibo_l[i-2]
    f1 = fibo_l[i-1]
    f2 = f0*int(k) + f1
    fibo_l.append(f2)
    i += 1

print (fibo_l[-1])