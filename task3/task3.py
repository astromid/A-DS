# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:10:46 2016

@author: astro
"""

import numpy as np
import time


def generateRandomArr(n):
    arr = [np.random.choice(10000) for i in range(0, n)]
    return arr


def qsort(arr):
    if arr:
        return qsort([x for x in arr if x < arr[int(len(arr)/2)]]) + \
            [x for x in arr if x == arr[int(len(arr)/2)]] + \
            qsort([x for x in arr if x > arr[int(len(arr)/2)]])
    return []


def shellsort(arr):
    def new_d(arr):
        i = int(len(arr) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(i / 2)
            yield i
    for d in new_d(arr):
        for i in range(d, len(arr)):
            for j in range(i, d-1, -d):
                if arr[j - d] < arr[j]:
                    break
                arr[j], arr[j - d] = arr[j - d], arr[j]
    return arr


'''
tlen = [5, 10, 50, 100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
tlen += [35000, 45000, 55000, 65000, 75000, 85000, 100000]
for length in tlen:
    lst = generateRandomArr(length)
    start_time = time.time()
    qsort(lst.copy())
    qTime = time.time() - start_time
    start_time = time.time()
    shellsort(lst.copy())
    sTime = time.time() - start_time
    msg = 'Len = {}, qsort: {}; shellsort: {}\n'
    print(msg.format(length, qTime, sTime))
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


lst = generateRandomArr(3000)
data = []
data.append(lst.copy())
lst2 = lst.copy()
for i in range(3000):
    oneStepBubble(lst, True)
    data.append(lst.copy())
for i in range(3000):
    oneStepBubble(lst2, False)
    data.insert(0, lst2.copy())

# с шагом в 0,05 по sort ratio
for i in range(0, len(data), 150):
    data_curr1 = data[i].copy()
    data_curr2 = data[i].copy()
    start_time = time.time()
    qsort(data_curr1)
    qTime = time.time() - start_time
    start_time = time.time()
    shellsort(data_curr2)
    sTime = time.time() - start_time
    ratio = (i - 3000) / 3000
    msg = 'Ratio = {}, qsort: {}; shellsort: {}\n'
    print(msg.format(ratio, qTime, sTime))
