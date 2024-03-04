# { * =====  IMP For Interview }

##  ------ 1. MODULES , COMMENTS , PIP ------- ##
# Modules>> can be imported and used in our program 
# PIP >> Package Manager for Python
# COMMENTS >> used to write well mannered and understandable code.
# REPL >> "Read evaluate print Loop" , for few lines of code , use Repl instead of Python but not to much used .



##  ------  2. Variables, dataTypes  -------- ##
# Variable = data Container 
# keyWord = reserved word eg. None , False , while , def , return  , and , break , try , import etc
# datatype :-
# 1> Integer
#2> Floating points Numbers
#3> Strings
#4> Booleans
#5> None #denotes nothing

# Rules For variable naming #
#1.>> Cannot start with Number 
#2.>> No white Space are allowed
#3.>> Contains underscore , digit and alphabet 


# Operators #
# 1.> Arithmatic 
# 2.> Logical (and , or , not )
# 3.> Assigned ( = )
# 4.> Comparison (< , > )
# 5.> Relational( == , <= , >=  )
 
##------------------------ 3. String----------------------------##
# Escape Sequence character >> Sequence of characters after backslash eg. "\n" , "\t"
#  friends = ["tanu" , "manu" , "harry" , "janu" ,"vanu"]
# print(friends[0:4])  >> ["tanu" , "manu" , "harry" , "janu" ]
# print(friends[-4])   >> manu

##------------------------ 4. List And Tuples--------------------##
# :Initialization of List:
#  list = [ 1, 2 , 3 , 4]
# tuples >> Immutable (cannot able to Update)
# :Initialization of tuples:
# tuple0 = ()
# tuple1 = (1,)      || if write "(1)" only without comma Becomes wrong
# tuples = ( 1, 2, 3, 4)
# print(tuple)


##-----------------------5. Dictionary And Sets----------------------##
## Initialisation of both set and dictionary are same "{}""
# Dictionary = collection of key value pairs 
# Empty Dictionary #
# a = {}        *** Empty Set 
# print(type(a)) >> Output :- dictionary TYPE
# 
# myDic = {
#      "1" : "tanu",
#      "2"  : "Manu",
#      "3" : "Janu"
#          }
# print(myDict['4']) >> Throw An Err  **
# print(myDict.get('4')) >> return None (if not present )  **

# Set = collection of unique Elements
# :Initialization of Sets:
# set1 = { 1, 2, 3, 4 , 3, 1, 5}   >> {1, 2, 3, 4, 5}
# b = set()          *** Empty Set 
# print(type(b))  >> Output :- set TYPE 
# *** Set is not hashable , So not able to add any list inside set but tuples can be added *** #
# s = { 20 , 20.0 , "20"}
# print("Length of set" , len(s)) >> 2 (BCOZ, 20 and 20.0 considered as 1-length and "20" is 2-length  )



##-------------------------6. Conditional Expressions --------------------------##
# if , elif , else are conditional Ladder 
# Indentation have 4 Spaces or 1 Tab #

##-------------------------7.LoopS --------------------------##
# In range , 3 parameters can be passed -->> range(start, stop, step-size) where step-size is skipping the no. of elements 
# Types > 1. For ()
#         2. while ()
###
# Difference Between For and While Loop is that :
# 1.Syntax are Different 
# for i in range():
# while condition :
# 2. In For loop , know the number of iterations in advance 
#   In while loop , not know the no. of iterations and will continued when the condition being true 
## for-else used together,"else" will executes only when "for" runs succesfully till end ..If "break" is used inside "for" loop then, else statement cannot be executed..
# PASS STATEMENT( NULL Statement ) >> pass useCase is similar to continue and break , used when need to do nothing 
# fstring >> print(f"{nums}X{i}={nums*i}")  >> use variable with the help of fstring 



##-----------------------8. Functions And Recursions -----------------------------##
# Types of function :- 1. Built-In( Ex>> print , sum , swap )  2. User-Defined( defined by user )
# pass default parameter >> def greet(name= "Stranger"):    print("hello!" + name )
# Uses of Strip >> Helps To remove an Extra Space from begining and ending of string
# def removeWord(strs , word):
#     newStr = strs.replace(word, "Hello")
#     return newStr.strip()

# this = "   hey ! Good Morning   "  
# result = removeWord(this , "hey" ) 
# print(result) 
    
##---------------------9. File I/O ------------------------------##
# RAM ->Volatile and its content are lost once program get terminates 
# HDD -> Non-Volatile 
# File -> Stored data in storage device
# Types of files -> 1. Text Files(.txt , .c  etc) 2.Binary Files (.jpg , .dat etc) 
# Modes Of opening File(In TXT) >> read'r' , write'w', append'a', update'+'
# Read'r' is For reading purpose and Write'w' is For creating new File and write(overwrite) text inside any empty file
# want To append text at the end of text inside file Use write() and append 'a'
# Modes In Binary use (read with 'rb')
# Fuction To Read File >> 1. readline , 2. read  ,3.

# USE OPEN FUNCTION >> To Open The file 
#syntax#
# f = open('sample.txt' , 'r') # by default 'read' mode sample.txt File 
# data = f.read()
# print(data)
# f.close()

#syntax#
# f = open('sample.txt' , 'w')   # for writing 'w' inside sample File and for append replace 'w' with 'a' rest of the code are same 
# f.write("Myself Tanu From Satna ")
# f.close()

# WITH STATEMENT #
# best way to Open and Close(No need to close) File Automatically is the With statement .
#syntax#
# with open("sample.txt") as f :
#     f.read()
# ? How To replace Any Word present In File ?
# Answer:- 
# Read in the file
# with open('sample.txt', 'r') as file:
#   filedata = file.read()

# # Replace the target string
# filedata = filedata.replace('Tanu', 'Shree')

# # Write the file out again
# with open('sample.txt', 'w') as file:
#   file.write(filedata)


##----------------OOPs-------------##
# Fundamental Concepts In OOPs are:
#1. Class
#2. Object 
#3. Abstraction 
#4, Encapsulation 
#6. PolyMorphism 
#5. Inheritance

##------------------Class & Object -------------------##
# class Employee:
#     name = "tanu"
#     def __init__(self , name , age , salary):
#         self.name = name 
#         self.age = age 
#         self.salary = salary 
#     def display_info(self):
#         print("Name :" , self.name)
#         print("Age:" , self.age ) 
#         print("Salary:" , self.salary)   
# print(Employee.name) # class attribute 
# emp = Employee("Tanushree", 20 , "30K")   #Instantiation of Class = Creation of an Object
# emp.display_info()   # instance Attribute 



##--------------------Abstraction & EnCapsulation--------------##

# Abstraction>> Hiding  the Implementation details of an object from the user and providing the simplified interface with object #
# from abc_exmp import Add 
# Add()
#eg>> Using Camera , user Know how to use camera for clicking the picture but they don't know the working function  defined by the programmer
#  
# 1. Abstract Class       2.Interface

#1. Abstract Class (different Implemention & similar(common) action )#
# from abc import ABC , abstractmethod     #(use * for all methods)
# class Car(ABC):
#     def Show(self):
#         print("4 wheels")
#     @abstractmethod    
#     def Speed(self):
#         pass
# class Maruti(Car):
#     def Speed(self):
#         print("100Km/H") 
# class Suzuki(Car):
#      def Speed(self):
#         print("70Km/H")           

#we are not able to create obj of pure abstract class eg,. Car 
# obj1 = Maruti()
# obj1.Show()
# obj1.Speed()
# obj2 = Suzuki()
# obj2.Show()
# obj2.Speed()


#2. Interface (same Action Different implementation )#
# having only abstractmethod 
# from abc import ABC , abstractmethod
# class Shape(ABC):
#     @abstractmethod  #only have abstractmethods
#     def Show(self):
#         pass 
# class Square(Shape):
#     def Show(self):
#         print("Has four Sides")    
# class Pentagon(Shape) :
#     def Show(self):
#         print("has 5 sides")   

# # not able to create Pure Abstract Object #
# obj1 = Square()
# obj1.Show()
# obj2 = Pentagon()
# obj2.Show()




# Encapsulation >> Hiding the Implementation details of an object from the user and providing the controlled access to it . 
# class Employee:
#     _name = "Tanu" # Protected 
#     __age = 20 # Private (written with double undescore are private not able to reveal it publicly )
#     def displayInfo(self)  :
#         print("Name :" , self._name)  
#         print("Age:" , self.__age )
# emp = Employee()
# print("Outside The Class" , Employee._name) # able to access that protected member 

# emp.displayInfo()

# print("Outside The Class" , Employee.__age) # not able to access that private member So throw an ERR 





##----------------------------Polymorphism ----------------##
# Same Object Different Behaviour #
# print(len("Tanushree"))
# print(len(["Tanu" , "Shree"]))
# len function is same but behaviour is different 
# Having OverLoading(calling same function number of times passing same params by adding one in each one by one ) and Overriding(for each customized function gives customized answer)Both #

# OverLoading 
# class MathOperations:
#     def add(self, x, y):
#         return x + y

#     def add(self, x, y, z):
#         return x + y + z
# math = MathOperations()
# print(math.add(2, 3))     
# print(math.add(2, 3, 4))   


#OverRiding
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog = Dog()
# dog.sound() 

# cat = Cat()
# cat.sound() 




##---------------------Inheritance---------------------##
# Child Inherits the parent Properties #
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog = Dog()
# dog.sound() 

# cat = Cat()
# cat.sound()

#Types> 
# 1. Single 
# 2. Multiple
# 3. MultiLevel





