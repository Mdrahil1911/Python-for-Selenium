#PACKAGES: Collection of Modules

#I want to acces m1 and m2 outisde the packages
#EX:1
#package1
#module1.py               #module2.py

#Package2
#module3
import sys
sys.path.append("paste the package path where 2 modules are present with forward slashes")
import module1
import module1

module1.fly()  #-----If only functions are present

hobj=module1.Human()     #Create objects if the functions are present inside the classes
hobj.fly()