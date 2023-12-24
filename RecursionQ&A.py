## 42. Fibonacci Number 
# Time Complexity is O(n) , Space Complexity is O(n)
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
# Time Complexity is O(logn) , Space Complexity is O(logn)
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
# Time Complexity is O(logn) , Space Complexityis O(logn)
def findSumOfDigit(n):
  # base cond
  if not n :
    return 0
  return (n % 10 + findSumOfDigit(n//10))
    
nums = 12357
result = findSumOfDigit(nums)
print("Sum Of the Given Digits" , result)


## 45. Find GCD or HCF
# APProach >>  Euclidean Algo 
# Time Complexity is O(log(min(a,b))) , Space Complexity is O(log(min(a,b)))
def findHCF( a , b ):
  if b == 0 :
    return a
  return findHCF(b , a % b)  ## For LCM use , { return abs(a*b)// gcd(a, b )}
a = 48 
b = 17
result = findHCF(a , b)
print(" HCF of a and b is" , result)
    


## 46.Print sums of all subsets of a given set
# Approach 1.>> Power Set 
# Approach 2.>> using recursion {SC = O(n)}, Divide in 2 parts- 
#  1> Selection (pointer move i+1 , sum + arr[i])
#  2> Rejection (pointer move i+1 , sum  )
# Store in DS if i == len(arr)
# then sort the stored sum , {SC = O(2^n)}
# Time Complexity is O(2^n) , Space complexity is O(n + 2^n)

def subsetSum(arr  , i  , sum ,  result ):
   
  if i == len(arr):  # if Come beyond the array  , Store Sum in DS
    result.append(sum)
    return 
  #Include element and recurse(Selection)
  subsetSum(arr , i + 1 , sum + arr[i]  , result  )
  #Exclude element and recurse(Rejection)
  subsetSum( arr , i + 1 , sum , result)

nums = [1, 2, 3]
sum = 0
result = []
i = 0
subsetSum(nums , i , sum  , result ) #fun calling
resultant = list(set(result)) #get unique elements and create list (after creating list able to sort that array )
resultant.sort() # sort getting sum 
for results in resultant:
 print(results , end =" " ) #lies result in one line 

 


                                
