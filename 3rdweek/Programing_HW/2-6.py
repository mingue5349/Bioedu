l1 = ['A', 'C', 'G', 'T']
l2 = ['A', 'C', 'G', 'T']


def mer(l1, l2, n):
    if n == 1:
        return l2

    ltmp = []
    for i in l1:
        for j in l2:
            ltmp.append(i + j)
    return mer(l1, ltmp, n - 1)


mer7_l = mer(l1,l2,7)
palin_l = []
for i in mer7_l:
    if i[0:3] == i[::-1][0:3]:
        palin_l.append(i)
print (palin_l)

