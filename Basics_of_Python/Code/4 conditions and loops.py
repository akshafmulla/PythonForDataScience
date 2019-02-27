# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:48:42 2019

@author: akshaf
"""

# Simple if-else
a,b = eval(input("Enter the numbers"))

if a>b :
    print("a is greater than b")
else:
    print("a is less than b")

# if a==b: print("a is equal to b") else: print("a is not equal to b")   Single line if else wont work here.


a,b,c = eval(input("Enter the numbers"))

#### Nested If

if a>b:
    if a>c:
        print("a is greatest",a)
if b>a:
    if b>c:
        print("b is greatest",b)
if c>a:
    if c>b:
        print("c is greatest",c)


### using nested if-else

if a>b & a>c:
    print("a is the greatest",a)
elif b>a & b>c:
    print("b is the greatest",b)
else:
    print("c is the greatest",c)

###  Mod code
a,b = eval(input("Enter the numbers"))
if a%b == 0 :
    print("remainder is zero")
else:
    print("remainder is non zero")















