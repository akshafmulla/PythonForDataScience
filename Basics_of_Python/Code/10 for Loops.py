# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:54:42 2019

@author: akshaf
"""

#For Loops

for i in range(1,11,1):
    print(i, end=' ')

# FInd odd number
for i in range(1,11,2):
    print(i, end=' ')

#Print the number in sequence taken from user
    
n = eval(input("Enter number"))
for i in range(1,n+1,1):
    print(i, end = ' ' )
    
# Print sum of n different numbers taken from user

n = eval(input("Enter the number"))
sum = 0
for i in range(1,n+1,1):
    sum += i
    
print("Sum of number is",sum)

# Print sum of even numbers
n = eval(input("Enter the number"))
sum = 0
for i in range(2,n+1,2):
    sum += i
    
print("Sum of number is",sum)

# accept 10 diff numbers from user and add them

sum = 0
for i in range(1,11,1):
    n = int(input("enter the %d number" %i))
    sum = sum + n

print("sum of 10 different numbers",sum)



#################### Day 3 #######################

# accept n diff numbers from user and add them

sum = 0
n = int(input("Please enter how many numbers you want to add"))
 
for i in range(1,n+1,1):
    x = int(input("enter the %d number" %i))
    sum = sum + x

print("sum of",n,"different numbers is",sum)

# sum of even numbers entered by user

sumeven = 0
n = int(input("Please enter how many numbers you want to add"))
 
for i in range(1,n+1,1):
    x = int(input("enter the %d number" %i))
    if(x%2==0):
        sumeven = sumeven +x

print("sum of",n,"even numbers is",sumeven)

# sum of even and odd numbers entered by user

sumeven = 0
evencount = 0
sumodd = 0
oddcount = 0

n = int(input("Please enter how many numbers you want to add"))
 
for i in range(1,n+1,1):
    x = int(input("enter the %d number" %i))
    if(x%2==0):
        sumeven = sumeven +x
        evencount += 1
    else:
        sumodd = sumodd + x
        oddcount += 1

print("sum of",evencount,"even numbers is",sumeven)
print("sum of",oddcount,"even numbers is",sumodd)

# factorial of a number

fact = 1
n = int(input("Enter a number"))
for i in range(1,n+1,1):
    fact = fact * i
print("The factorial of",n,"is",fact)


# sum of multiple fatorial numbers

fact = 1
n = int(input("Enter a number"))

for i in range(1,n+1,1):
    for i in range(1,n+1,1):
        fact = fact * i
      

print("The factorial of",n,"is",fact)

# skip a number and continue execution for further number - use continue

for i in range(1,11,1):
    if(i==5):
        continue
    print(i)
    
# break code execution for a particular number

for i in range(1,11,1):
    if(i==8):
        break
    print(i)














