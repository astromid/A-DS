# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:52:20 2016

@author: astro
Task 2 - compare shake- and paste-sort algorithms
"""
import numpy as np


def generateRandomArr(n):
    arr = [np.random.choice(1000) for i in range(0, n)]
    return arr, arr


def pasteSort(arr):
    n = len(arr)
    N = 0
    for i in range(1, n):
        x = arr[i]
        j = i
        N += 1
        while j > 0 and arr[j-1] > x:
            N += 2
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = x
    return N


def shakeSort(arr):
    l = 0
    r = len(arr) - 1
    N = 0
    while l <= r:
        for i in range(l, r):
            N += 1
            if arr[i] > arr[i+1]:
                N += 2
                arr[i], arr[i+1] = arr[i+1], arr[i]
        r -= 1
        for i in range(r, l, -1):
            N += 1
            if arr[i-1] > arr[i]:
                N += 2
                arr[i], arr[i-1] = arr[i-1], arr[i]
        l += 1
    return N

'''
for length in [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]:
    lst1, lst2 = generateRandomArr(length)
    N1 = pasteSort(lst1)
    N2 = shakeSort(lst2)
    print('Len = {}, paste = {}, shaker = {}\n'.format(length, N1, N2))
'''


def oneStepBubble(arr, direction):
    n = len(arr)
    # true - >, false - <
    if direction:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


lst1, lst2 = generateRandomArr(50)
data = []
data.append(lst1.copy())
for i in range(50):
    oneStepBubble(lst1, True)
    data.append(lst1.copy())
for i in range(50):
    oneStepBubble(lst2, False)
    data.insert(0, lst2.copy())

for i in range(len(data)):
    data_curr1 = data[i].copy()
    data_curr2 = data[i].copy()
    N1 = pasteSort(data_curr1)
    N2 = shakeSort(data_curr2)
    ratio = (i - 50) / 50
    print('Ratio = {}, paste = {}, shaker = {}\n'.format(ratio, N1, N2))