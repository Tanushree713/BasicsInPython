## Buy and sell the Stock on max_profit ##
# max_profit = max value(1st element is lowest after that look the max one ) - min value in a given array #
# Time complexity is O(n) , Space Complexity is O(1)
## yha pr 7 sbse highest stock value thi  pr after 1st day , stock get degrade so get the max loss from 1st to jump in 2nd day that's why 1st day is not considered as max value to provide profit ##

prices = [7, 1, 5, 3, 6 , 4 ]
def findMaxProfitInStock(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price :
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price 
    return max_profit 

result = findMaxProfitInStock(prices)
print("Max Profit in Stock get :" , result )        


## Collinear Points ##
# Both having Time Complexity O(1) and space Complexity O(1)
# 2 Appraoches :-1. using slope concept 2. using area of triangle concept
x1 , x2 , x3 , y1 , y2 , y3 = 1, 1 ,1 , 6, 0 , 9

#1# Approach 1(Using Slope Concept )

def isCollinearPointsUsingSlope(x1 , x2 ,x3 , y1 , y2 , y3):
    if((y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)):
        print("Points are collinear")
    else:
        print("Points are non-collinear")

result = isCollinearPointsUsingSlope(x1 , x2 ,x3 , y1 , y2 , y3)

#2# Approach 2(Using Area of Triangle Concept )

def isCollinearPointsUsingArea(x1 , x2 ,x3 , y1 , y2 , y3):
    area = 0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    if(area == 0):
        print(" Collinear Points")
    else:
        print("Non-Collinear Points")    

resultant = isCollinearPointsUsingArea(x1 , x2 ,x3 , y1 , y2 , y3) 



## Majority Elements ##
## Frequency of elements present in an array is greater than n/2 , where n is length of an array ##
nums = [1, 2 , 3, 2 , 1, 2, 2]

# Approach1 :- Hash Data Structure(key:value) , Time complexity is O(n) , Space Complexity is O(n) #

#importing Dictionary 
from collections import Counter

def majorityElement(nums):
 counts = Counter(nums)
 print(counts)
 max_count = max(counts.values())
 # If counts of values are same then return no one is majority element 
 # if all(count == max_count for count in counts.values()) :
 # return ("No one is Majority") 
 if max_count > len(nums)//2 : 
  return max(counts.keys() , key = counts.get)
 else :
    print("Not exist Majority") 

result = majorityElement(nums)
print("Majority Element is :" ,result)


# Approach2 :-  Boyer-Moore Voting Algo , Time Complexity is O(n) , space complexity is O(1)#
# calling 2 functions 1.findingMAjorityCandidate 2.CheckIs Majority or not
def findMajority(nums):
    candidate = None 
    count = 0 
    for num in nums :
     if count == 0:
        candidate = num
     count += (1 if num == candidate else -1)
    return candidate

def isMajority(nums , candidate):
    cnt = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == candidate:
            cnt += 1
    if cnt > n/2:
        return 1 
    else:
        return 0

def printMajority(nums): 
 candidate = findMajority(nums)
 if isMajority(nums , candidate) : 
    print("Majority Element in given array is:" , candidate)
 else:
    print("Not Exist Majority Element ")    

result = printMajority(nums)











