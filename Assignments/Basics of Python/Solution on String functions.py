# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:41:31 2019

@author: akshaf
"""

# Assignment

# 1. Write a python program to accept n different numbers from user & print following data
sumeven = 0
sumodd = 0
sum3 = 0
sum5and7 = 0
evenindex = 0
oddindex = 0
poscount = 0
negcount = 0
zerocount = 0

n = int(input("Please enter the count of numbers: "))

for i in range(1,n+1,1):
    x = int(input("Please enter the number: "))
    if(x%2 == 0):               # a.	sum of even numbers from n different nos
        sumeven += x
        evenindex += 1          # e.	count how many are even numbers
    if(x%2 !=0):                # b.	sum of odd numbers from n different nos
        sumodd += x
        oddindex += 1           # f.	count how many are odd numbers
    if(x%3 == 0):               # c.	sum of numbers which are divisible by 3 from n different numbers
        sum3 += x
    if(x%5 == 0 & x%7 == 0):    # d.	sum of numbers which are divisible by 5 and 7 both
        sum5and7 += x
    if(x > 0):
        poscount += 1           # g.	count how many are positive numbers
    elif(x == 0):
        zerocount += 1          # i.	count how many are zeros
    else:
        negcount += 1           # h.	count how many are negative numbers

print("Sum of even numbers is:",sumeven)
print("Sum of odd numbers is:",sumodd)
print("Sum of numbers divisible by 3 is:",sum3)
print("Sum of numbers divisible by 5&7 is:",sum5and7)
print("count of even numbers:",evenindex)
print("count of odd numbers:",oddindex)
print("count of positive numbers:",poscount)
print("count of negative numbers:",negcount)
print("count of zero numbers:",zerocount)

# 2. Write a python program to print sum of factorial series 1! + 2! +3!......... 10!
fact = 1
sum = 0
n = int(input("Enter a number: "))

for i in range(1,n+1,1): #1
    fact = fact * i
    print(fact)
    sum += fact   

print("The sum of factorial of",n,"numbers is",sum)

# 3. Write a python program to accept a number from user & 
# print square of that number condition to that user has entered
# positive number, give three chances to the user if user has entered negative number, 
# on 4th chance break the loop.
count = 1

while(count < 4):
    n = int(input("Please enter the number: "))
    if(n > 0):
        square = n*n
        print("square of",n,"is",square)
        count = 1
        break
    else:
        print("Please enter a positive number.")
        count += 1
        if(count == 4):
            print("Maximum attempts reached... Exiting !!!!")
        continue

# 4. Write a python to create ATM transaction, provide access of transaction till user wish, 
# give menu for b for balance check, w for withdraw, d for deposit, 
# In all cases print final updated balance amount, Accept initial balance amount from user.

balance = 10000
withdraw_amount = 0
deposit_amount = 0

while(True):
    user_input = input("Please enter b for balance check, w for withdraw, d for deposit: ")
    if(user_input == 'b' or user_input == 'B'):
        print("Your account balance is:",balance)
    elif(user_input == 'w' or user_input == 'W'):
        withdraw_amount= int(input("Please enter anount you want to withdraw: "))
        if(balance >= withdraw_amount):
            balance = balance - withdraw_amount
            print("The updated balance is:",balance)
        else:
            print("Insufficient funds. You have",balance,"in your account")
    elif(user_input == 'd' or user_input == 'D'):
        deposit_amount = int(input("Please enter the amount you want to deposit."))
        balance = balance + deposit_amount
        print("The updated balance is:", balance)
    elif(user_input == 'break'):
        break
    else:
        print("Please select the correct option.")
        

# Assignment on List
# 1.	How to create list
l = [1,2,3,4]
l

l1 = list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
l1

# 2.	How to create empty list
l2 = []
l2

# 3.	Indexing of List elements in forward way from left to right
l1[0:4]

# 4.	Indexing of List elements in reverse way from right to left
l1[-1:-5]  ## reverse traverse is not possible in list
l1.reverse()
l1[0:4]

# 5.	What is default traversing direction of List? Can we traverse list from right to left
l1[-1:-5]  ## reverse traverse is not possible in list
# left to right is default.

# 6.	How to access or display First element of List
l1[0]

# 7.	 How to access or display Last element of List if List consist of 9 elements, Answer by two ways
l1[8]
l1[-1]

# 8.	How the Nested list elements are accessed with two elements in a list , first element is nested list of 3 elements
n = [[1,2,3],"Hello"]

# 9.	How to display third last element with negative indexing
n[-1][-3]

# 10.	Slice list to display 3rd,4th and 5th element from List
l1[2:5]

# 11.	Display List elements from start to 6th
l1[0:6]

# 12.	Display elements from 2nd element to end
l1[1:]

# 13.	Display all elements of the list from beginning to end by using :
l1[:]

# 14.	Create List as odd = [2, 4, 6, 8], replace first element as 1
odd = [2, 4, 6, 8]
odd.remove(2)
odd.insert(0,1)
odd

# 15.	Replace element 2nd to 4th with [3,5,7]
del odd[1:4]
odd = odd + [3,5,7]
odd
# 16.	Display total number of elements in odd list
len(odd)

# 17.	Display occurance of 3 in odd list
l1.count(3)

# 18.	Display sum of all elements of odd list
sum = 0
for i in odd:
    sum += i
    
print(sum)
# 19.	Display maximum element from List
max(l1)

# 20.	Display minimum element from List
min(l1)

# 21.	Delete 3rd element from List by specifying index number
l1.pop(2)
l1

# 22.	Delete 3rd element whose value is 40 by specifying value
l2 = [34,12,40,54,30]
l2.remove(40)
l2

# 23.	Delete elements from 3rd to 6th from the list
del l1[2:6]
l1

# 24.	Pop element from List
l1.pop(4)

# 25.	Pop 5th element from List
l1.pop(4)

# 26.	Sort list and do not update original one
l3 = sorted(l2)
l2
l3

# 27.	Sort list by updating original one
l2.sort()
l2

# 28.	Sort list in a reverse order
l2.sort()
l2
l2.reverse()
l2

# 29.	Display sum of all elements of odd list
sum = 0
for i in odd:
    sum += i
    
print(sum)

# 30.	Clear whole list
l3.clear()
l3

# 31.	Create list a=[1,2,3] b=[4,5,6] and concatenate both & display new list
a=[1,2,3]
b=[4,5,6]

c = a+b
c

# 32.	Repeat list a 5 times and store in d
d = a*5
d

# 33.	Repeat only first two elements of List a 6 times and store in new
e = a[0:2]*6
e

# 34.	Check 30 is available in list a
if 30 in a:
    print("List a contains 30")
else:
    print("List a does not contain 30")

# 35.	Check 2 is not available in list a
if 2 in a:
    print("List a contains 2")
else:
    print("List a does not contain 2")

# 36.	Append 6 element in list a
a = a + [5,6,7,8,9,10]
a
# 37.	Append any decimal number to a list
a.append(11.4)
a

# 38.	Create a temp list of 5 elements and extend a list by adding temp list
temp = [1,2,3,4,5]
a = a + temp
a

# 39.	Display index number of any specified element
a[11]

# 40.	Copy list a to newlist
b = a.copy()
b

# 41.	Using for loop to traverse through list newlist and print all elements of the List on a single line separated by comma
for i in b:
    print(i, end = ',')

# 42.	Within a for loop only assign list and traverse and display each element of list on separated line
for i in b:
    print(i)

# 43.	Create a list of natural numbers from 1 to 50 by using inbuilt function
e = list(range(1,51,1))
e
e[11]

# 44.	Create List of even numbers from 2 to 40 by using inbuit function
even = list(range(2,40,2))
even

# 45.	Create list of numbers in descecending order with specified interval
reve = list(reversed(range(1,10,1)))
reve

# 46.	Creating a list from negative integers to positive integers of a number (Hint -5 to 5)
f = list(range(-5,5,1))
f

# 47.	Creating a list with equally spaced numbers
e = list(range(1,51,1))

# 48.	Print datatype of newlist
type(f)

# 49.	Insert 5th element in newlist as 90
f.insert(5,90)
f

# 50.	Write difference between del,pop & remove
# pop deletes a particular value using indexing
# remove deletes a particular value using actual value
# del is similar to pop except it can delete sequence of values using indexing

# 51.	Write difference between sorted and sort
# sort will update the list you are working on
# sorted will not update the list, instead we can create another list and put the sorted values of the current list in the new list without changing the current list.

# 52.	Write difference between sort and reverse
# sort will sort the list in ascending order
# reverse will reverse the sequence of values. for eg the last value will be first, secondlast will be second and so on.