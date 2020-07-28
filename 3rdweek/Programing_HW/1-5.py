n = input('enter num: ')

def n_pec(n):
    j = 1
    for i in range(1,int(n)+1):
        j *= i
    return j

print (n_pec(n))