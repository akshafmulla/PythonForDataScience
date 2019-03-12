# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:16:13 2019

@author: akshaf
"""

# count number of comma and spaces in a file

count_space = 0
count_comma = 0
with open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/commaandspace.txt","r") as rf:
    text = rf.read()
    for x in text:
        if(x == " "):
            count_space += 1
        if(x == ","):
            count_comma += 1
    print("The count of spaces in file is:",count_space,"and the count of commas in file is:",count_comma)