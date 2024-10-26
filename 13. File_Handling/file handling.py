#Steps to handle files

#Step 1: Craete a .txt file in the system
#Step 2: To read open("path file", 'r'), To write open("path file", 'w'), To append write open("path file", 'a')

#EX1: Writing data into text file

# file = open("C:\Users\MD Rahil\OneDrive - chaincode consulting llp\Desktop\python write.txt", 'w')
# file.write("This is my 1st statement\n")
# file.write("This is my 2nd statement\n")
# file.write("This is my 3rd statement\n")
# file.close()
# print("Added the statements in the file")

#Reading the data from the text file

file = open("C:\\Users\\MD Rahil\\OneDrive - chaincode consulting llp\\Desktop\\Untitled.txt", 'r')
print(file.read())
file.close()

#Appending the data into text file

file = open("C:\\Users\\MD Rahil\\OneDrive - chaincode consulting llp\\Desktop\\Untitled.txt", 'a')
file.write("This is my 6th statement\n")
file.write("This is my 7th statement\n")
file.close()
print("Appended the statements in the file")

#NOTE: Write mode will erase the data and add the new statements, but append will add new statemets with existing statements

