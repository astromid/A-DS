# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:32:12 2016

@author: astro
"""


import numpy as np
import matplotlib.pyplot as plt
import time
import turtle
from turtle import left, right, forward


def HilbertIter(n, pic):
    start_time = time.time()

    # построение кривой Гильберта в терминах L-систем
    def Lsys_rules(s):
        s = s.replace('a', '-Bf+Afa+fB-')
        s = s.replace('b', '+Af-BfB-fA+')
        return s.lower()

    axiom = 'a'
    dxdy = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    length = 2**n - 1
    margin = 0.05 * length
    domain = [0 - margin, length + margin, 0 - margin, length + margin]
    s = axiom
    for i in np.arange(n):
        s = Lsys_rules(s)

    if pic:
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.axis(domain)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(r'$n = {:d}$'.format(n))
        plt.show()

        s = s.replace('a', '')
        s = s.replace('b', '')

        p = np.array([[0.0, 0.0]])
        p_plot, = plt.plot(p[:, 0], p[:, 1], color="black")

        for i, c in enumerate(s):
            if c == '+':
                dxdy = np.roll(dxdy, +1, axis=0)
            if c == '-':
                dxdy = np.roll(dxdy, -1, axis=0)
            if c == 'f':
                p = np.vstack([p, [p[-1, 0]+dxdy[0, 0], p[-1, 1]+dxdy[0, 1]]])
            p_plot.set_data(p[:, 0], p[:, 1])
            fig.canvas.draw()
    delta_time = time.time() - start_time
    return delta_time


def HilbertRec(n, pic):
    start_time = time.time()
    size = 10

    def hilbert(n, angle):
        if n == 0:
            return 0

        if pic:
            turtle.color('Blue')
            turtle.speed(0)
            right(angle)

        hilbert(n-1, -angle)
        if pic:
            forward(size)
            left(angle)
        hilbert(n-1, angle)
        if pic:
            forward(size)
        hilbert(n-1, angle)
        if pic:
            left(angle)
            forward(size)
        hilbert(n-1, -angle)
        if pic:
            right(angle)

    hilbert(n, 90)

    delta_time = time.time() - start_time
    if pic:
        turtle.exitonclick()
    return delta_time

output = open('results.txt', 'w')
for n in range(0, 10):
    time_iter = 0
    time_rec = 0
    for i in range(0, 100):
        time_iter += HilbertIter(n, False)
        time_rec += HilbertRec(n, False)
    time_iter /= 100
    time_rec /= 100
    output.write(str(n) + ' ' + str(time_iter) + ' ' + str(time_rec) + '\n')
    msg = 'N = {}, Iter: {}, Rec: {}'
    print(msg.format(n, time_iter, time_rec))
output.close()
