# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:12:31 2016

@author: astro

Task 1 - compare Knuth–Morris–Pratt and bruteforce algorithms
"""

#needle - искомая подстрока, halystack - текст
def bruteforce(needle, haystack):
    n = len(haystack)
    m = len(needle)
    pos = -1
    #кол-во операций сравнения
    N = 0
    for i in range(n-m+1):
        found = True
        for j in range(m):
            N += 1
            if needle[j] != haystack[i+j]:
                found = False
                break
        if found:
            pos = i
            break
    return (pos, N)
    
def KMP(needle, haystack):
    #первый шаг - трансляция
    n = len(haystack)
    m = len(needle)
    N_trans = 0
    N = 0
    
    D = [0 for i in range(m)]
    for i in range(1, m):
        k = D[i-1]
        while k > 0 and needle[k] != needle[i]:
            k = D[k-1]
            N_trans += 1
        if needle[k] == needle[i]:
            k += 1
            N_trans += 1
        D[i] = k
    
    #D - массив сдвигов
    pos = -1
    k = 0
    for i in range(n):
        while k > 0 and needle[k] != haystack[i]:
            k = D[k-1]
            N += 1
        N += 1
        if needle[k] == haystack[i]:
            k += 1
        N += 1
        if k == m:
            pos = i - m + 1
            break
    return (pos, N_trans, N)
    
    
text = open('dna.txt', 'r')
haystack = text.read()
text.close()
needle = 'ATTTTGACAGGTCGCGATGCAAACTATAGACAACAGGGTATGGTGTTGTGAACGATTGGCTCGTGGTGATTCGCGGGCAATCGTCGCTAAGCGTTTAAAGATCCGAGTGCGTCGTCCTAGATTTACAGTCTTCGACACTATACCAGCCTAACATGAGAGACGTCCCTACCTTGGCAAAGGGGAATGTCGCATCCGCTCAACTAGAGAAGCTTCCCATGTTCATGCGAACACGGGTTAGAACCGTCTCTTGACTTCGAATTGCGGCCAAAATGCCTTGCGGACGTCGACACCCCTTTTCGGACGGCCCGACCGAAAGTTGCCGCCGGGTTCTCCCTGGTTGGTATGGGAGGGAACCTGTCGCGCCCCTAGGCAGACTACTTCGAAGTCGTTAGAAACGCCGTTGGTCTCGATTGGTGAGCGAGTCCAACTCCCTAAGAGCCTAAGATACTTCCCCGAAATGCCTTAGCACATATCTTGGGAGCATGTATTTCCTGTCGTCGCGCCGCATAAAACTCCTAGTTGTGAGTTGGTATGTGCGAGCCGATTGTTTTTTCTTCGTCCGTGGATAGTTCGTTCAACGCGATACTCATCACCGACCCGTGGGCCAGACGAATCATCGAAAATAGAACAATAGGTTTAGATACTGCAGTCGGGGCTGTAGTCGGATGCGGCACCACGCGGTCCTCATCAAGCTTAGATTCGAGGGGTCGAACCATCTAGGAATGTTAACATCTGTGACTGATTCCAGGACGCCAC'

(pos_brute, N_brute) = bruteforce(needle, haystack)
(pos_KMP, N_trans, N_KMP) = KMP(needle, haystack)
print('Len(needle)= ' + str(len(needle)) + ' Len(haystack)= ' + str(len(haystack)) + \
' N_brute=' + str(N_brute) + ' N_trans= ' + str(N_trans) + ' N_KMP=' + str(N_KMP))