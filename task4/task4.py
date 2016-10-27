# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:32:12 2016

@author: astro
"""


import matplotlib
import numpy as np
import matplotlb.pyplot as plt


def rules(s):
    s = s.replace('a', '-Bf+Afa+fB-')
    s = s.replace('b', '+Af-BfB-fA+')
    return s.lower()


axiom = 'a'
    