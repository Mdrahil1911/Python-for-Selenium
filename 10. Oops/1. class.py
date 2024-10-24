#CLASS: collection of variables(attributes) and methods (behaviour)
        #Class is a blueprint
        #It is a logical entity
        #Does not occupy space in memory
        #Once you created class, can add multiple objects in it

#NOTE: We can craete function without class
#NOTE: Methods are created inside the class and we need to call the method

class myclass:      #class is craeted with keyword class and name given as myclass
    def fun(self):      #Functions created inside the class are called methods
        pass             #self word argument is added and is refering to the class we should not remove even we add argument
    def display(self):
        print("Rahil")

mc1=myclass()   #creating a object and refering to the class
mc1.fun()       #calling methods inside the class
mc1.display()

class myclass2:
    def fun1(self, name):
        print(name)
mc2=myclass2()
mc2.fun1("Md Rahil")