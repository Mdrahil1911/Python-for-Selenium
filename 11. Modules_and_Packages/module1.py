#MODULES: Collection of functions, classes, Python file it self a module

#Create a module and access in different module(calling function from one module to other)

#Here iam calling the functions of module1 in module

import module2

module2.add(10, 20)
module2.add (5, 10)

#Accessing classes of other module

import module2

hobj=module2.Human()
hobj.fly()

bobj=module2.Bird()
bobj.fly()


