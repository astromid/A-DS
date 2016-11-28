# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:57:56 2016

@author: astro
"""


class skipList:
    # d - skip parameter
    def __init__(self, d=0):
        self.first = None
        self.last = None
        self.lenght = 0
        self.d = d
        # embedded operation counter
        self.count = 0

    class node:
        def __init__(self, value=None, next=None, next_d=None):
            self.value = value
            self.next = next
            self.next_d = next_d

    # find will return index & node with value x, or with min value greater
    # then x, or the last node, if x is greater then max value in the list
    def find(self, x):
        index = 0
        c_node = self.first
        value = c_node.value
        self.count += 1
        while(value < x):
            self.count += 1
            # if d-step is possible
            if(c_node.next_d != None):
                p_node = c_node
                c_node = p_node.next_d
                index += (self.d + 1)
                value = c_node.value
                # if d-step was reduntant
                self.count += 1
                if(value > x):
                    c_node = p_node.next
                    index -= self.d
                    value = c_node.value
            else:
                if(c_node.next != None):
                    p_node = c_node
                    c_node = p_node.next
                    index += 1
                    value = c_node.value
                else:
                    return (index, c_node)
        return (index, c_node)

    def add(self, x):
        if self.first is None:
            self.first = self.last = self.node(x, None)
        else:
            self.last.next = self.last.next_d = self.last = self.node(x, None)
            index, target_node = self.find(x)
            
            
lst = skipList()
lst.add(0)
lst.add(1)
lst.add(3)
lst.add(5)
lst.add(7)
