# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:29:06 2019

@author: akshaf
"""

## While Loops


# sum the numbers and end it if it is negative

number = 0
sum = 0

print("Enter numbers to add, negative number to end.")

while True:
    number = eval(input("Enter the number: "))
    if number < 0:
        break
    sum += number
print("The total is",sum)


# billing system where you keep adding the quatities until you select yes. when no is selected, program should stop

total = 0
choice = "yes"

while(choice == "yes" or choice == "y" or choice == "Y"):
    rate = eval(input("Enter the rate: "))
    quantity = eval(input("Enter the quantity: "))
    total += (rate * quantity)
    choice = input("wish to continue yes/no: ")
print("Your total bill is:",total)


















