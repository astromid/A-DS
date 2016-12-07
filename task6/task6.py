#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:19:12 2016

@author: ys-budakyan
"""
import numpy as np


# Peter J. Weinberger hash function
def PJWHash(key, N):
    # BI, TQ, OE, HB constants
    BitsInUnsignedInt = 4 * 8
    ThreeQuarters = int((BitsInUnsignedInt * 3) / 4)
    OneEighth = int(BitsInUnsignedInt / 8)
    HighBits = (0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth)

    hashPJW = 0
    hashHB = 0
    for s in key:
        hashPJW = (hashPJW << OneEighth) + ord(s)
        hashHB = hashPJW & HighBits
        if hashHB != 0:
            hashPJW = ((hashPJW ^ (hashHB > ThreeQuarters)) & (~HighBits))
    return (hashPJW & 0x7FFFFFFF) % N


# Daniel J. Bernstein hash function
def DJBHash(key, N):
    hashDJB = 0
    for s in key:
        hashDJB = ((hashDJB << 5) + hashDJB) + ord(s)
    return (hashDJB & 0x7FFFFFFF) % N

textfile = open('war-and-peace.txt', 'r')
words = [line.split() for line in textfile]
textfile.close()
# flat words list
words = [word for line in words for word in line]
# number of unic words (from previous task)
N = 30500
hashtablePJW = [None]*N
hashtableDJB = [None]*N
usedSpacePJW = 0
usedSpaceDJB = 0
# statistics resolution(1% of filling value)
M = 100
collisionPJW = np.zeros(M)
collisionDJB = np.zeros(M)
for word in words:
    collPJW_flag = False
    collDJB_flag = False
    keyPJW = PJWHash(word, N)
    keyDJB = DJBHash(word, N)
    # % of used space in hashtable
    aPJW = (usedSpacePJW / N) * 100
    aDJB = (usedSpaceDJB / N) * 100
    # some reporting
    msg = 'usedSpace:  {:.3f} % of PJW, {:.3f} % of DJB'.format(aPJW, aDJB)
    print(msg, end='\n')
    # indexes in collision arrays
    aPJW = int(aPJW)
    aDJB = int(aDJB)
    # PJW hashtable filling
    if hashtablePJW[keyPJW] is not None:
        collisionPJW[aPJW] += 1
        findFlag = False
        # find semi-node to frequency inc
        for item in hashtablePJW[keyPJW]:
            if item[0] == word:
                findFlag = True
                item[1] += 1
                break
        if findFlag is False:
            # add new semi-node
            hashtablePJW[keyPJW].append([word, 1])
    else:
        usedSpacePJW += 1
        hashtablePJW[keyPJW] = [[word, 1]]

    # DJB hashtable filling
    if hashtableDJB[keyDJB] is not None:
        collisionDJB[aDJB] += 1
        findFlag = False
        # find semi-node to frequency inc
        for item in hashtableDJB[keyDJB]:
            if item[0] == word:
                findFlag = True
                item[1] += 1
                break
        if findFlag is False:
            # add new semi-node
            hashtableDJB[keyDJB].append([word, 1])
    else:
        usedSpaceDJB += 1
        hashtableDJB[keyDJB] = [[word, 1]]
# output in file
output = open('results2.csv', 'w')
output.write('a, collPJW, collDJB\n')
for i in range(0, M):
    strPJW = str(collisionPJW[i])
    strDJB = str(collisionDJB[i])
    output.write(str(i / 100) + ',' + strPJW + ',' + strDJB + '\n')
output.close()
