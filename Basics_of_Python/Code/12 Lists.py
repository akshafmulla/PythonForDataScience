# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:44:48 2019

@author: akshaf
"""


####### Indexing

# creating a list

a = [1,2,3,4]  # creating directly
b = list([1,2,3,4])  # using list function

## accessing a particular element

m = [1,2,3,4,5,6,7,8]
m
print("First element of List is",m[0])
print("last element is",m[7])
print("first three elements are",m[0:3])
print("last four elements of list are",m[4:8])
print("Element from 2nd to 5th are",m[1:5])
print("7th element is  ",m[6])

n = ["happy",['b','i','r','t','h','d','a','y']]
print("print app from nested list",n[0][1:4])
print("print birth from nested list",n[1][0:5])
print("print day from nested list",n[1][5:8])
print("print h from 1st element",n[0][0])

## deleting a particular element

##### options :
# del method
# pop method
# remove() method
# clear() method

# pop() method

l1 = [1,2,3,4,1]
l11 = l1.pop(2) # Here we are passing the index value inside the pop() method.
l1  # This will contain the remaining list.
l11 # This will contain the only element which is remaining.

# remove method

l2 = [1,2,3,4,5,1]
l2.remove(1)  # Here we are passing value inside the remove() method.
l2  # This will remove only the first occurance of the value in the list. 

# delete method
l3 = [1,2,3,4,5]

del l3[0]
l3

del l3[2:3]  # in del we can delete range which is not possible in pop
l3

# clear method
l4 = [1,2,3,4]
l4.clear()
l4

### operations on list

# add 2 list
a = [1,2,3]
b = [4,5,6]
c = a + b  ## Adding wont add the two list. It will concatenate
c

# sequence
d = a*3
d

e = [1,2,3]*3
e

# list in for loop
for i in a:
    print(i)

# append
a.append(43)
a

a = a + [23,45,6]
a

# find count of a value
a.count(43)

# sort
a.sort()
a

dir(a)

a.reverse()
a

# if we dont want our original list to be affected, use sorted() method

b = sorted(a)
a
b

# min and max
min(a)
max(a)

# copy a list

g = a
g

# copy in reverse form
h = g.copy()
h

# insert(position,value)
a.insert(5,87)
a

