# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:58:28 2019

@author: akshaf
"""

# Dictionary is key:value pair.
# We can get the value based on key.

# creating a dictionary

d = dict()  # empty dictionary
d
type(d)

d1 = {'name':'Akshaf Mulla','age':28,'Job':'Fukat'}
d1
d1['name']

d2 = {'Employee1':['Akshaf',25,'Fukat'],'Employee2':['Mulla',28,'Kaam Dhandha'],'Employee3':['Irfan',26,'Retired']}
d2['Employee1']

del d2['Employee1']
d2

for i in d2.keys():
    print(d2[i])

for i in d2:
    print(i)

# pop usually works with index number. Here it works with key values. In the pop method we have to provide key value

squares = {1:1,2:4,3:9,4:16,5:25}
squares.pop(3)
squares  # value of key 3 is removed instead of value of 4.
squares.popitem()  # this will delete the last item from the dictionalry
squares

score = {'marks' : 256, 'percentage' : 82}
student = {'name' : 'Akshaf', ' Roll Number' : 14}

# We cannot add two tuples. we can add a particular key but cannot add two tuples.

student.update(score)  # wont work
student


