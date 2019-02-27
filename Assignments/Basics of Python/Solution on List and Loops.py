# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 02:01:45 2019

@author: akshaf
"""


## Assignment on String functions
## 1.	Create first as string
first = "Akshaf"

## 2.	Create middle as string
middle = "Irfan"

## 3.	Create last as string
last = "Mulla"

## 4.	Combine first, middle and last in name string
name = first + " " + middle + " " + last
name

## 5.	Display First character of name string
name[0]

## 6.	Display last character of name string by two methods (+ve and –ve indexing)
len(name)
print("last charater(+ve) is",name[17])
print("last charater(-ve) is",name[-1])

## 7.	Display First three characters of name string
name[0:3]

## 8.	Display 3rd to 6th character of the string name
name[2:6]

## 9.	Display last three characters of the string name by using negative indexing
name[-3:]

## 10.	Display length of name string
len(name)

## 11.	Display type of name string
type(name)

## 12.	Display id of name var
id(name)

## 13.	Display name string in small case
name.lower()

## 14.	Display name string in upper case
name.upper()

## 15.	Display name string in capital or proper or title case
dir(name)
name.title()
help(name.title)

## 16.	Repeat last string 5 times and store into new variable
last_3 = last*3
print(last_3)

## 17.	Find length of new variable
len(last_3)

## 18.	Combine name and new into name1 var, Display name1
name1 = name + " " + last_3
name1

## 19.	Replace last string word with abc in name1 var
name1.replace("Mulla","abc")

## 20.	Print index number of any character & print its index value
name1[14]
name1.find('u')

## 21.	Display occurrence of k character in name1
counter = 0
index=0
for i in name:
    index += 1
    if i == 'a':
        counter += 1
        print(index - 1)
    
print("count of k is",counter)


## 22.	Split name string & display each splited value by List method
new_name = name.split()
print(new_name)

## 23.	Split name string by assigning three var & print each varaible
new_name1,new_name2,new_name3 = name.split()
print(new_name1,new_name2,new_name3)

## 24.	Create a string with leading blank spaces and trailing blank spaces
spaces = " akshaf "

## 25.	Remove leading and trailing blank spaces of the string & print string (hint strip function)
spaces.strip(" ")

## 26.	Check whether name string is in upper case or not ( hint isupper)
name.isupper()

## 27.	Check whether name string is in lower case or not ( hint islower)
name.islower()

## 28.	Check whether name string is in proper case or not ( hint istitle)
name.istitle()

## 29.	Join hello string to each character of last string ( hint join)
print("Hello", last)

## 30.	Display help of join function of string (hint help(str.capitalize))
help(name.join)
help(str.join)

## 31.	Display All methods which can be used with string variable ( Hint on python prompt dir(name))
dir(name)
dir(str)

