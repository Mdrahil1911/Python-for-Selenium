#Return to this module after completing Numbers and String concept for now skip it

#Sequence data types: list, tuple

#LIST: is a collection which is ordered and changeable
        #Lists are written inside sqaure brackets []
        #List is mutable

#Creating a list

list1= [10, 20, 30, 40]    #Numbers list
list2=["mango", "banana", "apple", "watermelon"]  #strings list
list3=["kiwi",10, 20, "seed"]     #combination of numbers and strings
list6=list()     #Empty list

print(list1), print(list2), print(list3), print(list)

#Access items in a list

print(list1[0])   #We are giving index number
print(list2[-1])   #fetches last element in a list

#Range of Indexes

print(list2[0:3])
print(list3[-3:-1])

#Changing of item values

list2[3]="orange"
print(list2)

#Read the list items using loop

for i in list2:
    print(i)

#Check if item is exist in the item or not

if "watermelon" in list2:
    print("item exist")
else:
    print("item not exist")

if "orange" in list2:
    print("item exist")

#Adding new item in a list we use word "append"

list2.append("Pineapple")
print(list2)

#Use insert instead of append
list2.insert(0, "Jackfruit")  #You can specify the index to add the item at specific place
print(list2)

#Remove, delete, clear item from the list we use "pop()", del, clear()
list2.pop(0)
print(list2)

del list2[0]     #0th item is deleted
print(list2)

list2.clear()    #Empty list
print(list2)

#Copying of list
list2=list1.copy()
print(list2)

#Joining the list use operator "+"

list4=list2+list3
print(list4)

#Joining with using loop
print(list4, end=" ")
print(list1, end=" ")
for i in list4:
    list1.append(i)
print(list1)

'''TUPLE: is a collection which is ordered and unchangeable
    tuples are written in round brackets()
    Tuples are immutable'''

#Creating a tuple

tuple1=("apple", "banana", "dragon")
print(tuple1)

#Accessing tuple
print(tuple1[1])

#Chnaging tuple items
#Directly we cannot change it but we can convert them into list, change the value and convert to tuple

tuple2 = (10, 20, 30, 40, 50)
list5 = list(tuple2)      #converting the tuple
list5[1] = "orange"       #Modifying the value
tuple2 = tuple(list5)     #converting to tuple again from list
print(tuple2)

