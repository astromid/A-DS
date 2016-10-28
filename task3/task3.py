# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:10:46 2016

@author: astro
"""

import numpy as np
import time
import sys
sys.setrecursionlimit(5000)


def generateRandomArr(n):
    arr = [np.random.choice(10000) for i in range(0, n)]
    return arr


def qsort(arr):
    med = int(len(arr) / 2)
    if arr:
        return qsort([x for x in arr if x < arr[med]]) + \
            [x for x in arr if x == arr[med]] + \
            qsort([x for x in arr if x > arr[med]])
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


# повтор 10 раз для большей точности
tlen = [5, 10, 50, 100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
tlen += [35000, 40000, 50000, 60000, 70000, 80000, 100000]
output = open('results_1.txt', 'w')
for length in tlen:
    lst = generateRandomArr(length)
    start_time = time.time()
    for j in range(0, 10):
        qsort(lst.copy())
    qTime = (time.time() - start_time) / 10
    start_time = time.time()
    for j in range(0, 10):
        shellsort(lst.copy())
    sTime = (time.time() - start_time) / 10
    msg = 'Len = {}, qsort: {}; shellsort: {}\n'
    print(msg.format(length, qTime, sTime))
    output.write(str(length) + ' ' + str(qTime) + ' ' + str(sTime) + '\n')
output.close()


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
# повтор 50 раз для большей точности
output = open('results_2.txt', 'w')
for i in range(0, len(data), 150):
    start_time = time.time()
    for j in range(0, 50):
        qsort(data[i].copy())
    qTime = (time.time() - start_time) / 50
    start_time = time.time()
    for j in range(0, 50):
        shellsort(data[i].copy())
    sTime = (time.time() - start_time) / 50
    ratio = (i - 3000) / 3000
    msg = 'Ratio = {}, qsort: {}; shellsort: {}\n'
    print(msg.format(ratio, qTime, sTime))
    output.write(str(ratio) + ' ' + str(qTime) + ' ' + str(sTime) + '\n')
output.close()

