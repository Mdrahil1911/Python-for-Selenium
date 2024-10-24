#Variables created inside the class
class myclass:
    a, b =10, 20      #class variable
    def add(self): # where a and b are class variable
        # print(a,b)     #it will show error we cannot access class variable inside the methods

        print(self.a, self.b)  # define self keyword to access the class variable
        print(self.a*self.b)

mc=myclass()
mc.add()

#Defining glabal variable and accessing inside the class

x, y = 10, 20   #Global variable
class class2:
    def sub(self):
        print(x,y)    #global varaibles accessed, self keyword not necesssary
mc1=class2()
mc1.sub()

#global and local variable

i,j=10, 20
class class3:
    g, h = 5, 10    #class variable
    def mul(self):
        print(self.g, self.h)
        print(i, j)
mc3=class3()
mc3.mul()

#Same variable name for global, class and local. How we can access?

a, b = 5, 10
class myclass4:
    a, b =100, 200
    def fun(self, a, b):
        print(a, b)
        print(self.a, self.b)
        print(globals()['a'], globals()['b'])

mc4=myclass4()
mc4.fun(7, 8)

#Creating multiple objects from 1 class

class class5:
    def display(self, name):
        print(name)
mc5=class5()
mc5.display("John")

mc6=class5()
mc6.display("Peter")