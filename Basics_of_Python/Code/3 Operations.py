# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:16:38 2019

@author: akshaf
"""

# using input function
print("Apna time aaega")
n = input("Enter your name")
print("Your name is",n)


# adding two numbers
a = input("Enter first number")
b = input("Enter second number")
c = a+b
print(c) # This will result in string answer. Hence we need to typecast input to int.

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = a+b
print("sum of a and b is ",c)

#mean value of a and b is:
print("mean of a and b is ",(a+b)/2)

# we can use eval function instead of 2 input functions
a,b = eval(input("enter two numbers"))
sum = a+b
sub = a-b
mul = a*b
div = a/b
mod = a%b
print("sum is ",sum)
print("sub is ",sub)
print("mul is ",mul)
print("div is ",div)
print("mod is ",mod)

























