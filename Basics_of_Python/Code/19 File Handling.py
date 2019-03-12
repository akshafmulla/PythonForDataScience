# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:02:51 2019

@author: akshaf
"""

import sys

# using for loops
f=input("Enter filename with extension which u want to open : ")
fr=open(f,"r")
print("opening  file",fr.name,"for reading")
for line in fr:
    sys.stdout.write(line)
fr.close()
print("\n File ",f,"sucessfully reading completed")

# using while loops
f = input("Enter filename with extenion which you want to open : ")
fr = open(f,"r")
print("Opening file",fr.name,"for reading")
line = fr.readline()
while(line != ""):
    sys.stdout.write(line)
    line = fr.readline()
fr.close()
print("\nFile",f,"successfully reading completed")

import os
f = open('a.txt')
os.path.realpath(f.name)

##### Job file read ####

fr = open("job.txt","r")
line = fr.readline()
for line in fr:
    print(line)
    name,job,income = line.split(",")
    last,first = name.split(" ")
    income = int(income)
    income = income + 1000
    print("First Name",first)
    print("Last Name",last)
    print("Incremented income is",income)
fr.close()


## copying from one file to another and updating the copied the new file

fr=open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/job.txt","r")  
fw=open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","w")
line = fr.readline()
print(line)
fw.write(line+"\n")
fw.close()
#del str
for line in fr:
    print(line)
    name,job,income = line.split(",")
    last,first = name.split(" ")
    income = int(income)
    income = income + 1000
    print("First Name",first)
    print("Last Name",last)
    print("Incremented income is",income)
    fw = open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","a")
    fw.tell()
    s = name + "," + job + "," + str(income) +"\n"
    fw.write(s)
    print(s)
    fw.close()
fr.close()


#copying from one file to another using with keyword

with open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/job.txt","r") as rf:
    with open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","w") as wf:
        for line in rf:
            wf.write(line)

#copying from one file to another using with keyword and adding 1000 to income

with open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/job.txt","r") as rf:
    with open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","w") as wf:
        for line in rf:
            print(line,end="")
            name,job,income = line.split(",")
            print(income)
            income = int(income)
            income += 1000
            s = name +", "+ job+ ", " + str(income)+ "\n"
            wf.write(s)


#count number of lines in the files 
fr = open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","r")
text = fr.read()
print("Contents of file are",text)
fobj = open("D:/Study/Data Science/Imarticus/4 Python/Codes/Files/Newjob.txt","r")
count = 0
for i in fobj:
    count += 1
print("number of lines in a file",count)
fr.close()









