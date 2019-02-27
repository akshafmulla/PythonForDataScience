# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:23:38 2019

@author: akshaf
"""

name = "Akshaf"

len(name)

print(name)

print(name[2])

print(name[-3])

print(name[1:3])  # we have to give an extra number at the end. because it will tell python where to stop and not till where to print.

type(name)

name.upper()
name.lower()
name.title()

firstname = "Akshaf"
lastname = "Mulla"

Fullname = firstname +" "+ lastname
print(Fullname)

s = firstname*3
print(s)

name = Fullname+s

n = name.replace("kshaf","KSHAF")
print(n)

beforeSplitName = "Akshaf Irfan Mulla"

afterSplitArray = beforeSplitName.split(" ")  # This will give an array.
afterSplitArray[2]
print(afterSplitArray)

s,s1,s2 = beforeSplitName.split(" ")  # This will give seperate variables
print(s,s1,s2)
s[2]

help(str.find)

beforeSplitName.find("f")

help(str.count)
beforeSplitName.count("f")

s.join(s1)

n = input("Enter String")
f = n.find('r')
print(f)
if f>=0:
    print("r is found in string with index number",f)
else:
    print("r is found in string with index number")

n[12]

## Finding a string in a string
address = "mumbai@uct.ac.in sat 2019"
print("original string is:",address)
atpos = address.find("@")
print("Position of @ character is",atpos)
sppos  =address.find(' ' ,atpos)
print("position of blank space after @",sppos)
host = address[atpos+1:sppos]
print("Hostname is", host)

## replace a string

old = "Hello World"
print("Old String")

new = old.replace("World","to this World")
print("The new string is",new)

camels = 42
s = "I have spotted %d camels" %camels
print(s)
