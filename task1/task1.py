# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:12:31 2016

@author: astro

Task 1 - compare Knuth–Morris–Pratt and bruteforce algorithms
"""

import numpy as np

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
    N = 0
    
    D = [0 for i in range(m)]
    for i in range(1, m):
        k = D[i-1]
        while k > 0 and needle[k] != needle[i]:
            k = D[k-1]
            N += 1
        N += 1
        if needle[k] == needle[i]:
            k += 1
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
        if k == m:
            pos = i - m + 1
            break
    return (pos, N)
    
#сектор сбора статистики
text = open('dna.txt', 'r')
haystack = text.read()
text.close()

#т.к. строчка случайная, необходимо повторить N раз
N_brute_all = 0
N_KMP_all = 0
for step in range(100):
    
    #генерируем строку, которой нет в тексте
    alphabet_no = ['A', 'B', 'C', 'D']
    needle_len = 50
    needle= ''
    for i in range(needle_len):
        index = np.random.choice(len(alphabet_no))
        needle += alphabet_no[index]

    (pos_brute, N_brute) = bruteforce(needle, haystack)
    (pos_KMP, N_KMP) = KMP(needle, haystack)
    N_brute_all += N_brute
    N_KMP_all += N_KMP

N_brute_all = N_brute_all / 100
N_KMP_all = N_KMP_all / 100
print('Len(needle)= ' + str(len(needle)) + ' Len(haystack)= ' + str(len(haystack)) + \
' N_brute_avg=' + str(N_brute_all) + ' N_KMP_avg=' + str(N_KMP_all))