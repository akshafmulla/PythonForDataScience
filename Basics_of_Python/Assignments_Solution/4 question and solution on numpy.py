# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:59:55 2019

@author: akshaf
"""

# add in this for function less, less_equal,equal,not_equal,
#logical_or,logical_xor
import numpy as np

x =np.arange(8).reshape(2,4)
x1 = np.arange(8).reshape(2,4)
d = [[9,10,11,12],[13,14,15,16]]
x2 = np.array(d)
x2

x
x1
x2

less = np.less(x1,x2) 
less

less_eq = np.less_equal(x1,x2)
less_eq

equal = np.equal(x1,x2)
equal

not_eq = np.not_equal(x1,x2)
not_eq


# Logical operations
l1 = [True,False,False,True]
l2 = [True,True,False,False]

logicalOR = np.logical_or(l1,l2)
logicalOR

logicalXOR = np.logical_xor(l1,l2)
logicalXOR