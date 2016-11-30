# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:57:56 2016

@author: astro
"""
import numpy as np


class skipList:
    # d - skip parameter
    def __init__(self, d=0):
        self.first = None
        self.last = None
        self.lenght = 0
        self.d = d
        # embedded comparsion counter
        self.count = 0

    class node:
        def __init__(self, word=None, freq=1, next_1=None, next_d=None,
                     prev_1=None, prev_d=None):
            self.word = word
            self.freq = freq
            self.next_1 = next_1
            self.next_d = next_d
            self.prev_1 = prev_1
            self.prev_d = prev_d

    # find will return index & node with value x, or with min value greater
    # than x, or the last node, if x is greater than last value in the list
    def find(self, x):
        index = 0
        c_node = self.first
        word = c_node.word
        self.count += 1
        while word < x:
            self.count += 1
            # if d-step is possible
            if c_node.next_d is not None:
                p_node = c_node
                c_node = p_node.next_d
                index += (self.d + 1)
                word = c_node.word
                # if d-step was reduntant
                self.count += 1
                if word > x:
                    c_node = p_node.next_1
                    index -= self.d
                    word = c_node.word
            else:
                if c_node.next_1 is not None:
                    p_node = c_node
                    c_node = p_node.next_1
                    index += 1
                    word = c_node.word
                else:
                    return (index, c_node)
        return (index, c_node)

    def add(self, x):
        # counter value
        count_state = self.count
        # 1. list is empty
        if self.first is None:
            self.first = self.last = self.node(x)
            self.lenght += 1
        else:
            index, target_node = self.find(x)
            # create new node with word x
            new_node = self.node(x)
            self.lenght += 1
            # 2. word already exist in the list
            self.count += 1
            if target_node.word == x:
                target_node.freq += 1
                # length correction
                self.lenght -= 1
            # 3. new node is new first item
            elif target_node is self.first:
                new_node.next_1 = target_node
                target_node.prev_1 = new_node
                self.first = new_node
            # 4. new node is new last item
            elif target_node is self.last:
                target_node.next_1 = new_node
                new_node.prev_1 = target_node
                self.last = new_node
            # 5. new node between existing nodes
            else:
                new_node.next_1 = target_node
                new_node.prev_1 = target_node.prev_1
                new_node.prev_1.next_1 = new_node
                target_node.prev_1 = new_node
            # determine boundaries for balancer:
            if target_node.prev_d is not None:
                start_node = target_node.prev_d
            else:
                start_node = self.first
            self.balancer(start_node, target_node)
        return self.count - count_state

    # just print all list
    def display10top(self):
        start_node = self.first
        top10words = ['']*10
        top10freq = [0]*10
        while start_node is not None:
            word = start_node.word
            freq = start_node.freq
            if freq > np.min(top10freq):
                index = np.argmin(top10freq)
                top10freq[index] = freq
                top10words[index] = word
            start_node = start_node.next_1
        print('Top-10 words:', end='\n')
        for i in range(0, 10):
            freq = top10freq[i] / self.lenght
            print(top10words[i] + ', freq: ' + str(freq), end='\n')

    # estabilish all d-hop links
    def balancer(self, start_node, target_node):
        while start_node is not target_node:
            temp_node = start_node
            break_flag = False
            for i in range(0, self.d+1):
                if temp_node.next_1 is not None:
                    temp_node = temp_node.next_1
                else:
                    break_flag = True
                    break
            if break_flag:
                start_node.next_d = None
            else:
                start_node.next_d = temp_node
                temp_node.prev_d = start_node
            start_node = start_node.next_1
# create different lists
lst0 = skipList()
lst1 = skipList(1)
lst3 = skipList(3)
lst5 = skipList(5)

textfile = open('war-and-peace.txt', 'r')
words = [line.split() for line in textfile]
textfile.close()
# flat words list
words = [word for line in words for word in line]
# data arrays for every skipList
N = len(words)
data_list_d0 = np.zeros(N)
data_list_d1 = np.zeros(N)
data_list_d3 = np.zeros(N)
data_list_d5 = np.zeros(N)
idx = 0
for word in words:
    idx += 1
    if not(idx % 2000):
        percent = (idx / N) * 100
        msg = 'Processing {:.3f} %'.format(percent)
        print(msg, end='\n')
    index = lst0.lenght
    d0 = lst0.add(word)
    d1 = lst1.add(word)
    d3 = lst3.add(word)
    d5 = lst5.add(word)
    data_list_d0[index] = d0
    data_list_d1[index] = d1
    data_list_d3[index] = d3
    data_list_d5[index] = d5
# output
print('Writing csv', end='\n')
output = open('results.csv', 'w')
output.write('length, d0, d1, d3, d5\n')
for i in range(0, lst0.lenght):
    d0 = data_list_d0[i]
    d1 = data_list_d1[i]
    d3 = data_list_d3[i]
    d5 = data_list_d5[i]
    output.write(str(i)+','+str(d0)+','+str(d1)+','+str(d3)+','+str(d5)+'\n')
output.close()
print('Complete', end='\n')
lst0.display10top()
