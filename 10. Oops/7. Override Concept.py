#Override: Parent and child class have same method

class A:
    def m1(self):
        print("m1 is method from class A")

class B(A):
    def m1(self):
        super().m1()     #By adding this we called class A method from class B
        print("m1 is also a method from class B")

bobj=B()
bobj.m1()    #Latest/new method will be printed here it referes to classB method


#EX1: Accessd class variable of A in the class B

class A:
    a, b = 10, 20

class B(A):
    i, j = 100, 200
    def m(self, x, y):
        print(x+y)
        print(self.a + self.b)   #class variable of is called
        print(self.i, self.j)

bobj=B()
bobj.m(25, 15 )

#EX2: Override Variables

class A:
    name = "Peter"

class B(A):
    name = "John"

bobj = B()
print(bobj.name)

#To override the latest cariable we need ti create a method to access the old variable

class A:
    name = "Peter"

class B(A):
    name = "John"
    def test(self):
        print(super().name)     #we need to create method in that add super(), direct we cannot


bobj = B()
bobj.test()

#Overriding Methods

class Bank:
    def roi(self):
        return 0

class Xbank(Bank):
    def roi(self):          #Same method but return is different
        return 10

class Ybank(Bank):
    def roi(self):           #Same method but return is different
        return 12

Xobj= Xbank()
print(Xobj.roi())

Yobj=Ybank()
print(Ybank.roi())

