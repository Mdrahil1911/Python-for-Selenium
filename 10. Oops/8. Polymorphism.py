#POLYMORPHISM: One thing can have many things
        #This can be implemented using oveloading concept
        #Polymorphism is not fully supported in python but we can achieve basic concepts ot it

class Human:
    def hel(self, name=None):
        if name is not None:
            print("Hello" +" "+ name)
        else:
            print("Hello")

hobj=Human()
hobj.hel("Peter")
hobj.hel()