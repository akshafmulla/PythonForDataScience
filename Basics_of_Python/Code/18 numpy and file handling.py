# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:44:08 2019

@author: a007
"""

# Friday

import numpy as np
x=np.random.random(10)
print(" x is ", x)
x1=np.random.random(10)+5
x1
y=np.random.random(10)
z=np.random.random(10)
a=np.array(zip(x,y,z))       # all x , y ,z will be b zipped inside a with np.array function
print("Zip Array of x, y,z is :", a)

a=np.array([[1,2,3],[4,5,6]])
print(" Array b is ", a)

z=np.zeros((2,1),dtype="int32")
print("\n the z matrix of zeros of single column is \n",z)

a=np.append(a,z,axis=1)
print("\n The array a after adding one column of zeros\n",a)

z1=np.zeros((2,2),dtype="int32")
print("\n The z matrix of zeros of two columns is\n",z1)

a=np.append(a,z1,axis=1)
print("\n the array a after adding two columns of zeros\n",a)

z2=np.zeros((2,6),dtype="int32")
print("\n the z2 matrix of zeros of two colimns is\n",z2)

a=np.append(a,z2,axis=0)
print("\n The array a after adding two rows of zeros\n",a)


# toprint list of odd numbers from given list
l1=[1,2,3,4]

def funlist(list_):   # passing parameter as list
    s=[]
    s=[i for i in list_ if (i%2)!=0]   # writing condition within list, output will b list
    list_=s
    print(list_)
funlist(l1)
    
def funl(list_):
    s1=[]
    for i in list_:
        if(i%2 != 0):
            s1[i] = i
        list_ = s1
    print(list_)
funl(l1)

l2=[3,4,6,9]
funlist(l2)


#create a list & pass same list to func 1 n func 2
# sum  of odd nos, n sum of even nos


def sumodd(listt):
    s=[]
    s=[i for i in listt if (i%2)!=0]    # s=s=[i for i in listt if (i%2)!=0] 
    listt=s                              #  print("the sum of list of odd elements is",sum(s))
    print(listt)
    print(sum(listt))
    
def sumeven(listt):
    s=[]
    s=[i for i in listt if (i%2)==0]
    listt=s
    print(listt)
    print(sum(listt))
    
L=[1,2,3,4,5,6,7,8,9,10]
print("sum of odd numbers is ",sumodd(L))
print("sum of odd numbers is ",sumeven(L))



        
# accepting array of list from usercreating odd  element array list from entered list
import numpy as np
def funarray(arr):
    a=np.array([arr])    # user will give d 
    a=np.array([a for a in arr if np.mod(a,2)!=0])      # inbuilt np.mod method
    print("odd element array created from given list",a)
arr1=np.array([1,2,3,4])
funarray(arr1)




# FILE HANDLING

fobj = open("a.txt", "w")
print("Name of the file : ", fobj.name)
fobj.write("Hello welcome to file")
fobj.close()   # closed opened file

fobj = open("a.txt","w")
print(fobj.name)
fobj.write("akjdhakdhkahdkahskjdhauidgabdkjahdkjahdukhaskjdhaskjdhuahduahdakj")
fobj.close()

fr=open("a.txt","r")
str=fr.read()
print("current position",fr.tell())
fr.seek(0,0)
print("current position",fr.tell())
str1=fr.read(5)
print(" the contents of file are: ",str)
print("First five characters of file are:",str1)
print("current position",fr.tell())
s=fr.readline()
print("the readed line of file are:",s)
fr.close()

f1=open("a.txt","r")
t1=f1.read()
for s in t1:
    print(s,end=" ")
f1.close()

f1=open("a.txt","r")
t1=f1.read()
for s in t1:
    word=s.split(" ")
    print(word,end=" ")
f1.close()

f1=open("a.txt","r")
t1=f1.read()
word=t1.split(" ")
print(word,end=" ")
print("\n First wordis",word[0])
for i in word:
    print(i)
f1.close()


f1=open("a.txt","r")
t1=f1.read()
f1.close()
print("original contents of the file are: ", t1)

fobj=open("a.txt","a")
fobj.write("\n Here is some additional text added at the end!")
fobj.close()

fr=open("a.txt","r")
text=fr.read()
fr.close()
print("content appended contents in the file are",text)

fobj = open("a.txt", "w")          
print("Name of the file : ", fobj.name)
print("mode of the file:",fobj.mode)
fobj.write("Hello welcome to file\n")
fobj.write("welcome to python\n")
fobj.write("Intro to python")
fobj.close()

fobj=open("a.txt","r")
f=fobj.readlines()          # readlines will 
print("Contents are",f)
fobj.seek(0,0)
f1=fobj.readline()
print("\n First line is \n ", f1)
f2=fobj.readline()
print("\n Second line is \n", f2)
fobj.close()   # closed opened file

fr=open("a.txt","r")
f=fobj.read()
print("\n Contents of a1.txt file are:\n",f)
fobj.close()




fobj = open("a.txt", "w")          
print("Name of the file : ", fobj.name)
print("mode of the file:",fobj.mode)
fobj.write("Hello welcome to file\n")
fobj.write("welcome to python\n")
fobj.write("Intro to python")
fobj.close()
fobj=open("a1.txt","w")
lines=["hello, welcome to  python", "another line of text","thirs line of text"]
fobj.writelines(lines)
fobj.close()
fobj=open("a1.txt","r")
f=fobj.read()
print("\n Contents of a1.txt file are:\n",f)
fobj.close()


