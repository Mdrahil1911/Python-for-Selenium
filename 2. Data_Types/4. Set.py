#Return to this module after completing Numbers and String concept for now skip it

#SET: is a collection of unordered and unidexed items
    #Written in curly brackets {}
    #Set is a mutable

#Crreating a Set

set1={"apple", "banana", "orange", 10, 20}
print(set1)

#Accessing sets through loops index wont work here
for i in set1:
    print(i)

#Adding, Updating(multiple items can addeed), removing items in a set using add(), update(), remove()

set1.add("watermelon")
print(set1)

set1.update([50, 60, 100])   #Keep the updagte elements in square brackets
print(set1)
print(len(set1))    #To print the length of set'

set1.remove(100)
print(set1)

#NOTE: Difference between remove and discard is if u try to remove non existing element remove shows error but discard doesnt show error

# set1.remove(100)      #Shows KeyError: ____
set1.discard(100)

#Joining set we use union

set2={100,200,300}
set3=set1.union(set2)
print(set3)

set1.update(set3)    #Joining usingg update
print(set1)