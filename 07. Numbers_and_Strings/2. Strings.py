#Strings are immutable - If the id value changes efter each run then its immutable

#ways of creating string

s= "welcome"
s=str("welcome")
s=""
s=str()
s=''

print(s)
#it always prints the last variable assinged

a ="welcome"

print(id(a))    #Every time you run a new id is genearted

print((a*3))

# "in" "not in" operators along with strings which return true or false (boolean values)

x= "Indian"

print("Ind" in x)
print("inds" in x)
print("ian" not in x)


