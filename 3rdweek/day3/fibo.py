# 피보나치 수열 - 재귀함수코드 예시

# 내가 짠 코드
#fibo_l = [0, 1]
#
#
#i = 2
#
#while len(fibo_l) < 50:
#    fibo_l.append(fibo_l[i-1] + fibo_l[i-2])
#    i += 1
#
#
#print (fibo_l)


# 강사님 짜신 코드
import sys

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) #함수도 return 가능. 

n = int(sys.argv[1])

print (fib(n))
