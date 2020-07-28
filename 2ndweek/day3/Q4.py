#!/usr/bin/env python

#s_str = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
#
#l_s = s_str.split(" ")
#
#dic = {}
#
#for i in l_s:
#    a = l_s.count(i)
#    if i not in dic.keys():
#        dic[i] = a 
#    else:
#        continue


#for i in dic:
#    print (i,dic[i])



import collections

#l_str = s_str.split(' ')


#collections 모듈의 Counter를 이용하면 자동으로 개수 세줌
#cnt = collections.Counter(l_str)
#print (cnt)


A = ['a','b','a','c','d','f']
B = ['b','c','d','e','e','e']
C = ['q','w','e','r','t','y','y','y']

a_cnt = collections.Counter(A)
b_cnt = collections.Counter(B)
c_cnt = collections.Counter(C)

a_cnt['a'] += 5
#print (a_cnt)
print (a_cnt | b_cnt)
print (a_cnt & b_cnt)
print (a_cnt + b_cnt)
print (a_cnt - b_cnt)






