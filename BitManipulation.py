##$$$ BIT MANIPULATION  $$$##
# Right Shift (10>>3)=> 10/2^3 ==> 1
# Left Shift (<<)

#Question1>>Find out single element in arr = [ 1, 2 , 2, 4, 5, 4, 3, 5 , 3] ??output is 1
# pseudocode >>
#  XOR = 0 
#  for i in range(len(arr)):
#     XOR = XOR ^ arr[i] 
#  print(XOR)


## If having more than 2 element are single in arr
# pseuduCode >>
# 
# 
# 
#  
#Question2>> Swap 2 numbers a, b
# a = a^b
# b = a^b
# a = a^b

#Question3>> Given n1= 6 and n2 =3 find xor between them >> 6^5^4^3 
#if(n % 4 == 0 ):print(n) >>n= 4 , 8
#if(n % 4 == 1):print(1)  >>n=1 , 5
#if(n % 4 == 2):print(n+1) >>n= 2, 6
#if (n % 4 == 3):print(0)  >>n= 3, 7

#Question4>> Check if N is ODD or not
# if (n & 1 == 0) :
#   print(even)
# else:
#   print(odd)
 
#Question5>> Check bit is set(mean 1 is present ) at ith or not 
# mask = (1<<i) 
# if(mask & n != 0):
#   print(bit is set)
# else:
#   print(not set)
#   n = n | mask :. sets the bit
## hint : if bit is not set wanted to set it so use OR('|') operator 

#Question6>> Remove Last set Bit >> 1100 >>1000
#   newBit = (n & n-1) 

#Question7>> Check n is Power of 2 or Not 
# if(n & n-1 == 0):
#   print(yes)

#Question8>> Count no. of set bits 
# while(n!=0):
#    n = (n & n-1):
#      count++
# print(count)


## Armstrong Number ##
# Time Complexity is O(n) , Space Complexity is O(1) #
import math
def numPower(n):
    return math.pow(n , 3)

def  isArms(num):
        originalNum = num
        result = 0
        while num > 0 :
            lastdigit = num % 10
            cubeNum = numPower(lastdigit)
            result = result + cubeNum
            num = num // 10
        if result == originalNum :
            return True 
        else:
            return False
nums = 253
resultant = isArms(nums)
print("Is Armstrong Number :" , resultant) 


## Pythagorean triplets ##
## Time Complexity is O(n == 3) , Space Complexity is O(1) ##
## Approach >> Sort([a , b, c]) store in a, b , c and then , check by applying pythagoreas Triplet ##
def is_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2



## Reverse Array Using Stack ##
# Time Complexity is O(2n) , Space Complexity is O(2n) #
def reversedArr(arr) :
    stack = []
    result = []
    for i in range( len(arr)):
        stack.append(arr[i])
    while stack:
        result.append(stack.pop())  

    return result  
arr = [5 , 4, 3, 2, 1]     
resultant = reversedArr(arr)
print(resultant)     
