# If you want to print any statement in console window we are using print statement

#We have diffferent methods to print the outputs

#Approach 1

name, age, sal = "Rahil", 26, 50000
print(name, age, sal)

#Approach 2

print("Name is:", name)
print("Age is:", age)
print("salary is:", sal)

#Approach 3: Usinf %

print("Name is:%s \nAge is: %d sal is: %g" %(name, age, sal))

#Approach 4: Using curly braces {}

print("Name is:{} Age is:{} salary is:{}" .format(name, age, sal))
