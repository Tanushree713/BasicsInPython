## 42. Fibonacci Number 
# Time Complexity is O(n) , Space Complexity is O(1)
def fibonacciNum(n):
  # Base Cond
  if n == 0 or n == 1 :
    return n
  else :
    return fibonacciNum(n-1) + fibonacciNum(n-2)   

n = 4 
result = fibonacciNum(n)   
print("Fibonacci is " , result)  


## 43.Find Power of four
# APProach1>>Using Maths
# Time Complexity is O(1)) , Space Complexity is O(1)
from math import log
def findPower(n):
 return n > 0 and log(n , 4)% 1 == 0 #for +ve values
n = 14 
result1 = findPower(n)
print("Given n is Power of x" , result1)

# APProach2>>Using Recursion
# Time Complexity is O(n) , Space Complexity is O(1)
def findPowerNum(n):
    # Base Cond
    if n==1 :
        return True 
    elif n <= 0 :
        return False 
    else:
        return n % 4 == 0 and findPowerNum(n // 4)  #make sure n is multple of 4 then also powerofnum or divisible by 4       
n = 16
result2 = findPowerNum(n)
print("Given n is Power of x using recursion" , result2)




## 44. Sum of Digit of a Number Using recursion
#APProach >> Reverse number and add them 
# Time Complexity is O(n) , Space Complexityis O(1)
def findSumOfDigit(n):
  sum = 0
  remainder = 0 
  # base cond
  if not n :
    return 0
  return (n % 10 + findSumOfDigit(n//10))
    
nums = 12357
result = findSumOfDigit(nums)
print("Sum Of the Given Digits" , result)


## 45.
## 46.
