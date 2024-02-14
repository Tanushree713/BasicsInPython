## STAR PATTERN ##
#1. ****
#   ****
#   ****
#   ****
def pattern1 (n):
    patn = ""
    for i in range(n):
        for j in range(n):
            patn += "* "
        patn += "\n"
    return patn      
             
# r = int(input("enter rows : "))
# c = int(input("enter cols : "))
# patn1 = pattern1(r , c)
# n = int(input("Enter the Rows & Colm Number :"))
# patn1 = pattern1(n)
# print("Pattern1 is:\n" + patn1)



#2.
# *
# **
# ***
# ****
def pattern2(n):
    patn = ""
    for i in range(1, n+1):
        for j in range (i):
            patn += "*"
        patn += "\n"
    return patn 
# n = int(input("Enter the Rows & Colm Number :"))
# patn2 = pattern2(n)
# print("Pattern2 is:\n" + patn2)    



 #3.****
 #  ***
 #  **
 #  *
def pattern3(n):
    patn = ""
    for i in range(1 , n+1):
        for j in range( 1, n-i+2 ):
            patn += "* "
        patn += "\n"
    return patn 
# n = int(input("Enter the rows and Cols :"))
# patn3 = pattern3(n)
# print("Pattren3 is:\n" + patn3 )           


#4.     *
#      ***
#     *****
#    *******
def pattern4(n):
    pat =""
    for i in range(n):
        # for spaces
         for j in range(n-i-1):
            pat += " "
         for j in range(2*i+1):
            pat += "*"
         for j in range(n-i-1):
            pat += " "
         pat += "\n"  
    return pat            
# n = int(input("Enter the rows and Cols :"))
# patn4 = pattern4(n)
# print("Pattern4 is:\n" + patn4 ) 


#5. *******
#    *****
#     ***
#      *
def pattern5(n):
    pat  = ""
    for i in range(n):
        for j in range(i):
            pat += " "
        for j in range(2*n -(2*i+1)) :
            pat += "*"
        for j in range(i):
            pat += " "
        pat += "\n"
    return pat              
             
# n = int(input("Enter the rows and Cols :"))
# patn5 = pattern5(n)
# print("Pattren5 is:\n" + patn5 )             



#6. *
#   **
#   ***
#   ****
#   *****
#   ****
#   ***
#   **
#   *
def pattern6(n):
    for i in range(0 , n):
        print("*" * i ) 
    for i in range(n-1 , 0 , -1):
        print("*" * i) 
    print("\n")       
# n = int(input("Enter the rows and Cols :"))
# pattern6(n)
      


#7. 1
#   01
#   101
#   0101
#   10101      
def pattern7(n):
    for i in range(1 , n+1):
        if i % 2 == 0 :
            start = 0 
        else :
            start = 1
        for j in range(i):
            if start == 0 :
                if j % 2 == 0 :
                    print("0", end="")
                else:
                    print("1" , end="")  
            else :
                if j % 2 == 0 :
                    print("1" , end="")
                else:
                    print("0" , end="")
        print()    
n = int(input("Enter The rows :"))        
pattern7(n)                 

