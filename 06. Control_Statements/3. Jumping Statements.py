#Jumping: break, continue

#We always use these along with conditional statements or looping statements

#EX:1
for i in range(1,10):
    if i==5:
        break
    print(i, end=" ")
print("program exited!!!!!!")
print()

#EX:2
for i in range(1,10):
    if i==5:
        continue           #it skips 5 but continues loop
    print(i, end=" ")
print("program exited!!!!!!")
print()

#EX:3
for i in range(1,21,2):
    if i==10 and 1==20:
        continue
    print(i, end=" ")