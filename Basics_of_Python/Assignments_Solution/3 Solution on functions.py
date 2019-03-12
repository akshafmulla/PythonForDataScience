# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:16:12 2019

@author: akshaf
"""
import math

# 1. funtion to print area and perimeter of rectangle

def areaperm():
    l,b = eval(input("Enter length and breadth of rectangle: "))
    area = l*b
    perimeter = 2*(l+b)
    print("Area of rectangle is",area,"and perimeter of rectangle is",perimeter)

areaperm()

# 2. sum,sub,mul,div

def arithmeticOper():
    a,b = eval(input("Enter two numbers: "))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div

a,s,m,d = arithmeticOper()
print("Sum is:",a,"subtraction is:",s,"Multiplication is:",m,"Division is:",d )

# 3.

def arearectangle():
    l,b = eval(input("Enter the length and breadth of a rectangle: "))
    area = l*b
    print("Area of rectangle is",area) 
    
def areacirc():
    r = eval(input("Enter the radius of the circle: "))
    area = math.pi*r*r
    print("Area of circle is:",area)

def volSphere():
    r = eval(input("Enter the radius of sphere: "))
    volume = (4/3)*math.pi*r*r*r
    print("Volume of sphere is:",volume)

def perimetereRectangle():
    l,b = eval(input("Enter the radius of sphere: "))
    perimeter = 2*(l+b)
    print("Perimeter of rectangle is:",perimeter)

def circumCircle():
    r = eval(input("Enter the radius of sphere: "))
    circumference = 2*math.pi*r
    print("circumference of Circle is:",circumference)

def areatriangle():
    a,b,c = eval(input("Enter the three sides of a traingle: "))
    s = (a+b+c)/2
    area = ((s-a)*(s-b)*(s-c))**0.5
    print("Area of the shape is:",area)
    
x = eval(input("Select from 1 to 6. select 1 - rectangle, 2 - circle, 3 - Sphere, 4 - Rectangle perimeter, 5 - Circle circum, 6 - Area rectangle: "))
if (x == 1):
    arearectangle()
elif(x == 2):
    areacirc()
elif(x==3):
    volSphere()
elif(x==4):
    perimetereRectangle()
elif(x==5):
    circumCircle()
elif(x==6):
    arearectangle()
else:
    print("Enter correct value")

# 4 simple and compund interest
    
def simpInterest():
    p = eval(input("Please enter principal amount : "))
    r = eval(input("Please enter ROI : "))
    t = eval(input("Please enter time in years : "))
    r = r/100
    i = p*r*t
    print("Simple interest for Principal amount",p,"with rate of interest of",r," for",t,"years is:",i)
    
simpInterest()

def compoundInterest():
    p = eval(input("Please enter principal amount : "))
    r = eval(input("Please enter ROI : "))
    t = eval(input("Please enter time in years : "))
    n = eval(input("Please enter compound computation of interest based on quaterly tenure : "))
    r = r/100
    nt = n*t 
    a = p*(1+(r/n))**nt
    i = a-p
    print("Compound interest for Principal amount",p,"with rate of interest of",r," for",t,"years and compounded for",n,"quarters is:",i)
    
compoundInterest()  

# 5 number divisible by 5,7 or both

def div5and7():
    n = eval(input("Please enter the number : "))
    if(n%5==0 and n%7==0):
        print(n,"is divisble by 5 and 7 both")
    elif(n%5 == 0):
        print(n,"is divisble by 5")
    elif(n%7 == 0):
        print(n,"is divisble by 7")
    else:
        print(n,"is neither divisble by 5 nor with 7")

div5and7()


# 6 table of a number

def table():
    number = eval(input("Please enter the number: "))
    for i in range(1,11,1):
        tableOfNumber = number*i
        print(number,"*",i,"=",tableOfNumber)

table()

# 7 sum of even numbers

def sumOfEven():
    sumi = 0
    n = eval(input("Please enter the number : "))
    for i in range(1,n+1,1):
        if(i%2 == 0):
            sumi += i
    print("Sum of Even numbers from 1 to",n,"is :",sumi)

sumOfEven()
            
# 8 number is odd or even
def oddOrEven():
    n = eval(input("Please enter the number : "))
    if(n%2 == 0):
        print(n,"is Even")
    else:
        print(n,"is odd")
        
oddOrEven()        
        
# 9 Write a fun to accept number of subjects value through function, accept n subjects marks from user 
# calculate total and percentage and accordignly grade and print the same

def marks():
    sum1 = 0
    percentage = 0
    count = 0
    
    subject = int(eval(input("Enter the number of subjects:")))
    for i in (1, subject+1,1):
        n = int(input("Please enter marks: "))
        if(n >= 0):
            sum1 += n
            count += 100
        else:
            print("Value cannot be less than 0")
            break
        print(sum1)
        percentage = (sum1*100)/(count)
    if(percentage >= 90):
        print("Student secured A+ Grade with",percentage,"%")
    elif(percentage >= 75):
        print("Student secured Distinction Grade with",percentage,"%")
    elif(percentage >= 60):
        print("Student secured First Class Grade with",percentage,"%")
    elif(percentage >= 40):
        print("Student secured Pass Class Grade with",percentage,"%")
    else:
        print("Student failed with",percentage,"%")
            

marks()


# 10 Create divide function which will have divisor and divident 2 params, 
# it should return quotient and remainder and print both, 
# by checking remainder print whether both numbers are divisible or not
    
def divide():
    dividend = eval(input("Please enter the dividedend : "))
    divisor  = eval(input("Please enter the divisor: "))
    quotient = math.floor(dividend/divisor)
    remainder = dividend%divisor
    print("The division of",dividend,"and",divisor,"resulted in quotient of",quotient,"and remainder of",remainder)
    
    if(remainder == 0):
        print("Both numbers are divisible")
    else:
        print("Both numbers are not divisible")

divide()
    
    