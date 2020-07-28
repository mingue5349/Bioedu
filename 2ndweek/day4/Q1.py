#!/usr/bin/env python

sequence = input("input sequence: ")

#짝수 개 시퀀스일 때 회문서열을 판별

nucleotide = ['A','T','G','C']

while True:
    
    if len(sequence)%2 != 0:
        print("please enter sequence length with even number!!")

    else:
        rev_seq = sequence[::-1]
        rev_seq = rev_seq.replace('A','t')
        rev_seq = rev_seq.replace('T','a')
        rev_seq = rev_seq.replace('G','c')
        rev_seq = rev_seq.replace('C','g')
        rev_seq = rev_seq.upper()
        if rev_seq == sequence:
            print (sequence + " is palindromic")
        else:
            print (sequence + " is not plaindromic")
        
    break
