# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:58:21 2019

@author: akshaf
"""

# we use def keyword here to define a variable.

# Function has 2 parts
# 1. Fucntion definition
# 2. Function Call

#This is called as function definition:
def s(a,b):   # here a and b are formal parameters
    s1 = a + b
    return(s1)

#This is known as function call
s(1,2)

# No return type functions
def msg2():
    print("Munni badnaam hue darling tere liye")
    
msg2()

def msg3():
    print("Ye duniya..duniya pittal di.. duniya pittal di")
    print("baby doll main sone di.. baby doll main sone di")

msg3()


## Write a program to multiply 2 numbers
def mul():
    a= 5
    b = 6
    return(a*b)

m = mul()
m

# Nested function
def square(x):
    s = x*x
    return(s)

def cube(x):
    s = x*square(x)
    print(s)
cube(4)

# sum of 3 numbers
def sum(x,y,z):
    su = x+y+z
    return su
sum(1,2,3)

#avg of 3 numbers
def avg(a,b,c):
    s = (a+b+c)/3
    print(s)
avg(1,2,3)

# avg of 3 numbers and input from user
a,b,c = eval(input("Enter the 3 numbers"))
s = avg(a,b,c)
s

# we can have more than one return values in python.
# in such cases, pyhton return the value in the form of tuples.
# so to access it, we can either use one variable to get the output and then segregate OR we can select multiple variables.
# see example below. first we took tow variables to store sum and average independently.
# in the next example we stored the output in a single variable then used indexing to get a particular values.


def sumavg(a,b,c):
    s = a+b+c
    avg = s/3
    return s,avg

s,a = sumavg(1,2,3)
s,a

# we can also store teh above output in one variable.
s = sumavg(1,2,3)
s
s[0]
s[1]

# area and ircumference of circle
import math

def circle(r):
    area = math.pi*r*r
    circum = 2*math.pi*r
    print("Area of circle is",area,"Circumference of circle is",circum)
    
circle(4)

## Taking user input within the function

def triangle():
    a,b,c = eval(input("Enter the three sides of a traingle: "))
    s = (a+b+c)/2
    area = ((s-a)*(s-b)*(s-c))**0.5
    print("Area of the shape is:",area)

def circ():
    r = eval(input("Enter the radius of the circle: "))
    s = math.pi*r*r
    print("Area of circle is:",s)

def squr():
    l = eval(input("Enter the side of square : "))
    s = l * l
    print("Area of square:",s)
    
x = eval(input("Select from 1 to 4. select 1 - traingle, 2 - circle, 3 - Square: "))
if (x == 1):
    triangle()
elif(x == 2):
    circ()
elif(x==3):
    squr()
else:
    print("Enter correct value")

# Evenoddd
    
def evenodd(x):
    if(x%2 == 0):
        print(x,"is even")
    else:
        print(x,"is odd")
    
evenodd(4)

# factorial

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

inp = eval(input("Please enter the number: "))
factorial = factorial(inp)
print("Factorial of",inp,"is:",factorial)


########## Day 5 ########################

# square of int and float only. no negative numbers.
def squareOfInt(x):
    if(type(x) != float and type(x) != int):
        print("Invalid input")
    else:
        if(x<0):
            print("Value cant be negative")
        else:
            return x*x

squareOfInt(-3.4)
squareOfInt("as")

# passing function arguments by name 

def fun(a,b,c,d):
    result = a*b*c-d
    print(result)

fun(1,2,3,4)  # passing arguments without names
fun(a=1,b=2,c=3,d=4) # passing arguments with name 
fun(d=1,c=3,a=2,b=3) # passing arguments with name and different order

# Nesting of functions

def gm():
    print("Hello from gm")

def hello():
    gm()
    print("Hello from hello")

def welcome():
    hello()
    print("Hello from welcome")

welcome()

a*a*a

# write cube of number program by calling square of number program

def cube(x):
    result = squareOfInt(x)*x
    print(result)

cube(3)

# program to show the use of string argument in functions
# create a function to determine wehther each letter in the string is a vowel or alphabhet/constant

def vowel(str):
    vowel_count = 0
    vowel_set = ['a','e','i','o','u']
    for i in str:
        if i in vowel_set:
            vowel_count += 1
            print("The letter",i,"is a vowel")
        else:
            print("The letter",i,"is an alphabhet/constant")
    print("count of vowels in your string is",vowel_count)

def len_fun(str):
    len_count = 0
    for i in str:
        if i != ' ':
            len_count += 1
    return len_count

def inp_fun():
    choice = int(input("Enter your choice - 1 for vowel, 2 for length : "))
    mystr = input("Enter the String : ")
    if choice == 1:
        vowel(mystr)
    elif choice == 2:
        print("Length of string is",len_fun(mystr))
    else:
        print("Enter correct value")

def main_vowel_len():
    conti = "y"
    while conti == "y":
        inp_fun()
        conti = input("Do you wish to continue y/n : ")
    print("Thanks")

main_vowel_len()


# Reverse of number

# creating a reverse functiom
def reverse_func(num):
    reverse=0
    while num>0:
        remainder = num%10
        reverse =(reverse *10) + remainder
        num = num//10
    return reverse

reverse_func(345)

## palindrome
def palindrome_func(num):
    original=num
    rev=0
    while num!=0:
        rev=rev*10
        rev=rev+int(num%10)
        num=int(num/10)
    if original == rev:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
palindrome_func(789987)
palindrome_func(23)         

# creating an input function
def input_func():
    choice=int(input("enter your choice= 1: Reverse, 2: Palindrome: "))
    if choice==1:
        x=int(input("Enter the number whose reverse is to be calculated: "))
        print("The reverse of the number ", x,"is:", reverse_func(x))
    elif choice==2:
        x=int(input("Enter the number for which you want to check if it is Palindrome "))
        palindrome_func(x)
    else:
        print("Not a valid choice")

# main program calling the input function
def main_palindrome():
    cont = "yes"
    while(cont=="yes"):
        input_func()
        cont=input("Do you wish to continue: yes/no: ")
    print("Thanks")




