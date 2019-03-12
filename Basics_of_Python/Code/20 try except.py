# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:01:40 2019

@author: akshaf
"""

fname = input("Enter file name")
try:
    fhand = open(fname)
    fobj = open(fname,"r")
    for i in fobj:
        print(i)
except:
    print(fname,": File not found")
