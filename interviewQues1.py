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




## Sort Colors (0, 1, 2) ##
arr = [ 2, 0 , 1, 2 ,0]
# if asked to do sorting then , use hash DS whose Time complexity is O(n) and Space Complexity is O(1) #
##  Here, Use P0 --> Pointing0(Put LHS) and P2 --> Pointing2(Put RHS) , automatic given array get sorted and is applicable if (0,1,2) are only elements in an array ## 
# Time complexity is O(n)

def sortColors(arr):
    curr = p0 = 0
    p2 = len(arr) - 1 
    while curr<= p2:
     if arr[curr] == 0:
        # swapping putting 0 at p0 towards LHS
        arr[p0] , arr[curr] = arr[curr] ,arr[p0]
        curr +=1
        p0 +=1
        # swapping putting 2 at p2 towards RHS
     elif arr[curr] == 2:
        arr[p2], arr[curr] = arr[curr] , arr[p2]
        p2 -= 1   
     else:
        curr += 1
    return arr 

resultSortedColors = sortColors(arr)
print("sortedColors are:" , resultSortedColors)



## Top K Frequent Elements ##
# finding out largest kth elements according to their highest frequency #
# Time Complexity is O(n + klog(n)) , in worst case k=n So, overall TC becomes O(n^2) 
#  and Space Complexity is O(n)

from collections import Counter 
import heapq
array = [2 , 1, 1 ,1 , 3, 3 , 4]
k = 3
# Base Cond if finding out K(same as given array length) elements , return array 
def topKfrequnecyElement(array , k):
 if k == len(array):
    return set(array)

 count = Counter(array)
 print(count)
 return heapq.nlargest(k , count.keys() , key = count.get)    

result = topKfrequnecyElement(array , k)
print("Top K elements is" ,result)




## Top Closest points ##
# k - Minimum Distance wale points ko as a output paas krna h # 
# Time complexity is O(klogn), Space Complexity is O(n+k) , where in worstCase k=n
from heapq import heappush , heappop
import math 

def get_distance(x, y):
    return math.sqrt(x**2 + y**2)

def kClosestPoints(points , k):
    min_heap = []
    n = len(points)
    for i in range(n) :
        x = points[i][0]
        y = points[i][1]
        heappush(min_heap , (get_distance(x , y) , points[i]))

    result = []
    for i in range(k):
        result.append(heappop(min_heap)[1])
    return result  

points = [[3,3] , [5,-1] ,[-2,4]]
k = 2

topkpoints = kClosestPoints(points , k)
print("Top K Closest Points", topkpoints )



## Count Number of ways to reach Upstairs ##
# either Takes one step or two step at a time #
# Time Complexity is O(n), Space Complexity is O(1) #

def countNumWays(n):
    if ( n <= 3):
        return n 
    else :
        return countNumWays(n-1) + countNumWays(n-2) 

n = 5
print("Number Of ways To reach Upstairs " ,countNumWays(n))       



## Find Pairs whose Sum equals to target value ##
# Using Two pointer Approach #
# Time Complexity is O(n) , Space Complexity is O(1)

def findPairs( arrays , target):
    # big Problem
    l = 0
    r = len(arrays)-1 
    while l < r :
      if arrays[l] + arrays[r] == target :
        return l , r
      elif arrays[l] + arrays[r] < target :
        l = l + 1
      else :
        r = r -1     


    return -1 , -1

arrays = [ 20 , 35 , 7 , 9 , 11]
target = 55
sumOfPairs = findPairs(arrays , target)
print("index of element whose sum is given target value :", sumOfPairs)



  

## KADANE'S ALGORITHM ##
# Maximum SubArr Sum #
# Time Complexity is O(n) , Space Complexity is O(1) #
def MaxSumSubarr(nums):
    start =  0
    end = 0 
    currSum = 0 
    maxSum = float('-inf')
    total_indx = 0 
    n = len(nums)
    for i in range(n):
        currSum += nums[i]
        if currSum < 0 :
            currSum = 0 
            total_indx = i + 1
        if currSum > maxSum :
            maxSum = currSum 
            start = total_indx 
            end = i 

    if maxSum == 0 :  # empty 
        start = -1 
        end = -1

    return ( maxSum , nums[start:end + 1] )
# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = MaxSumSubarr(arr)
print("Maximum Subarray Sum And Corresponding Subarray:", result )




## Kth Missing Element in an Array ##
# Time Complexity is O(n) , Space Complexity is O(1)
def kthMising(nums , k):
    low = 0 
    high = len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        midEle = nums[mid] - (mid+ 1)
        if midEle < k :
            low = mid + 1
        else:
            high = mid + 1
        return low + k 
nums = [2 ,3 ,4 ,7 ,11]
k = 5    
result = kthMising(nums , k) 
print("kth Missing element is " ,result) 
  







