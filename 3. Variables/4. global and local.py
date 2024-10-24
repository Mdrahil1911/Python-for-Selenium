#COME TO THIS TOPIC ONCE U FINISHED FUNCTIONS MODULE TILL THAT SKIP THIS

#variable
    # global - craeted outside of function
    # local - craeted inside the function

global_variable = 20
def func():
    local_variable=10
    print(local_variable)

print(global_variable)
func()   #After calling of function only local variable prints, we cant call local variable outside of function

#EX:1: global and local variable with same name

XY=100
def cool():
    XY=200
    print("inside",XY)
print("outside func", XY)
cool()
print("after calling func", XY)

#Accessing and changing the global variable inside the function having same variable name as local variable

ab=1
def cool2():
    global ab  #we mentioned global variable inside the function
    ab=2      #changed value of a global variable using local variable
    print(ab)     #global variable changed its value to 2 and printed here
cool2()
print(ab)   #local variable affects the global variable and new global variable is printed outside the function

g=500
def cool3(g,h):
    print(g,h)
cool3(600,700)



