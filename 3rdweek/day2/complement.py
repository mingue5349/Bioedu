seq1 = 'ATGTTATAG'

seq1 = seq1.replace('A','t')
seq1 = seq1.replace('T','a')
seq1 = seq1.replace('G','c')

print (seq1.upper())



import sys

def comp1(seq: str)->str:
    comp_1 = ""
    for s in seq:   
        if s == 'A':
            comp_1 += 'T'
        elif s == 'C':
            comp_1 += 'G'
        elif s == 'G':
            comp_1 += 'C'
        elif s == 'T':
            comp_1 += 'A'
    return comp_1


def comp2(seq: str) -> str:
    d_comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    comp_2 = ""
    for s in seq:
        comp_2 += d_comp[s]
    return comp_2

# ipython 을 사용했을 때 대화형 모드에서 스크립트를 가져와 실행할 수 있게 해줌.  
# 또한 다른 파일에서 현재 파일의 함수를 불러와 사용할 수 있게 해줌,
# 예를 들어
# 다른 파일에서 import [파일명] 을 사용해서 불러오면
# 현재 파일의 함수를 사용할 수 있다. 
# 그리고 아래 라인 (if __name__ == '__main__':)은 새로운 파일의 함수를 실행했을 때 실행되지 않는다.

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print (f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print (seq)
    print (c1)
    print (c2)

