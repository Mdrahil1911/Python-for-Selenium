#FUNCTIONS: A block of statements/ a piece of code which will perform task
            #Function declaration/ Creation (def keyword we use)
            #Calling the function/Invoking function (by func name)

def myfun():       #Declaration of the function using def keyword
    print("Hello Rahil!!,\n How are you?")

myfun()      #Calling a function with its name

#Function with Argument
def myfun2(name):
    print("Hello", name)

myfun2("Rahil")   #calling a function with parameter

def cal(a,b):      #Argument
    return a+b #Returning the output
print(cal(10, 20))
# c=cal(10,20)     #cal(10,20) assigned to function and return value is stored in a variable c
# print(c)

#Functions can return multiple values

def largest(l,k):
    if l>k:
        return l,k
    else:
        return k,l
print(largest(100,200))

