# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:33:07 2019

@author: akshaf
"""

# Tuple is similar to List, except it is immutable i.e. once created, we cannot modify it.
# Secondly, we can traverse tuple in reverse order.

m = (1,2,3,4)
type(m)
m

m2 = ("mouse",[1,2,3,4],(1,2,4))
m2
type(m2)

a,b,c = m2
a
b
c

t = 2,3
type(t)
t

m3 = m + m2
m3

m3 = m3 + [1,2]  # This is error

m[0]
m[-1]
m[1:3]
m2[0][3]
m2[0][2:]
l = [1,2,3,"pp",78.9]
t2 = tuple(l)
t2

for i in t2:
    print(i, end = ' ')

1 in t2
t2.count(2)

sum(m)
m

min(m)
max(m)
len(m)
sorted(m)
reversed(m)  # reverse not present in tuple

#convert list to tuple
a = [1,2,3,4]
k = tuple(a)
type(k)
