#CONSTRUCTOR name is fixed def __init__(self):
#will not return value, can take arguments
#Will be called at the time of object creation

class myclass:
    def __init__(self):
        print("This is a constructor")

    def method(self):
        print("Hello ")

mc=myclass()     #constructor will be executed

#Constructor with arguments
class myclass2:
    name = "Peter"       #class variable
    def __init__(self, name):      #local variable in a constructor
        print(name)
        print(self.name)
        
mc2 = myclass2("David")
