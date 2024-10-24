def fun(i,j):
    print(i,j)
fun(i=10, j=20)     #Assigning using keyword
fun(j=20, i=10)     #specific character takes specfified value

#Default value is assigned to positional arguments

def fun2(i, j=200):
    print(i,j)
fun2(100, 300)   #Final argument assigned will take the value

fun2(100)   #Here by default value of j will be printed, if we dont specify

def greet(name, greetmsg):
    print(greetmsg +" "+ name)
greet(name="Rahil", greetmsg="How are you")     #Keyword

#Thumb Rule: Positional argument must appear before keyword arguments
#EX:
def fun3(a, b, c=10):
    print(a, b, c)
# fun3(c=20, 100, 500)      #This will throw error

fun3(10, 20, c=30)

