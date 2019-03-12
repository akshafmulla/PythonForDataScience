# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:32:41 2019

@author: akshaf
"""
import numpy as np

# Create a two dimensional array with two rows four columns as x
x1 = [[1,2,3,4],[5,6,7,8]]
x = np.array(x1)
x

# Display type of array by two different methods
type(x)
x.__class__

# Display dimension of array
x.ndim

# Display size of array in terms of row and column
x.shape

# Display data type of 2D array created
x.dtype

# Append 4 zeros to current Array row wise and store it into n1 and display n1
n1 = np.append(x,[[0,0,0,0]],axis = 0)
n1

# Append 2 columns of zeros to current array and store it into n2 and display n2
n = np.zeros((3,2),dtype = np.int32)
n
n2 = np.append(n1,n,axis = 1)
n2

# Create a matrix of zeros with 5 rows and 5 columns
m = np.zeros((5,5))
m

# Concatenate n1 and n2 to n3 and display n3
n3 = np.append(n1,n2,axis = 1)
n3

# Create array of 50 elements with values from 0 to 49 and reshape it into rows and cols
a1 = np.arange(50).reshape(10,5)
a1

# Replace 7 to 11 element of array to 15
a1[1][2:5] = 15
a1[2][0:2] = 15
a1

# Create a array a1 of 3 rows with 5 elements in each row
a2 = np.arange(15).reshape(3,5)
a2

# Display 3rd row
a2[2]

# Display first row
a2[0]

# Display First two columns
a2[:,0:2]

# Display last two columns
a2[:,3:]

# Display middle column
a2[:,2]

# first and second row with first 2 col
a2[0:2,0:2]

#transpose of a2
a2.T

# array with random values with 6r and 3c
arr = np.random.randn(6,3)+9
arr

# absolute of array
ab=np.abs(arr)
ab

# square root
sq1 = np.sqrt(a2)
sq1

# exponential
ex = np.exp(a2)
ex

# sum
sm=np.sum(a2)
sm

#std deviation
sd=np.std(a2)
sd

# mean
mn=np.mean(a2)
mn

# square
squ=np.square(a1)
squ

# sin
sin = np.sin(a2)
sin

# cos
cos = np.cos(a2)
cos

# tan
tan = np.tan(a2)
tan

# log
log = np.log10(a2) # number should be non zero

#Arithmetic operations

# operations work index wise like it works in R.

x =np.arange(8).reshape(2,4)
x1 = np.arange(8).reshape(2,4)
d = [[9,10,11,12],[13,14,15,16]]
x2 = np.array(d)
x2

x
x1
x2

add = np.add(x1,x2) 
add

sub = np.subtract(x1,x2)
sub

mul = np.multiply(x1,x2)
mul

div = np.divide(x1,x2)
div

power = np.power(x1,x2)
power

mod = np.mod(x1,x2)
mod

maxx = np.maximum(x1,x2)
maxx

minn = np.minimum(x1,x2)
minn

greater_eq = np.greater_equal(x1,x2)
greater_eq

greater = np.greater(x1,x2)
greater

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

logicalAND = np.logical_and(l1,l2)
logicalAND

logicalOR = np.logical_or(l1,l2)
logicalOR

logicalNOT = np.logical_not(l1)
logicalNOT

logicalXOR = np.logical_xor(l1,l2)
logicalXOR
