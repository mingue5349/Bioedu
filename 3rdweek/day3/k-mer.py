# n bp 길이 NTD 의 모든 경우의 수를 출력해보자
import sys

n = int(sys.argv[1])
l1 = ['A','C','G','T']
l2 = ['A','C','G','T']
def mer(l1, l2, n):
    if n == 1:
        return l2
    
    ltmp = []
    for i in l1:
        for j in l2:
            ltmp.append(i+j)
    return mer(l1,ltmp,n-1)



print (mer(l1,l2,n))   
