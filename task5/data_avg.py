#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:45:46 2016

@author: ys-budakyan
"""

import numpy as np


batch = 125
datafile = open('results.csv', 'r')
data = [line.split(',') for line in datafile]
datafile.close()
d0 = []
d1 = []
d3 = []
d5 = []
for i in range(1, len(data)):
    line = data[i]
    d0.append(float(line[1]))
    d1.append(float(line[2]))
    d3.append(float(line[3]))
    d5.append(float(line[4]))

d0_avg = []
d1_avg = []
d3_avg = []
d5_avg = []
length = []
for i in range(0, int(len(d0)/batch)):
    avg_d0 = 0
    avg_d1 = 0
    avg_d3 = 0
    avg_d5 = 0
    for j in range(0, batch):
        avg_d0 += d0[i*batch + j]
        avg_d1 += d1[i*batch + j]
        avg_d3 += d3[i*batch + j]
        avg_d5 += d5[i*batch + j]
    avg_d0 /= batch
    avg_d1 /= batch
    avg_d3 /= batch
    avg_d5 /= batch
    d0_avg.append(avg_d0)
    d1_avg.append(avg_d1)
    d3_avg.append(avg_d3)
    d5_avg.append(avg_d5)
    length.append((i+1)*batch)
output = open('results_avg.csv', 'w')
output.write('length_avg, d0_avg, d1_avg, d3_avg, d5_avg\n')
for i in range(0, len(d0_avg)):
    l = length[i]
    d00 = d0_avg[i]
    d01 = d1_avg[i]
    d03 = d3_avg[i]
    d05 = d5_avg[i]
    msg = str(l)+','+str(d00)+','+str(d01)+','+str(d03)+','+str(d05)+'\n'
    output.write(msg)
output.close()
