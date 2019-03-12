# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:18:39 2019

@author: akshaf
"""

import numpy as np
data1 = [[1,2,3,4],[5,6,7,8],["ab","c","d","d"]]
print("data1",data1)
type(data1)
a = np.array(data1)
a
type(a)  # This give numpy array
data1.__class__  # similar to type(data1) function
a.__class__  # similar to type(a) function
a.ndim # gives dimension of rows
a.shape # gives shape in the form of (row,column)
a.dtype # shows which all different datatypes are present in a

a1 = np.arange(15).reshape(3,5) # arrange will create a sequence and reshape will shape in (row,column) structure
a1
type(a1)
a1.ndim
a1.shape
a1.dtype

z= np.zeros((3,6))
z

a = np.arange(50)
a
a.ndim
a[0]
a[6] # 6th element
a[0:3] # first 3 elements
a[4:8] # 5th to 8th element
a[2:] # All elements that start from 2
a[:] # all elements from start to end
a[-3:] # last 3 ekements

a1 = np.arange(15).reshape(3,5)
a1
a1[0]
a1[1]
a1[2]
a1[1:]
a1[1][2]

