# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:15:00 2016

@author: astro

Generator for DNA code
"""

import numpy as np

alphabet = ['C', 'G', 'A', 'T']
N = 1000
data = ''
for i in range(0, N):
    index = np.random.choice(len(alphabet))
    data += alphabet[index]

output = open('dna.txt', 'w')
output.write(data)
output.close()