#We can create 2 methods inside the class

#Instance Method - we can call only through objects
#Static Method - Can directly call using class
    #annotation used @staticmethod

#NOTE: In instance self keyword refers to the class
#NOTE: In static self keyword refered to argument

class myclass:
    def fun(self):
        print("instance of the class")

    @staticmethod
    def fun2(self, name):
        print(self, name)

mc1=myclass()
mc1.fun()
mc1.fun2(100, 200)

myclass.fun2("apple", "banana")   #direclty called using class
myclass.fun(10)   #it will show instance of the class we cannot call

