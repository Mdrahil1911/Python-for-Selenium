# Control Statements: Always programme run line by line but sometimes we need to skip or repeat some staements

#CONDITIONAL statements: (if, if else, elif)

#EX: 1 : Print a persion is eligible to vote or not

Name= input("Enter the name of the person:")
Age= int(input("Enter the age:"))

if Age>=18:
    print("Person is eleigible to vote")
else:
    print("Not eligible to vote")

#EX 2: Find a number is even or odd (num%2)

num=int(input("Enter the number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

#if else
#create a program if we add day 1 show sunday, 2- moday etc...

day=input("enter the day:")
if day==1:
    print("Sunday")
elif day==1:
    print("Moday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednessday")
else:
    print("enytered invalid day")