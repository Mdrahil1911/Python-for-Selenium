#Exception is an event which will cause program termination

#Whener user providing invalid input, at that time it casess

#Even though programming is throwing exception the below statement gets executed those are handled by exception handling

#In python we have 3 statements to handle

#try, except, else
#Whichever statements are throwing exception just keep them in try block

#EX1:

print("starting the programme")
print("Executing the code")
try:
    print(x)      #We did not defined x value so it will throw exception and programme stops here
except:           #To not stop the program we kept that sttement in try block
    print("exception occured")
print("End of the programme")

#EX2: Mentioning exception error, if you know

print("starting the programme")
print("Executing the code")
try:
    print("x")      #We did not defined x value so it will throw exception and programme stops here
except NameError:           #To not stop the program we kept that sttement in try block(NameError: name 'x' is not defined)
    print("exception occured")
print("End of the programme")