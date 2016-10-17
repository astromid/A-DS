# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:52:20 2016

@author: astro
Task 2 - compare shake- and paste-sort algorithms
"""
import numpy as np


def generateRandomArr(n):
    arr = [np.random.choice(10000) for i in range(0, n)]
    return arr


def pasteSort(arr):
    n = len(arr)
    N_cmp = 0
    N_swap = 0
    for i in range(1, n):
        x = arr[i]
        j = i
        N_cmp += 1
        while j > 0 and arr[j-1] > x:
            N_cmp += 1
            N_swap += 1
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = x
    return (N_cmp, N_swap)


def shakeSort(arr):
    l = 0
    r = len(arr) - 1
    N_cmp = 0
    N_swap = 0
    while l <= r:
        for i in range(l, r):
            N_cmp += 1
            if arr[i] > arr[i+1]:
                N_swap += 2
                arr[i], arr[i+1] = arr[i+1], arr[i]
        r -= 1
        for i in range(r, l, -1):
            N_cmp += 1
            if arr[i-1] > arr[i]:
                N_swap += 2
                arr[i], arr[i-1] = arr[i-1], arr[i]
        l += 1
    return (N_cmp, N_swap)

'''
tlen = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
for length in tlen:
    lst = generateRandomArr(length)
    N1_cmp, N1_swap = pasteSort(lst.copy())
    N2_cmp, N2_swap = shakeSort(lst.copy())
    msg = 'Len = {}, paste: cmp {}, swap {}; shaker: cmp {}, swap {}\n'
    print(msg.format(length, N1_cmp, N1_swap, N2_cmp, N2_swap))
'''


def oneStepBubble(arr, direction):
    n = len(arr)
    # direction: bool, true - >, false - <
    if direction:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


lst = generateRandomArr(1000)
data = []
data.append(lst.copy())
lst2 = lst.copy()
for i in range(1000):
    oneStepBubble(lst, True)
    data.append(lst.copy())
for i in range(1000):
    oneStepBubble(lst2, False)
    data.insert(0, lst2.copy())

# с шагом в 0,02 по sort ratio
for i in range(0, len(data), 20):
    data_curr1 = data[i].copy()
    data_curr2 = data[i].copy()
    N1_cmp, N1_swap = pasteSort(data_curr1)
    N2_cmp, N2_swap = shakeSort(data_curr2)
    ratio = (i - 1000) / 1000
    msg = 'Ratio = {}, paste: cmp {}, swap {}; shaker: cmp {}, swap {}\n'
    print(msg.format(ratio, N1_cmp, N1_swap, N2_cmp, N2_swap))
