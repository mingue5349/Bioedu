import sys
k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

HxH = (m/(k+m+n)*(m-1)/(k+m+n-1)*1/4)
HxR = (m/(k+m+n)*n/(k+m+n-1)*1/2)*2
RxR = (n/(k+m+n)*(n-1)/(k+m+n-1))

print (1-HxH-HxR-RxR)