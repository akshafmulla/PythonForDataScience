# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:52:45 2019

@author: akshaf
"""

c1,c2,c3,c4,c5 = eval(input("Enter Marks"))

counter = 0
if(c1<40):
    counter += 1
if(c2<40):
    counter += 1
if(c3<40):
    counter += 1
if(c4<40):
    counter += 1
if(c5<40):
    counter += 1    
    
total_marks = c1 + c2 + c3 + c4 + c5
percentage_scored = total_marks/5

print("Percentage Scored", percentage_scored)
print("Total Marks Scored",total_marks)


if(counter == 0):
    if(percentage_scored > 75):
        print("Distinction")
    elif(percentage_scored >= 60):
        print("First Class")
    elif(percentage_scored >= 50):
        print("Second Class")
    elif(percentage_scored >= 40):
        print("Pass Class")
elif(counter <= 2):
    print("ATKT")
else:
    print("Fail")