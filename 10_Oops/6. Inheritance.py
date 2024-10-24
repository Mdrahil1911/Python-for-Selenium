#INHERITANCE: Acquiring all the variables(attributes) and methods(behavious) from one class to another class

#USES: Code reusability, Avoid Duplication

#TYPES: Single level, Multi Level, Heirarchy, Multiple Inheritance

#EX1: Single Level Inheritance

class A:
    def m1(self):
        print("Method 1 is printed")

class B(A):
    def m2(self):
        print("Method 2 is printed")

bobj=B()
bobj.m1()     #So class b is able to access class A methods
bobj.m2()

#EX2: Multi Level Inheritance

class A:
    a, b = 10, 20
    def method1(self):
        print(self.a, self.b)

class B(A):
    def method2(self):
        print("Class method b is executed")

class c(B):
    def method3(self):
        print("class method c is excuted")

cobj=c()

cobj.method1()      #class c is able to access class A as well class B
cobj.method2()

#EX3: Heirarchy Inheritance

class A:
    def g1(self):
        print("class A")

class B(A):
    def g2(self):
        print("class B")

class C(A):
    def g3(self):
        print("class C")

bobj=B()
cobj=C()

bobj.g1()     #Class a can be access through class B as well as Class C

cobj.g1()      #we cannot access class B using C

#EX:4 Multiple Inheritance

class A:
    def h1(self):
        print("h1 from class A")

class B:
    def h2(self):
        print("h2 of class B")

class C(A,B):
    def h3(self):
        print("h3 of class C")

cobj=C()

cobj.h1()
cobj.h2()

