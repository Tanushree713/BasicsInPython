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
# fstring >> print(f"{nums}X{i}={nums*i}")



##-----------------------8. Functions And Recursions -----------------------------##
# Types of function :- 1. Built-In( Ex>> print , sum , swap )  2. User-Defined( defined by user )
# pass default parameter >> def greet(name= "Stranger"):    print("hello!" + name )