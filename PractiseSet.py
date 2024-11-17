## INPUTS IN PYTHON ##
#1. Single Inputs >> 
#   raw_input() OR input() OR int(input())
#2. Mutiple Space Separated
#   map(input().split())  OR map(int , input().split()) OR map(raw_input().split())
#3. List (ARRAY)>>
# list(map(int , input().split())) OR map(int , raw_input().split(','))
#4.Convert Array to string #
#  ''.join(map(str , arr))   ([4 , 5, 6] => 456)
## Appending ##
# result = ""
# result += char (Input-"XYZ", Output-"XYZ")

## Prepending ##
# result = ""
# result = char + result (Input-"XYZ" , Output-"ZYX" )
#-----------#
# [char = "XYZ"
# result = ""
# for c in char :
#     result = c + result 
# print(result)   ]



##ASCII VALUE##
# A-Z -: 65 - 90
# a-z -: 97 - 122
# 0-9 -: 48 - 57 




##Plus One##
# Tc is O(n) , SC is O(n) #
class Solution(object):
    def plusOne(self, digits):
        string = map(str , digits)
        string = ''.join(string)
        number = int(string) + 1
        return [int(digit) for digit in str(number)]


##Sorting Algo's##
#1. BubbleSort# 
# Tc is O(n^2), Sc is O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr 
arr = [ 6 , 4 , 2 , 1 , 5]
# result = bubbleSort(arr)
# print("Sorted arr Using BubbleSort" , result )


#2. SelectionSort#
# Tc is O(n^2) , Sc is O(1) #
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mid_indx = i 
        for j in range(i+1 , n):
            if arr[mid_indx] > arr[j]:
                mid_indx = j 
        arr[i] , arr[mid_indx] = arr[mid_indx] , arr[i]
    return arr
arr = [ 6 , 4 , 2 , 1 , 5]
# result = selectionSort(arr)
# print("Sorted arr Using SelectionSort ", result )


#3. InsertionSort#
# Tc is O(n^2) , Sc is O(1) #
def insertionSort(arr):
    n = len(arr)
    for i in range(1 , n):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j- 1
        arr[j+1] = key 
    return arr 
arr = [ 6 , 4 , 2 , 1 , 5]  
# result = insertionSort(arr)
# print("Sorted arr Using InsertionSort ", result )       


#4. HeapSort#
# Tc is O(nlogn) , Sc is O(1) #

#5. Quicksort#
# Tc is O(nlogn) , Sc is O(1) #
def quickSort(arr , p , q):
    if p < q :
        mid = partition(arr , p , q)
        quickSort(arr , p , mid - 1)
        quickSort(arr , mid + 1 , q)
        return arr 
def partition(arr , p , q):
    i = p 
    pivot = arr[p]
    for j in range(i+1 , q+1):
        if pivot > arr[j]:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[p] = arr[p] , arr[i]
    return i 
arr = [ 6 , 4 , 2 , 1 , 5] 
p = 0 
q = len(arr) - 1
# result = quickSort(arr , p , q)
# print("Sort arr Using QuickSort" , result)
 

#6. MergeSort #
# Tc is O(nlogn) , Sc is O(n) #
def mergeSort(arr , i , j):
    if i == j :
        return arr 
    else :
        mid = i + (j-i) // 2
        mergeSort(arr , i , mid)
        mergeSort(arr , mid+1 , j) 
        mergeProcedure(arr , i , mid , j)
        return arr 
def mergeProcedure(arr , i , mid , j ):
    n1 = mid - i + 1
    n2 =  j - mid 
    leftArr = [0] * n1
    rightArr = [0] * n2 
    for m in range(n1):
        leftArr[m] = arr[i+m]
    for n in range(n2):
        rightArr[n] = arr[mid+1+n]
    p = 0 
    q = 0 
    k = i 
    while p < n1 and q < n2 :
        if leftArr[p] <= rightArr[q]:
            arr[k] = leftArr[p]
            p += 1
        else:
            arr[k] = rightArr[q]
            q += 1
        k += 1
    while p < n1 :
        arr[k] = leftArr[p]
        p += 1
        k += 1 

    while q < n2 :
        arr[k] = rightArr[q]
        q += 1 
        k += 1
arr = [ 6 , 4 , 2 , 1 , 5] 
i = 0
j = len(arr) - 1
# result = mergeSort(arr , i , j)   
# print("Sort Arr Using MergeSort" , result )                   


##ARRAYS##
#1.MaximumAndMinimum#
# Tc is O(n) , Sc is O(1)#
def maxAndmin(arr , i , j):
    max_val = 0 
    min_val = 0
    if i == j :
       max_val = arr[i]
       min_val = arr[i]
    elif i == j-1 :
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]
    else:
        mid = i + (j-i) //2  
        max_l , min_l = maxAndmin(arr , i , mid)
        max_r , min_r  = maxAndmin(arr , mid+1 , j)
        if max_l < max_r :
            max_val = max_r
        else:
            max_val = max_l

        if min_l < min_r :
            min_val = min_l 
        else:
            min_val = min_r   

    return max_val , min_val 

arr = [12, 1, 4, 5, 18 , 10]
i = 0 
j = len(arr) - 1
# result = maxAndmin(arr , i , j)             
# print("Max and Min val in Arr " , result )


#2.BestTimeToSell#
# Tc is O(n) , Sc is O(1) #
def bestTimeToSell(prices):
    max_profit = 0
    min_price = float("inf")
    for i in range(len(prices)):
        if prices[i] < min_price :
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i]-min_price
    return max_profit 

arr = [ 1 , 3, 5,  7 , 12 , 2]
# result = bestTimeToSell(arr)
# print("Best Time To Sell Stock is " , result )


##*Kadanes Algo*##
# Tc is O(n) , Sc is O(1)#
def maxSumSubArr(arr):
    currSum = 0
    maxSum = float("-inf")
    n = len(arr)
    start = 0
    end = 0
    tempInd = 0 
    for i in range(n):
        currSum += arr[i]
        if currSum < 0 :
            currSum = 0
            tempInd = i+1
        elif currSum > maxSum :
            maxSum = currSum
            start = tempInd 
            end = i
    return (maxSum , arr[start:end+1])            
arr = [1 , 2, 3, 4, 5]
result = maxSumSubArr(arr)
# print("Maximum Sum SubARR" , result )

#3.MaximumProductSubArr#
# Tc is O(n) , Sc is O(1) #
def maxProductSubArr1(arr):
    n = len(arr)
    suffix = 1
    prefix = 1
    maxProduct = 0 
    for i in range(n):
        if suffix == 0 :
            suffix = 1
        elif prefix == 0 :
            prefix = 1   
        else:
            prefix = prefix * arr[i]
            suffix = suffix * arr[n-i-1]
            maxProduct = max(maxProduct , max(suffix , prefix))
    return maxProduct
      #--wanna To find start and end Index --#
def maxProductSubArr2(arr):
    n = len(arr)
    suffix = 1
    prefix = 1
    maxProduct = float('-inf')
    startIndex = 0
    endIndex = 0
    tempStart = 0

    for i in range(n):
        if prefix == 0:
            prefix = arr[i]
            tempStart = i
        else:
            prefix *= arr[i]

        if prefix > maxProduct:
            maxProduct = prefix
            startIndex = tempStart
            endIndex = i

        if suffix == 0:
            suffix = arr[n - i - 1]
            tempStart = n - i - 1
        else:
            suffix *= arr[n - i - 1]

        if suffix > maxProduct:
            maxProduct = suffix
            startIndex = n - i - 1
            endIndex = n - tempStart - 1

    return maxProduct, startIndex, endIndex
arr = [2 , 3 , -4, -1 , 0 , 7 , 2]      
# result = maxProductSubArr1(arr)
# print("Max Product SubArr " , result )

##*NumberOfRoomsHavingGoldCoins*##
# Tc is O(n^2) , Sc is O(k) #
def startAndEndOfRoom(N , K , coins):
    start , end , currSum = 0 , 0 , 0 
    result_start , result_end = 0 , float('inf')
    while end < N :
        currSum += coins[end]
        while currSum  > K :
            currSum  -= coins[start]
            start += 1
        if currSum == K :
            if end - start < result_end - result_start :
                result_start , result_end  = start , end 
        end += 1
    if result_end == float('inf') :
        return "No Solution"
    else:
        return result_start + 1, result_end + 1    

# N = int(input("Enter rooms"))
# K = int(input("Enter coins "))
# coins = list(map(int , input("No. of coins in Room").split()))
# result = startAndEndOfRoom(N , K , coins)
# print("No. of Rooms start and End ", result )
#Input>>
#No.of Rooms >> N - 10
#No. Of coins in Room >> array - 5 3 7 14 18 1 18 4 8 3
#No.of coins Needed To collect >> K - 15
#Output>>
# Index of start and end of Room  >> 1 3


##*Count_ContinuousHorses*##
# Tc is O(n) , SC is O(1) #
def count_continuous_horses(arr, K):
  start = 0 
  end = 0
  currSum = 0  
  maxCount = 0 
  n = len(arr)
  while end < n :
    currSum += arr[end]
    while currSum >= K :
        currSum -= arr[start]
        start += 1
    maxCount = max(maxCount , end - start + 1)
    end += 1  
  return maxCount 
arr = [10 , 90 , 80 , 20 , 90 , 60 , 40 , 60 , 70 , 75]
K = 100
result = count_continuous_horses(arr, K)  
# print("max Continuos Horses" , result )


##*MinLengthSubArrWhoseSumIsGreaterANDEqualTok*##
# Tc is O() , Sc is O() #
def minLengthOfSubArrSumGreaterTok(arr , k):
    minLen = float("inf")
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i , n):
            total += arr[j]
            if total >= k :
                minLen = min(minLen , j-i+1)
                break
    if minLen == float('inf'):
        return 0 
    else:
        return minLen    
arr = [1,3,4]     
k = 11       
# res = minLengthOfSubArrSumGreaterTok(arr , k)
# print(res)

   
##MAXSubArraySumOfSizeK##
def maxSubArrSizek(arr , k):
    res = 0
    maxSum = 0
    n = len(arr)
    for i in range(n-k+1):
        res = sum(arr[i:i+k])
        maxSum = max(maxSum , res)
    return maxSum 
arr = [2,3,4,5,3,6]
# k = 3
# res = maxSubArrSizek(arr , k)
# print(res) 




#Kth Count Of the Candidates to get Kth continuous ##
# Tc is O(n) , SC is O(1)
def kthcount(k , nums):
    count = 0
    cand = None 
    for num in nums :  
        if num == cand:
           count += 1
        else:
            cand = num 
            count = 1 
        if count == k :
            return cand 

    return -1          
nums = [180 , 180 , 200 , 200 , 200 , 350 , 540 , 180]  
k = 3         
result = kthcount(k , nums)
# if (result != -1 ):
#     sumres = k*result
#     print("Kth count" , sumres)
# else:        
#     print("Not Found") 



##*FlipZeroesAtKTimesGetTheMaxLen*##
# Tc is O(n^2), Sc is O(1)#
def flipZeroesAtKTimes(arr):
    maxlen = 0
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(i , n):
            if arr[j]== 0 :
                cnt += 1
            if cnt <= k :
                length = j -i + 1
                maxlen = max(maxlen , length)    
            else:
                break 
    return maxlen 
arr = [ 1,1,1,0,0,0,1,1,1,1,0,1]                
# res = flipZeroesAtKTimes(arr)
# print(res)



##*FruitsInBasket*##
 #Need to store distinct k types fruits in Basket #
 # Tc is O(n^2) , Sc is O(k)#
def stringInBasket(string , k):
    maxlen = 0
    arr = list(string)
    n= len(arr)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(arr[j])
            if len(seen) <= k :
                length = j-i+1
                maxlen = max(maxlen , length)
            else:
                break 
    return maxlen            
string = "aaabcacb"
# k= 2
# res = stringInBasket(string , k)
# print(res)


##*CountSubArrWhoseSumEqualsToK*##
# Tc is O(n) , Sc is O(1) #
def countSubArrEqualsTok(nums , k):
    if k < 0 :
        return 0
    else:
        n = len(nums)
        left = 0 
        right = 0 
        cnt = 0
        currSum = 0  
        while right < n :
            currSum += nums[right]
            while currSum > k :
                currSum -= nums[left]
                left += 1
            cnt += (right-left+1)
            right += 1
    return cnt 
nums = [1,0,1,0,1]  
k = 2                
# res1 = countSubArrEqualsTok(nums , k)
# res2 = countSubArrEqualsTok(nums , k-1)
# print(res1-res2)



##Count the Nice SubARR ##
#SubArr which contains odd elements Equals to K Times #
# Tc is O(n) , Sc is O(n) #
def niceSubArr(nums , k):
    result = []
    n = len(nums)
    for num in nums :
        if isOdd(num):
            result.append(1)
        else:
            result.append(0) 
    if k < 0 :
        return 0    
    else:        
        left = 0 
        currSum = 0 
        cnt = 0 
        right = 0           
        while right < n : 
            currSum += result[right]
            while currSum > k :
                currSum -= result[left]
                left += 1
            cnt += right-left +1
            right += 1   
        return cnt      
def isOdd(n):
   return (n % 2 != 0 )
nums = [1 ,1,2, 1,1]
k = 3
# res1 = niceSubArr(nums , k)
# res2 = niceSubArr(nums , k-1)
# print(res1-res2)
 


##Count The SubARR with K diff Integer ##
# Tc is O(n^2) , Sc is O(k) #
def countSubArrWithKDiff(nums , k):
    n = len(nums)
    cnt = 0
    for i in range(n):
        seen = set()
        for j in range(i , n):
            seen.add(nums[j])
            if len(seen) == k :
                cnt += 1
            elif  len(seen) > k :
                break 
    return cnt   
nums = [1,2,1,3,4] 
k = 3             
res1 = countSubArrWithKDiff(nums , k)
print(res1)


##MAXCOSTOFLAPPY_LEGALANDILLEGAL##
def max_cost(n, cost, labels, daily_count):
    max_cost = 0
    current_day_cost = 0
    num_legal_today = 0

    for i in range(n):
        # Add cost regardless of label
        current_day_cost += cost[i]

        # Only count legal items for daily requirement
        if labels[i] == "legal":
            num_legal_today += 1

        # When we reach the required daily count of legal items
        if num_legal_today == daily_count:
            # Update max_cost if the current day's cost is higher
            max_cost = max(max_cost, current_day_cost)
            # Reset counters for the next day
            current_day_cost = 0
            num_legal_today = 0

    return max_cost

# Example usage
n = 5
cost = [0, 3, 2, 3, 4]
labels = ["legal", "legal", "illegal", "legal", "legal"]
daily_count = 1

result = max_cost(n, cost, labels, daily_count)
print(result)  # Expected Output: 5






#4.TripletSum#
# Tc is O(n^2) , Sc is O(k) #
def tripletSum(nums) :
    resultant = []
    n = len(nums)
    nums.sort()
    for i in range(n-2):
        if i >= 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = n - 1
        while left < right :
            total = nums[i] + nums[left] + nums[right]
            if total == 0 :
                resultant.append([nums[i] , nums[left] , nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left< right and nums[right] == nums[right-1]:
                    right -= 1    
                left += 1
                right -= 1    
            elif total < 0 :
                left += 1
            else :
                right -= 1 
    return resultant         
arr = [2 , 1 , -4, -1 , 0 , 3 , -2]  
# result = tripletSum(arr)
# print("Triplet Sum " , result )


#5.KthSmallestEle#

#5.1 Using QuickSelection Sort #
# Tc is O(nlogn) , Sc is O(1)#
def kthSmallest1(arr , p , q , k):
        m = partition(arr , p , q)
        if m == k :
            return arr[m-1]
        elif m < k :
            return kthSmallest1(arr , m , q , k)
        else:
            return kthSmallest1(arr , p , m-2 , k)

def partition(arr , p , q):
    i = p
    pivot = arr[p]
    for j in range(i+1 , q+1):
        if arr[j] < pivot :
            i += 1 
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i] , arr[p] = arr[p] , arr[i]
    return i + 1

arr =  [2 , 1 , -4, -1 , 0 , 3 , -2]  
k = 3 
p = 0 
q = len(arr) - 1
# result = kthSmallest1(arr , p , q, k)
# print("Kth Smallest Element1" , result)   


#5.2 Using HeapSort #
# Tc is O(nlogk) , Sc is O(k) #
from heapq import heappush , heappop 
def kthSmallest2(nums , k):
    heap = []
    for num in nums :
        if len(heap) < k :
            heappush(heap , -num)
        else:
            if num < -heap[0]:
                heappop(heap)
                heappush(heap , -num)
    return -heap[0]                
arr =  [2 , 1 , -4, -1 , 0 , 3 , -2] 
k = 2
# result = kthSmallest2(arr , k)
# print("Kth Smallest Element2" , result )

# Using BSTConcept #
# Tc is O(nlogn) , Sc is O(k)#


#6.RepeatAndMissingNum#
# Tc is O(n) , Sc is O(1) #
def repeatAndMiss(nums):
    n = len(nums)
    repeat = 0
    missing = 0 
    for num in nums:
        indx = abs(num) - 1
        if nums[indx] < 0 :
            repeat = abs(num)
        else:
            nums[indx] = - nums[indx]    
    for i in range(n):
        if nums[i] > 0 :
            missing = i + 1
    return repeat, missing
arr = [2 ,1 , 5, 4, 4] 
# result = repeatAndMiss(arr)
# print("Repeat And Missing are ", result )            



#7.MergeIntervals#
# Tc is O(nlogn) , Sc is O(1) #
def mergeIntervals(intervals):
    n = len(intervals)
    if not intervals :
        return []
    intervals.sort(key = lambda x:x[0])   
    merged = [intervals[0]]
    for i in range(1 , n):
        curr_intervals = intervals[i]
        last_merged_intervals = merged[-1]
        if curr_intervals[0] <= last_merged_intervals[1]:
            merged[-1] = [last_merged_intervals[0] , max(curr_intervals[1] , last_merged_intervals[1])]
        else:
            merged.append(curr_intervals)    
    return merged 
intervals = [[2, 3] , [3 , 8 ] , [1, 6] , [7, 10]]  
# result = mergeIntervals(intervals)
# print("Merged Intervals are ", result )           


#8.MergeSortedArr#
# Tc is O(n) , Sc is O(1) #
def mergedSortedArr(arr1 , arr2):
    m = len(arr1)-1
    n = len(arr2)-1
    merged = len(arr1) + len(arr2) - 1
    arr1.extend([0]* len(arr2))
    while m >= 0 and n >= 0 :
        if arr1[m] > arr2[n]:
            arr1[merged] = arr1[m]
            m -= 1
        else:
            arr1[merged] = arr2[n]
            n -= 1     
        merged -= 1

    while m >= 0 :
        arr1[merged] = arr1[m]
        m -= 1
        merged -= 1 

    while n >= 0 :
        arr1[merged] = arr2[n]
        n -= 1 
        merged -= 1     

    return arr1
arr1 = [ 2  , 4 , 6, 8] 
arr2 = [ 1 , 3, 5, 7]
# result = mergedSortedArr(arr1 , arr2 ) 
# print("Merged Sorted Arr" , result  )


#9.MajorityEle#
# Tc is O(n) , Sc is O(1) #
def findCand(nums) :
    cand = None 
    count = 0
    for num in nums :
        if count == 0 :
            cand = num 
        count += (1 if cand == num else -1 ) 
    return cand 
def ismajorityEle(nums , cand ):
    cnt = 0 
    n = len(nums)
    for i in range(n):
        if nums[i] == cand :
            cnt += 1
    if cnt > n//2 :
        return True 
    else :
        return False 

def majorityEle(nums):
    cand = findCand(nums)
    result = ismajorityEle(nums , cand)
    # if result :
    #     print("Is Majority " , cand)
    # else:
    #     print("Not Majority ")    
nums = [2 , 3 ,3, 3, 2, 5 , 3]
result = majorityEle(nums)


#10.FindDuplicates#
# Tc is O(n) , Sc is O(n) #
def findDupli(nums):
    seen = set()
    dupli = []
    for num in nums :
        if num in seen:
            dupli.append(num)
        else:
            seen.add(num)
    return dupli 
arr = [2 , 3 ,3, 2, 5 , 4] 
# result = findDupli(arr)
# print("Duplicates are ", result )              


## APP2 ##
# TC is O(n) , SC is O(1) #
def findDupli2(nums):
    xor_res = 0
    for num in nums :
        xor_res ^= num 
    for i in range(1 , len(nums)):
        xor_res^= i 
    return xor_res
# nums = [ 2, 1, 5, 4, 6, 3 , 3] --> o/p:- 3


## APP3 ##
# Tc is O(n) , SC is O(1) #
XOR = 0 
for i in range(len(arr)):
  XOR = XOR ^ arr[i] 
print(XOR)
# arr = [ 1, 2 , 2, 4, 5, 4, 3, 5 , 3] --> O/p:- 1



##RETURNING UNIQUE ARRAY ##
# Tc is O(n), SC is O(1) #
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums :
         return 0 
        uniqIndx = 0 
        for i in range(1 , len(nums)):
            if (nums[i] != nums[uniqIndx]): # not equal  ie, unique
                uniqIndx += 1
                nums[uniqIndx] = nums[i]
          
        return  uniqIndx + 1 , nums[:uniqIndx+1]


## REMOVE ELEMENTS FROM AN ARRAY ##
# TC is O(n) , SC is O(1) #
class Solution(object):
    def removeElement(self, nums, val):
      if not nums :
        return 0
      uniqIndx = 0   
      for i in range(0, len(nums)):
        if (nums[i] != val) :
            nums[uniqIndx] = nums[i] 
            uniqIndx += 1           
      return uniqIndx  


#11.FindNumDivisibleBy2&5#
# Tc is O(b-a) , Sc is O(k)  #
def FindNumDivisibleBy2_5(a , b):
    marked = 0 
    for num in range(a , b+1):
        if num%2 == 0 or num%5 == 0 :
            marked |= (1 << (num-a))
    multiples = []
    for i in range(b-a+1):
        if ( marked & (1 << i) )!= 0   :
            multiples.append(a+i)
    return multiples
a = 10
b = 25
# result = FindNumDivisibleBy2_5(a , b)
# print("Numbers Divisible by 2 or 5 ", result )                 


#12.MergeOperations#
# Tc is O(n) , Sc is O(1) #
def mergeOperationCount(arr):
    i = 0 
    j = len(arr) - 1
    count = 0 
    while i <= j :
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            arr[i + 1] = arr[i] + arr[i+1] 
            count += 1    
            i += 1

        else:
            arr[j-1] = arr[j] + arr[j-1]
            count += 1
            j -= 1
    return count 
arr = [ 1, 2, 3 , 8 , 4 ,  5 , 1]
# result = mergeOperationCount(arr) 
# print(" MergeoperationTo make palindrome ARR :" , result )  

#13.Power(a, n)#
# Tc is O(logn)  , Sc is O(1) #
def power(a ,n):
    if n == 0 :
        return 1
    elif n == 1:
        return a
    elif n < 0:
        n = -n
        a = 1/a
        return power(a , n)
    else:
        mid = n//2
        b = power(a , mid)
        result = b * b
    if n % 2 :
        return a * result
    else:
        return result 
a = 2
n = 5
# result = power(a , n)
# print("n is the Power of a " , result )     


#14.NextPermute#
# Tc is O(n) , Sc is O(1) #
def nextPermute(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] > arr[i+1]:
        i -= 1
    if i == -1 :
        arr.reverse()
    else:
        j = len(arr) - 1
        while arr[i] > arr[j]:
            j -= 1
        arr[i] , arr[j] = arr[j] , arr[i]
        arr[i+1:] = reversed(arr[i+1:])
    return arr
arr = [ 1, 3, 2]
# result = nextPermute(arr)
# print("resultant is " , result )       


#15.SumPairs#
# Tc is O(n) , Sc is O(1) #
def sumPairs(arr , target):
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[i+1] :
            break 
    right = i  
    left = (i+1) % n
    while left != right :
        if arr[left] + arr[right] == target :
            return True 
        elif arr[left] + arr[right] < target :
            left = (left + 1 ) % n  
        else:
            right = ( n + right - 1 ) % n   
    return False 
arr = [ 15, 26, 38, 9, 10]
key  = 19
# result = sumPairs(arr , key )
# print("Sum Pairs :" , result )


#16.SortColors#
# Tc is O(n)  , Sc is O(1) #
def sortColors(nums) :
    curr = 0 
    p0 =  0
    p2 = len(arr) - 1
    while curr < p2 :
        if nums[curr] == 0 :
            nums[p0] , nums[curr] = nums[curr] , nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2 :
            nums[p2] , nums[curr] = nums[curr] , nums[p2]
            p2 -= 1
        else:
            curr += 1
    return nums 
arr = [ 2 , 1 , 0 , 1, 2, 0]       
# result = sortColors(arr)
# print("Sorted Colors " , result)    

#17.RotateArr#
# Tc is O(n) , Sc is O(1) #
def reverseArr(arr , start , end):
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1 
    return arr    
def rotateARR(arr , k) :
    n = len(arr)
    k = k % n
    reverseArr(arr , 0  , n-1)
    reverseArr(arr , 0  , k-1)
    reverseArr(arr , k , n-1)
    return arr 

arr = [ 2 , 3, 4 , 5, 7 , 8 , 10 ]
k = 2
# result = rotateARR(arr , k)
# print("Rotated k Arr" , result )


#18.ConsecutiveOnes#
# Tc is O(n) , Sc is O(1) #
def consecutiveOnes(nums) :
    maxCount = 0 
    count = 0 
    for num in nums :
        if num == 1 :
            count += 1
            maxCount =  max(maxCount , count)  
        else:
            count = 0
    return maxCount
arr = [ 1 , 1, 1 , 0 ,0 , 1, 1, 3, 1, 0]    
# result = consecutiveOnes(arr)    
# print("The Consecutive Ones is " , result )  



##*SymmetricPairs*##
# Tc is O(n^2) , Sc is O(k) #
def symmetricPairs(arr):
    n = len(arr)
    symmetric = []
    for i in range(n) :
        for j in range(i+1 , n):
            if arr[j][0] == arr[i][1] and arr[j][1] == arr[i][0] :
                symmetric.append((arr[i][1] , arr[i][0]))
    return symmetric            
arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]                
result = symmetricPairs(arr)
# print(result)


##*ToFindtheMaxElementInSubARR*##
# Tc is O(n) , Sc is O(k) #
def findMaxElementInSubarrays(arr , k):
    n = len(arr)
    result = []
    for i in range(n-k+1):
        max_val = max(arr[i:i+k])
        result.append(max_val)
    return result 
arr = [1 ,2, 3, 4, 5, 6]   
k = 3 #size of Subarr 
result = findMaxElementInSubarrays(arr , k) 
# print("The Maximum Element In SubArray of K size is ", result )


##*ReplaceNonCoprimeWithLCM*##
## Non Coprime == gcd is greater than 1 ##
# Tc is O(n^2) , Sc is O(n) #
class Solution(object):
    def replaceNonCoprimes(self, nums):
      n = len(nums)
      result = []
      nums.reverse()
      for num in nums :
        result.append(num)
        while len(result) > 1  and self.gcd(result[-1], result[-2]) != 1 :
            last = result.pop()
            second_last = result.pop()
            result.append(self.lcm(last , second_last))
      return result[::-1]   
         

    def gcd(self , a , b):
        while b!= 0:
            a , b = b , a % b 
        return a      
    def lcm(self , a, b):
        if b == 0 :
            return a
        return abs(a*b)//self.gcd(a, b) 
# nums =[6,4,3,2,7,6,2]
# Output=[12,7,6]


##*ClosestNumInUnsortedARR*##
# Tc is O(n^2) , Sc is O(1) #
def closestNumInArr(arr , k):
    arr.sort()
    n = len(arr)
    maxHeap = float('inf')
    for i in range(n):
        for j in range(i+1 , n):
            if abs(arr[i] - arr[j]) <= maxHeap :
                maxHeap = abs(arr[i] - arr[j])
                print(arr[i] , arr[j])
    if maxHeap == float('inf') :
        print("None")
arr = [2, 3 , 4 ,6]
k = 0
# resultant = closestNumInArr(arr , k)                 


##*BenchPress*##(CODECHEF)
# Tc is O(nlogn) , Sc is O(1) #
def benchPress(n , r , w_rod , arr):
    totalSum = w_rod
    arr.sort()
    i = 0
    while i < n-1 :
        if arr[i] == arr[i+1]:
            totalSum += 2*arr[i]
            i += 2
        else:
            i += 1    
    if totalSum >= r:
        print("YES")
    else:
        print("NO")    
# testCase = int(input("Enter No. of Tests :"))
# while testCase :
#     testCase -= 1
#     numweights , requiredWeight , rodWeight = map(int , input().split() )
#     arr = list(map(int , input().split()))
    # benchPress(numweights , requiredWeight , rodWeight , arr )     


#Inputs>> 
# no. of weights - 6 
# requiredWeight - 100
# Rodweight - 40 
# avaialbleWeightBits = 10, 10, 10, 10, 10, 10
#Outputs>>
#YES (left side>> 30(10, 10 , 10) And right side>> 30(10, 10, 10) : RIGHT CONFIG )


##*PutsZeroesAtTheEndOfArray*##
# Tc is O(n) , Sc is O(n) #
def putsZeroesAtTheEndOfArray(arr):
    nonZero = []
    zero = 0
    for i in range(len(arr)):
        if arr[i] != 0 :
            nonZero.append(arr[i])
        else:
            zero +=  1   
    nonZero.extend([0] * zero)
    return nonZero
arr = [4, 0 , 1, 0 , 3, 0]
result = putsZeroesAtTheEndOfArray(arr) 
# print("Zeroes At End" , result )              


##*CountElementsGreaterThanPreviousElements*##
# Tc is O(n) , Sc is O(1) #
def countEle(arr):
    n = len(arr)
    i = 0 
    count = 1
    while i < n-1 :
        if arr[i] < arr[i+1]:
            count += 1
        i += 1
    return count 
arr = [ 7 , 4, 8 , 2, 9] 
result = countEle(arr)     
# print("Count of Elements Greater than Previous Ele" , result )  


##*CountSundayGivenWeekDays*##
# Tc is O(n) , Sc is O(1) #
def countSunday(startDay , n):
    weekDays = ["Mon" , "Tues" , "Wednes", "Thurs" , "Fri" , "Satur" , "Sun"]
    indexOfStartDay = weekDays.index(startDay)
    indexOfSunDay = 6
    remainingDays = (indexOfSunDay - indexOfStartDay) % 7
    if n < remainingDays :
       return "Not Possible"
    days =  n - remainingDays   
    count = 1 + (days // 7)
    return count    
start_day = 'Wednes'
total_days = 30
sundays = countSunday(start_day, total_days)
# print("Number of Sundays", sundays)        


##*FineChargeOnOddAndEvenVehicleAccordingToDate*##
# Tc is O(n) , Sc is O(1) #
def fineCharge(vehicles , date):
    n = len(vehicles)
    charge = 0 
    if (date % 2 == 0):
        for i in range(n):
            if (vehicles[i] % 2) != 0 :
                charge += 200 
    else:
        for i in range(n):
            if (vehicles[i] % 2 ) == 0 :
                charge += 200
    return charge  
vehicles = [5 , 2 , 3 , 1] 
date = 12              
result = fineCharge(vehicles , date)
# print("Fine By Odd or Even Vehicles Based on Even or Odd Date" , result )


##*ConvertSumOfNumIntoSingleDigit*##
# Tc is O(n) , SC is O(1) #
def convertSumOfNumInSingle(n):
    sum = sumOfNum(n)
    while sum > 9 :
        sum = sumOfNum(sum)
    return sum 
def sumOfNum(n):    
    sum = 0
    while n > 0 :
        digit = n % 10 
        sum += digit 
        n = n //10
    return sum   
n = 987654321      
result = convertSumOfNumInSingle(n)
# print("Convert Sum into Single Digit " , result )


##*CONVERT_NUM TILL ITS SQUAREsSUM ENDS TO 1 *##
## Tc is O((logn)^2) , Sc is O(n)  ##
class Solution(object):
    def isHappy(self, n):
        while n > 1:
            n = self.sumNumber(n)
        if n == 1:
            return True 
        else:
            return False    
    def sumNumber(self, n):
        sqre = 0 
        while n > 0 :
            lastDigit = n % 10
            sqre += pow(lastDigit , 2)
            n = n//10
        return sqre




##*NearestSmallestNumberInUnsortedARr*##
# Tc is O(n) , Sc is O(n) #
def small_nearestNum(arr):
    stack = [] 
    result = []
    for i in range(len(arr)):  
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if not stack :
            result.append(-1)
        else:
            result.append(stack[-1])    
        stack.append(arr[i])    
    return result 
arr = [ 1 , 6, 4 , 10 , 2 , 5]
res = small_nearestNum(arr)
# print("Nearest Smaller Num " , res)        
#Input-[1 ,6 , 4, 10 , 2, 5]
#Output-[-1 , 1 , 1 , 4 , 1 , 2]


##FactorsBecomeNumber##
# Tc is (n+k) , Sc is O(n) #
def factorsBecomeNum(num):
    resultant = []
    stack = []
    for i in range(9 , 2 , -1):
            while num % i == 0 :
                stack.append(i)
                num = num / i 
    if num != 1 :
        return -1            
    while stack :
        resultant.append(stack.pop())
    res = map(str , resultant)   # converting arr into string list  
    return ''.join(res)            
num = 100     #input = 100 (100 % 5 == 0 , 20 % 5 == 0 , 4 % 4 == 0 )
result = factorsBecomeNum(num) #output ( [5 , 5, 4] => 455 )
# print("Factors Become Complete Num " , result  )


##RequiredPipesForBalancingWaterFlow##
# Tc is O(n) , Sc is O(1) #
def requiredPipes(outgoing , incoming , r ):
    value  = 0 
    outgoSum = 0 
    incomeSum = 0 
    for num in outgoing :
       outgoSum += num-2
    for num in incoming :
        incomeSum  += num-2
    if incomeSum == outgoSum :
        return "BALANCE"    
    if outgoSum > incomeSum:
        value = outgoSum - incomeSum 
        value += 2
        return f"-{value}"
    else:
        value = incomeSum - outgoSum 
        value += 2
        return value               
n = [85 , 75 , 95] #OutgoingPipe
m = [70 , 80 , 45] #IncomingPipe
r = 2              #RustFactor
resultant = requiredPipes(n , m , r)
# print("Pipes are ", resultant)


##*EquillibriumIndex_WhoseLeftandRightSUMisEqual*##
# Tc is O(n)  , Sc is O(n) #
def equIndex(arr):
    n = len(arr) 
    leftSum = [0]*n 
    rightSum = [0]*n
    leftSum[0] = arr[0]
    rightSum[n-1] = arr[n-1]
    for i in range(1 , n):
        leftSum[i] = leftSum[i-1] + arr[i]
    for i in range(n-2 , -1 , -1):
        rightSum[i] = rightSum[i+1] + arr[i] 
    for i in range(n):
        if leftSum[i] == rightSum[i]:
            return i 
arr = [-7, 1, 5, 2, -4, 3, 0]
index = equIndex(arr)
# print("Equilibrium Index is:" , index)                   
#input = [ -7 , 1, 5, 2 ,-4 , 3, 0]
#output - [-7+1+5 = -1] , [-4+3+0 = -1] So , EquIndexis[2] == 3


##*ReplaceARRbyRankOfArray*##
# Tc is O(nlogn) , Sc is O(n) #
def rankOfUnsortedARR(arr):
    sorted_uniqueEle = sorted(set(arr))
    rank_dict = {}
    for rank in range(len(sorted_uniqueEle)):
        value = sorted_uniqueEle[rank] #{2 , 6, 15 ,20 , 26 , 98}
        rank_dict[value] = rank + 1 #{2:1 , 6:2 , 15:3 , 20:4 , 26:5 , 98:6}
    rankedArr = []    
    for num in arr:
        rankedArr.append(rank_dict[num])
    return rankedArr   
arr = [20 , 15 , 26 , 2 , 98 ,6 , 2]  
result = rankOfUnsortedARR(arr)
# print("Replaced The Elements According to Sorted Rank " , result )
#inputs=[20 , 15 , 26 , 2 , 98 ,6 , 2]
#outputs=[4 , 3, 5 , 1 , 6 , 2  , 1] #2 is 1st ranker(sorted Manner)



##FINDRANKEDINDESCENDINGUSINGSTACKPOP##
def indexedMountain(arr):
    res = []
    for num in arr:
        res.append(num)
    result = []  # Store the indices of the max elements
    while len(res) > 0:
        indexMaxNum = arr.index(max(res))  # Find index of the max element from original arr
        print(indexMaxNum)
        result.append(indexMaxNum)  # Store the index
        res.pop(res.index(max(res)))  # Remove the max element from res
    
    return result

arr = [2, 4, 6, 1, 8, 5]
result = indexedMountain(arr)
print(result)



##*GetMaxContainerIn_K_PriceValue*##
# Tc is O(2^n * n^2) , Sc is O(n * 2^n) #
from itertools import combinations
def getMaxContainer(prices , containers , k):
    maxContainer = 0
    for r in range(1 , len(prices)+1):
        for indices in combinations(range(len(prices)) , r) :
            currPriceSum = 0 
            for i in indices :
                currPriceSum += prices[i]
            if currPriceSum <= K :
                    currContainerSum = 0 
                    for i in indices :
                        currContainerSum += containers[i]
                    if currContainerSum > maxContainer:
                        maxContainer = currContainerSum 
    return maxContainer 
prices = [10, 10, 40, 50, 90]
containers= [10, 20, 20, 50, 150]
k = 105
result = getMaxContainer(prices , containers , k)
# print("Get Max Containers" , result )    
#Input >
# price = [10, 10, 40, 50, 90]
# container =[10, 20, 20, 50, 150]
# k = 105 
# Output = 170 [10 + 90 = 100 at index 1 and 4 and getting its corresponding container size 20 + 150 = 170 ]


##BasedOnFrequencyReturnARR##
# Tc is O(n) , Sc is O(n) #
from collections import Counter
import heapq
def getcount(arr):
    n = len(arr)
    count = Counter(arr)
    res = (heapq.nlargest(n, count.keys() , count.get))
    print(' '.join(map(str , res)))

# testcase = int(input("Enter testcases")) 
# while testcase:
#     inputs = int(input("enter inputs")) 
#     arrlist = list(map(int , input("list").split())) 
#     getcount(arrlist)
#     testcase = testcase - 1


# ConversionFromRomanToInteger#
# Tc is O(n) , Sc is O(k) #
class Solution(object):
    def romanToInt(self, s):
        romanMap = {
            'I' : 1 ,
            'V': 5  , 
            'X': 10 ,
            'L': 50 ,
            'C': 100 , 
            'D': 500 ,
            'M': 1000 ,
        }

        s = reversed(s)
        prevVal = 0
        totalVal = 0
        for char in s :
           currVal = romanMap[char]
           if currVal < prevVal :
             totalVal -= currVal 
           else:
              totalVal += currVal
           prevVal = currVal 
        return totalVal      
             

##ADD BINARY DIGITS##
# TC is O(n) , Sc is O(n) #
class Solution(object):
    def addBinary(self, a, b):
        i = len(a)-1
        j = len(b)-1
        carry = 0 
        result = []
        while i >= 0 or j >= 0 or carry : 
            if i >= 0 :
                digit_a = int(a[i])
            else:
                digit_a = 0
            if j >= 0 :        
                digit_b = int(b[j])
            else:
                digit_b = 0 
            total = digit_a + digit_b + carry 
            carry = total // 2
            result.append(str(total % 2))
            i -= 1
            j -= 1    

        return ''.join(reversed(result))    



#19.SpiralMatrix#
# Tc is O(n*m) , Sc is O(n*m) #
def spiralMatrix(arr):
    left = 0
    right = len(arr[0]) -1
    top = 0
    bottom = len(arr) - 1
    result = []
    while left < right and top < bottom :
        for i in range(left , right + 1):
            result.append(arr[top][i])
        top += 1
        for i in range(top , bottom + 1):
            result.append(arr[i][right])
        right -= 1
        if top < bottom :
            for i in range(right , left - 1 , - 1):
                result.append(arr[bottom][i])
            bottom -= 1
        if left < right :
            for i in range(bottom , top - 1 , -1):
                result.append(arr[i][left])
            left += 1
    return result  
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = spiralMatrix(arr)
# print("SpiralMatrix", result )


#20.MatrixDiagonalSum#
# Tc is O(n) , Sc is O(1) #
def matrixDiagonalSum(arr):
    n = len(arr) 
    res = 0
    for i in range(n):
        res += arr[i][i]
        res += arr[i][n-i-1]
    if n % 2 :
        res -= arr[n//2][n//2]
    return res         
arr = [[1, 2, 3 , 0], [4, 5, 6 , 0], [7, 8, 9 , 0] , [11, 12, 13 , 0]]
# result = matrixDiagonalSum(arr)
# print("Matrix Diagonal Sum " , result )

#21.CountNegInsortedMatrix#
# Tc is O(n+m) , Sc is O(1) #
def countNegInMatrix(arr):
    rows = len(arr[0])
    cols = len(arr)
    i = 0 
    j = rows - 1
    count = 0 
    while i < cols and j >= 0 :
        if arr[i][j] < 0 :
            count += cols - i 
            j -= 1
        i  += 1
    return count 
arr = [ [1, 2, 3, -4],
    [5, 6, -7, -8],
    [9, 10, -11, -12]]
# result = countNegInMatrix(arr)
# print("Count Neg Num " , result )

#22.RichestCustomerWealth#
# Tc is O(n*m)  , Sc is O(1) #
def richestWealth(nums):
    total = 0 
    maxWealth = 0 
    for num in nums :
        total = sum(num)
        maxWealth = max(maxWealth , total)
    return maxWealth
arr = [[1, 2, 3, -4],
    [5, 6, -7, -8],
    [9, 10, -11, -12]]    
# result = richestWealth(arr)
# print("Richest wealth " , result )        
    
#23.ToeplitzMatrix#
# Tc is O(n*m) , Sc is O(1) #
def toeplitzMat(arr):
    rows = len(arr) 
    cols = len(arr[0])
    for i in range(rows-1):
        for j in range(cols-1):
            if arr[i][j] != arr[i+1][j+1]:
                return False 
    return True 
arr = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# result = toeplitzMat(arr)    
# print("Toeplitz Mat " , result )            

#24.RotateImage#
# Tc is O(n*m) , Sc is O(1) #
def rotateImg(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1 , n):
            arr[i][j] , arr[j][i] = arr[j][i] , arr[i][j]
    for i in range(n):        
        arr[i] = list(reversed(arr[i]))      
    return arr 
mat = [[1, 2, 3 ], [4, 5, 6 ], [7, 8, 9 ]]      
# result = rotateImg(mat)
# print("Matrix is Rotated" , result )

#25.TransposeMatrix#
# Tc is O(n*m) , Sc is O(n*m)#
def transposeMat(mat):
   rows = len(mat)
   cols = len(mat[0]) 
   res = [[0]* rows for _ in range(cols)]
   for i in range(rows) :
        for j in range(cols):
            res[j][i] = mat[i][j]
   return res    
mat = [[1,2,3],[4,5,6],[7,8,9]]
# result = transposeMat(mat)
# print("Transposal Matrix  " , result )       

#26.SetMatrixZeroes#
# Tc is O(n*m) , Sc is O(1) #
def setMatZeroes(arr):
    col0 = 1 
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0 :
                arr[i][0] = 0 
                if j != 0 :
                    arr[0][j] = 0
                else:
                    col0 = 0 
    for i in range(m-1 , -1 , -1):
        for j in range(n-1 , 0 , -1):
            if arr[i][j]!= 0 :
               if arr[i][0] == 0 or arr[0][j] == 0 :
                 arr[i][j] = 0
    if arr[0][0] == 0 :
        for j in range(n):
            arr[0][j] = 0

    if col0 == 0 :              
        for i in range(m) :
            arr[i][0] = 0 

    return arr 

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# result = setMatZeroes(matrix)
# print("Set matrix" , result )

#27.Reshape#
#Tc is O(m*n) , Sc is O(m*n) #
def reshapeMat(mat, r ,c):
    m = len(mat)
    n = len(mat[0])
    res = [[0]*c for _ in range(r)]
    originalLen = m * n 
    if originalLen != r*c :
        return mat 
    else :
        for i in range(originalLen):
            res[i//c][i%c] = mat[i//n][i%n]
    return res 
mat = [[1,2],[3,4]]
# result = reshapeMat(mat , 1, 4 )
# print("Reshaped" , result  )               

#28.FlippingImg#
# Tc is O(m*n) , Sc is O(1) #
def flipImg(mat):
    n = len(mat)
    for i in range(n):
        mat[i] = list(reversed(mat[i]))
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 :
                mat[i][j] = 0 
            else:
                mat[i][j] = 1
    return mat 
mat = [[1,1,0],[1,0,1],[0,0,0]]  
# result = flipImg(mat)
# print("Flpi Image " , result )                         


##*FormUpperTraingle*##
# Tc is O(n^2) , Sc is O(1) #
def upperTriangle(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i > j :
               mat[i][j] = 0    #   if mat[i][j] != 0 
    return mat                  #     return False
mat = [                         # return True 
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]    
result = upperTriangle(mat)
# print("Upper Triangle " , result )               


##*FormLowerTraingle*## 
# Tc is O(n^2) , Sc is O(1) #
def lowerTraingle(mat) :
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i < j :
                mat[i][j] = 0 # To check mat[i][j] != 0 return False 
    return mat                # return True 
mat = [
     [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
] 
result = lowerTraingle(mat)
# print("Lower Traingle " , result ) 

##*MediansOfRowIn2DMatrix*##
# Tc is O(n*n) , Sc is O(k) #
def median(matrix):
    medians = []
    for row in matrix :
        sortedRow = sorted(row)
        n = len(sortedRow)
        if n % 2 == 1 :
            median = sortedRow[n//2]
        else:
            median = (sortedRow[n//2 - 1] + sortedRow[n//2]) / 2 
        medians.append(median)
    return min(medians)         
matrix = [ [1, 3, 2, 4],
    [2, 5, 1, 4],
    [4, 3, 1, 2],
    [5, 1, 4, 3]
    ]
result = median(matrix)
# print("Median Of Row In Matrix" , result )    


##CountOnesInRowWise##
# Tc is O(n) , Sc is O(k) #
def countOnesIn2DMat(mat):
    maxCnt  = 0 
    result = []
    for num in mat :
        totalCnt = sum(num)
        # maxCnt = max(maxCnt , totalCnt)
        result.append(totalCnt)    
    return result 
mat = [[1,0,1],
       [0,1,1],
       [0,1,0]]    
# result = countOnesIn2DMat(mat)
# print(result)


##*EncryptStringUsing2DMat*##
# Tc is O(n^2) , Sc is O(n^2) #
import math
def encryptStrIn2DMat(string) :
    n = len(string)
    rows = math.ceil(math.sqrt(n)) #3
    cols = math.ceil(n // rows)#4
    mat = [['']* cols for _ in range(rows)] #row=4 , col = 3(4*3)
    index = 0 
    for i in range(rows):
        for j in range(cols):
            if index < n :
                mat[i][j] = string[index]
                index += 1
            else:
                mat[i][j] = "" 
                print(mat)
    encryptStr = ""            
    for j in range(cols):
        for i in range(rows):
            if mat[i][j] != '':
                encryptStr += mat[i][j]     
    return encryptStr
input_string = "PLEASESAVEME"
# result  = encryptStrIn2DMat(input_string)
# print("Encrypted Str", result)
    


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math
def encryptstr(string):
    n = len(string)
    col = math.ceil(math.sqrt(n))  #3
    row = math.ceil(n / col) #4
    arr = [[0]*col for _ in range(row)]  #3*4 (row value inside col and col val inside row hota h )
    index = 0
    for i in range(row):
        for j in range(col):
            if index < n :
                arr[i][j] = string[index]
                index += 1
    print(arr) 
    encrypt = ""
    for j in range(col):
        for i in range(row):
            encrypt += arr[i][j]
    return encrypt            
    
string = "ABCDEFGHIJKL"    
res = encryptstr(string) 
print(res)
    
    
    

#2D find greater route moving only top to bottom or left to right #
# Tc is O(m+n) , Sc is O(1) #
def _2DMatrix(arr):
    top = 0 
    left = 0 
    bottom = len(arr)-1 
    right = len(arr[0])-1
    result = arr[top][left]
    while top < bottom or left < right :
        if top < bottom and left < right :
           if arr[top+1][left] > arr[top][left+1]:
              top += 1  #down movement 
           else:
              left += 1   #right movement
        elif top < bottom :
            top += 1
        else:
            left += 1
        result += arr[top][left]
    return result           

matrix = [[1 , 2, 3 , 4], [14 , 15, 16 , 17],[7 , 8, 3 , 22],[9 , 10 , 1 , 19]]
result = _2DMatrix(matrix)
print("Maximum Values with top bottom or left right Route" , result )
#---Taking 2D Matrix Input---#
# rows , columns = map(int , (input("Enter rows and columns: ").split()))
# matrix = []
# for i in range(rows):
#     rows = []
#     for j in range(columns):
#         element = int(input())
#         rows.append(element)
#     matrix.append(rows)
# print("Matrix is Formed") 
# print()   
# for row in matrix :
#     print(row)


#---Taking 2D Matrix Input ----#
# rows , columns = map(int , (input("Enter rows and columns: ").split()))
# matrix = []
# for i in range(rows):
#     row = list(map(int , input("Enter elements  ").split()))
#     matrix.append(row)
# print("Matrix is Formed") 
# print()   
# for row in matrix :
#     print(row)





#29.ReverseStr#
# Tc is O(n) , Sc is O(n) #
def reverseStr(string):
    string = list(string)
    left = 0 
    right = len(string) - 1
    while left < right :
        string[left] , string[right] = string[right] , string[left]
        left += 1
        right -= 1
    string = ''.join(string)
    return string
string = "hello"
# res = reverseStr(string)
# print("Reversed string " , res)         



#30.FirstUniqueCharInStr#
# Tc is O(n) , Sc is O(n) #
from collections import Counter 
def firstUniqueChar(string):
    charCount = Counter(string)
    for index, char in enumerate(charCount):
        if charCount[char] == 1 :
            return char, index 
    return -1 
string = "leetcode"
# result = firstUniqueChar(string)
# print("FirstUnique Char" , result )
          
#31.ReverseWordsInStr#
# Tc is O(n) , Sc is O(n) #
def reverseWordsInStr(string):
    words = string.split()
    reverse = words[::-1]
    newStr = ' '.join(reverse)
    return newStr
string = "the sky is blue" 
result = reverseWordsInStr(string)
# print("Reversed Words : " , result )     


#32.LengthOfLastWords#
# Tc is O(n) , Sc is O(n) #
def lengthLastWords(string):
    words = string.split()
    lastword = words[-1]
    return len(lastword)
string = "Tanu is good and smart women"
# result = lengthLastWords(string)
# print("Length of last String" , result)

#33.LongestCommonPrefix#
# Tc is O(n*m) , Sc is O(k) #
def longestCommonPrefix(string):
    common = []
    if not string :
        return []
    string.sort()
    firstStr = string[0]
    lastStr = string[-1]
    for i in range(len(firstStr)):
        if i < len(lastStr) and firstStr[i] == lastStr[i] :
            common.append(firstStr[i])
        else :
            break 
    return ''.join(common)
string = ["flower","flow","flight"]
# result = longestCommonPrefix(string)
# print("Longest Common Prefix : " , result)             

#34.LongestSubStr#
# # Tc is O(n) , Sc is O(n) #
def longestSubstr(string):
    n = len(string)
    charset = set()
    maxLen = 0 
    left = 0 
    for right in range(n):
        if string[right] in charset :
            charset.remove(string[left])
            left += 1
        charset.add(string[right])
        maxLen = max( maxLen , right - left +1 )
    return maxLen      
string = "abcabcbb"    
# result = longestSubstr(string)   
# print("LongestSubstr" , result )  

#35.JewelsAndStones#
# Tc is O(n+m) , Sc is O(n) #
def jewelAndStones(jewels , stones):
    jewelset = set(jewels)
    count = 0
    for s in stones:
        if s in jewelset:
            count += 1
    return count 
jewels = "aA"
stones = "aAABBBb"
# result = jewelAndStones(jewels , stones)
# print("Jewels And Stones" , result )            


##Find the Index of the First Occurrence in a String##
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def strStr(self, haystack, needle):
      if ( needle == "") :
        return 0 
      len_n = len(needle)
      len_h  = len(haystack)
      for i in range(len_h - len_n + 1):
        if haystack[i:i+len_n] == needle :
            return i 
      return -1             


#36.ValidAnagram#
# Tc is O(2n) , Sc is O(2n) #
from collections import Counter
def validAnagram(str1 , str2):
    countstr1 = Counter(str1)
    countstr2 = Counter(str2)
    if countstr1 == countstr2:
        return True 
    else :
        return False 
str1 = "anagram"
str2 = "nagara"
# result = validAnagram(str1 , str2 )
# print("ValidAnagram is" , result )

#37.ReverseVowels#
# Tc is O(n) , Sc is O(1) #
def reverseVowels(string):
    vowels = "AEIOUaeiou"
    left = 0 
    right = len(string) - 1
    newStr = list(string)
    while left < right :
        while left < right and newStr[left] not in vowels :
            left += 1 
        while left < right and newStr[right] not in vowels :
            right -= 1 
        newStr[left] , newStr[right] = newStr[right] , newStr[left]    
        left += 1
        right -= 1
    return ''.join(newStr)               
string = "hello"
# result = reverseVowels(string)
# print("Reverse vowels :" , result )

#38.ValidPalindrome#
# Tc is O(n) , SC is O(n) #
def sanitizeStr(string):
    sanitize = ""
    for char in string :
        if char.isalnum():
            sanitize += char.lower()
    return sanitize 
def validPalindrome(string):
        newstring = sanitizeStr(string)
        left = 0
        right = len(newstring) - 1
        while left < right :
            if newstring[left] != newstring[right] :
                return False
            left += 1
            right -= 1
        return True 
string = "race a car"
# result = validPalindrome(string)
# print("ValidPalindrome" , result )       

#39.IsomorphicStr#
# Tc is O(n) , Sc is O(n)#
def isomorphicStr(s1 , s2):
    if len(s1) != len(s2):
        return False 
    map_s1_to_s2 = {}
    map_s2_to_s1 = {}
    for char_s1 , char_s2 in zip(s1 , s2):
        map_s1_to_s2.setdefault(char_s1 , char_s2)
        map_s2_to_s1.setdefault(char_s2, char_s1)
        if map_s1_to_s2[char_s1] != char_s2 or map_s2_to_s1[char_s2] != char_s1:
            return False
    return True 
s2, t2 = "foo", "bar"
# print(isomorphicStr(s2, t2))  # Output: False            

#40.RedistributeStr#
# Tc is O(n) , Sc is O(n) #
from collections import Counter
def redistributeStr(words):
    charCount = Counter()
    n = len(words)
    for w in words :
      charCount.update(w) 
    for count in charCount.values() :
        if count % n != 0 :
            return False
    return True          
string = ["abc" , "bc", "aabc"]
# result = redistributeStr(string)
# print("redistribute Make Equal :" , result )

#41.BalancedStr#
# Tc is O(n) , Sc is O(1) #
def balancedStr(string):
    count = 0 
    r = 0 
    n = len(string)
    for i in range(n):
        if string[i] == "R":
            r += 1
        elif string[i] == "L":
            r -= 1
        if r == 0 :
            count += 1
    return count 
string = "RLRLRLLL"
# result = balancedStr(string)
# print("Split balanced String" , result)                     


##*LongestCommonSubsequences*##

# Using Memoization APP #
# Tc is O(m*n) , Sc is O(m*n) #
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
       m = len(text1) 
       n = len(text2) 
       memo = [[None] * (n + 1) for _ in range(m + 1)]
       return self.funcOfLCS(m-1 , n-1 , text1 , text2 , memo)

    def funcOfLCS(self , i , j , str1 , str2 , memo):
        if memo[i][j] is not None:
            return memo[i][j]
        if i < 0 or j < 0 :
            memo[i][j] = 0
        elif str1[i] == str2[j]:
            memo[i][j] = 1 + self.funcOfLCS( i-1 , j-1 , str1 , str2 , memo)
        else:
            memo[i][j] = max(self.funcOfLCS(i-1 , j , str1 , str2 , memo ) , self.funcOfLCS(i , j-1 , str1 , str2 , memo))

        return memo[i][j]

# Using Bottom Up APP #
# Tc is O(m*n) , Sc is O(m*n)#
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
       m = len(text1) 
       n = len(text2) 
       dp = [[0] * (n + 1) for _ in range(m + 1)]
       for i in range(1 , m+1):
         for j in range(1 , n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
       return dp[m][n]

##*ConvertStr1ToStr2*##
# Tc is O(m*n) , Sc is O(m*n)
def convertStr1ToStr2(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    lcs_length = funcOfLCS(s1 , s2)
    deletions = m - lcs_length
    insertions = n - lcs_length
    return deletions + insertions

def funcOfLCS(text1 , text2):
    m = len(text1)
    n = len(tex2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1 , m+1):
        for j in range(1 , n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])    
    return dp[m][n]             
# Input: 's1' = "abcd", 's2' = "anc"
# Output: 3 (deletions= len(s1)-lcs_length[2 = 4-2] , insertions = len(s2)-lcs_length[1 = 3-2 ] )


##*UnCommonCharInStrings*##
# Tc is O(n) , Sc is O(n) #
def commonCharBtTwoStrings(s1 , s2):
    result = []
    lcs = get_lcs(s1 , s2)
    for char in s1 :
        if char not in lcs :
            result.append(char)
    return ''.join(result)         
def get_lcs(s1 , s2):   
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    lcs = []
    i = m 
    j = n 
    while i > 0 and j > 0 :
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1        
    lcs.reverse()
    return ''.join(lcs)
s1 = "processed"
s2 = "esd"
result =  commonCharBtTwoStrings(s1 , s2)
# print("Common char In Strings :" , result )




##*FindInsertionsForBalancingParanthesis*##
# Tc is O(n) , SC is O(1) #
def findInsertionToBalanceParan(s):
    insertions = 0 
    balance = 0 
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
        if balance < 0 :
            insertions += 1
            balance = 0 
    insertions += balance 
    return insertions  
s = '())))'
result = findInsertionToBalanceParan(s)
# print("Insertions To Balance paranthesis ",result) 

##*EncryptTheString*##
# Tc is O(n) , Sc is O(n) #
def encryptTheString(mapping , string):
    if not string.islower() or ' ' in string :
        return "Invalid Input" 
    encrypt_str = ''
    for char in string :
        encrypt_str += mapping[char]
    return encrypt_str
mapping = {
        'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k',
        'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q',
        'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w',
        's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c',
        'y': 'd', 'z': 'e'
}  
string = "helloworld"
result = encryptTheString(mapping , string)
# print("Encrypted String is" , result )


##*EncryptStrInAsciiVal*##
# Tc is O(n) , Sc is O(n) #
def encryptStr(string, key):
    result = []
    for char in string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            index = (index + key) % 26
            result.append(chr(index + ord('A')))
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            index = (index + key) % 26
            result.append(chr(index + ord('a')))
        elif '0' <= char <= '9':
            index = ord(char) - ord('0')
            index = (index + key) % 10
            result.append(chr(index + ord('0')))
        else:
            result.append(char)  
    return ''.join(result)

string = "ADTU89"
key = 2
result = encryptStr(string, key)
# print("Encrypted String:", result)



##*CountAqua*##
# Tc is O(n) , Sc is O(1) #
def countAqua(string , l):
    n = len(string)
    countA = 0 
    maxi = 0 
    for i in range(n):
        if (i % l == 0 ):
            if maxi < countA :
                maxi = countA
            countA = 0 
        if string[i] == 'a':
            countA += 1
    if maxi < countA :
        maxi = countA
    return maxi 
string = "bbbaaababa"
l = 3
result = countAqua(string , l )
# print("Count Aqua in String" , result)                      

# Inputs>> 
# N = "bbbaaababa" #Total Curtains
# L = 3 #box Contains curtains"Aqua-a"or"Black-b"at a time 
# Ouputs>>
# 3



##*FindFrequentVowels*##
# Tc is O(n) , Sc is O(n + k ) #
import heapq
from collections import Counter
def findFrequentVowels(s):
    count = 0 
    vowelLetter = getVowelsInString(s)
    count = Counter(vowelLetter)
    res = heapq.nlargest(1 , count.keys() , key = count.get )
    if res :
        return res[0]
    else:
        return -1    
def getVowelsInString(s):    
    vowels = "aeiou"
    stack = []
    for i in range(len(s)):
        if s[i] in vowels :
            stack.append(s[i])
    return stack 
s = "xdy"    
result = findFrequentVowels(s)
# print("To Find Frequent vowels In String" , result )             


##CONVERT_NUMTOEXCELTITLE##
# TC is O(n) , Sc is O(n) #
class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0 :
            columnNumber -= 1
            remainder = columnNumber % 26 
            result = chr(remainder + ord('A')) + result 
            columnNumber = columnNumber // 26 
        return result
       

##CONVERT_TITLETONUM##
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def titleToNumber(self, columnTitle):
       result = 0 
       for char in columnTitle :
         result = result * 26 + (ord(char) - ord('A')+1)
       return result  




##*SumOfEachSubstrNotequalTolengthofitsSubstring*##
# Tc is O(n^3) , Sc is O(1) #
def substrSumNotEqualToSubstrlen(string , length):
    count = 0
    n = length 
    arr = list(map(int , string))
    for i in range(n):
        for j in range(i , n):
            substrSum = 0 
            for k in range(i , j+1):
                substrSum += arr[k]
            substrLen = j - i + 1    
            if substrSum != substrLen:
                count += 1
    return count 
string = "20"
length = 2                   
result = substrSumNotEqualToSubstrlen(string , length)
# print("count of sunstr sum not equal to its len of substr :", result )
#input - "201"
# output - 3  #[[0]=len(1)=sum(0) ,[2]=len(1)=sum(2) ,[01]=len(2)=sum(1) ] === 3]



#42.Fibonacci#
#42.1 Using Recursion#
# Tc is O(2^n) , SC is O(1) #
def fibonacci1(n):
    if n == 0 :
        return 0
    elif n == 1 or n == 2:
        return 1 
    else:
       return  fibonacci1(n-1) + fibonacci1(n-2)
# wanna to print Fiboseries #
       
# def print_fibonacci_series(n):
#     for i in range(n):
#         print(fibonacci1(i), end=" ") 
n =  3
# result = fibonacci1(n)
# print("Fibonacci Num" , result)   


#42.2 Using DP#

#42.2.a> Memoization(Top-down Appr) #
# Tc is O(n) , Sc is O(n) #
def fiboByMemo(n , memo):
    result = 0
    if memo[n] is not None :
        return memo[n]
    if n == 1 or n == 2 :
        result = 1
    else:
        result = fiboByMemo(n-1 , memo) + fiboByMemo(n-2  , memo)
    memo[n] = result 
    return memo[n]    

def fibonacci2_a(n):
    memo = [None] * (n+1)
    return fiboByMemo(n , memo)
n =  3        
# result = fibonacci2_a(n)
# print("Fibonacci Num" , result)


#42.2.b> Tabulation( Bottom-up Appr)# Better For large Numbers Calculations
# Tc is O(n) , Sc is O(n) #
def fiboByTabu(n , bottom):
    if n <= 2:
        return n

    bottom[1] = 1
    bottom[2] = 1
    for i in range(3 , n+1):
        bottom[i] = bottom[i-1] + bottom[i-2]
    return bottom[n]    

def fibonacci2_b(n):
    bottom = [None] * (n+1)
    return fiboByTabu(n , bottom)  
n =  12        
# result = fibonacci2_b(n)
# print("Fibonacci Num" , result)


#43.PowerFour#

#43.1 Using Recursion#
# Tc is O(2^n) , Sc is O(1)#
def powerFour1(n):
    if n <= 0 :
        return False
    elif n == 1:
        return True 
    else:
        return n % 4 == 0  and powerFour1(n // 4)
n = 20
# result = powerFour1(n)
# print("Find power Four" , result )        


#43.2 Using Memoization#
#Tc is O(n) , Sc is O(1)#  
def powerFour2(n, memo):
    if memo[n]  is not None :
        return memo[n]
    if n <= 0:
         res = False
    elif n == 1:
        res = True
    else:
        res = n % 4 == 0 and powerFour2(n // 4, memo)
    memo[n] = res
    return memo[n]    

n = 64
memo= [None] * (n+1)
# result = powerFour2(n , memo )
# print("Find power Four:", result)


#44.SumOfDigit#
# Tc is O(2^n) , Sc is O(1)#
def sumOfDigit(n):
  
    if n == 0 :
        return 0
    else:
        return n % 10 + sumOfDigit(n//10)  
n =  4321          
# result = sumOfDigit(n)
# print("Sum Of Digit :" , result )


#45.FindGCD#
# Tc is O(2^n) , Sc is O(1) #
def findGCD(a , b):
    if b == 0 :
        return a
    else :
        return findGCD(b , a%b)      
a = 2 
b = 4       
# result = findGCD(a , b)           
# print("Finding GCD :" , result )              

#46.SumOfSubsets#
# Tc is O(2^n) , Sc is O(2^n + n)# 
def sumOfAllSubsets(arr , i , sum , result ):
    if len(arr) == i :
        result.append(sum)
        return 
    else :
        sumOfAllSubsets(arr , i+1 , sum + arr[i] , result)
        sumOfAllSubsets(arr , i+1 , sum , result )

arr = [1 , 2, 3]
i = 0 
sum = 0
result = [] 
sumOfAllSubsets(arr , i , sum , result )
resultant = list(set(result))
resultant.sort()
# for r in resultant:
#     print(r , end = " ")


##*TogglingBits*##
# Tc is O(n) , Sc is O(1) #
import math
def toggleBits(n):
    index = 0 
    ans = 0 
    while n > 0 :
        if n & 1 == 0 :
            ans += math.pow(2 , index)         
        index += 1
        n = n // 2 
    return int(ans) 
n = 10 
result = toggleBits(n)
# print("Toggled Bits Give ", result )
#Inputs - n = 10 (1010)
# Output - 5  (onToglling gets 0101 == 5)


##*SeatArrangementIfTwoSeatAreFixed*##
# Tc is O(n) , Sc is O(1) # 
def factorial(n):
    res = 1
    if n == 0 or n == 1 :
        return 1
    else:
        while n > 1 :
            res = res * n 
            n -= 1
        return res 
def seatArrangement(n):
    if n > 2:
        return factorial(n - 1) * 2
    elif n == 2 :
        return 2
    else:
        return "Invalid Num"
chairNum = 4
result = seatArrangement(chairNum)
# print("Seat Arranged " , result )


##*CountNonRepeatedDigitsInNum*##
# Tc is O(n) , SC is O(1) #
def countNonRepeatedDigits(n1 , n2):
    count = 0 
    for num in range(n1 , n2+1):
        digits = set(str(num))
        if len(str(num)) == len(digits):
            count += 1
    return count  
n1 , n2 = 11 , 15           
result  = countNonRepeatedDigits(n1 , n2)
# print("Count Non Repeated " , result )            



#47.SearchIn2DMatrix #
# Tc is O(log(m*n)) , Sc is O(1) #
def searchIn2DMat(arr , target):
    m = len(arr)
    n = len(arr[0])
    left = 0
    right = m*n - 1
    while left <= right :
        mid = left + (right - left )// 2
        mid_Ele = arr[mid//n][mid%n] 
        if mid_Ele == target :
            return True   
        elif mid_Ele < target:
            left = mid + 1
        else :
           right = mid - 1
    return False 
arr = [[ 1, 2 ,3 ] , [4, 5, 16] , [7, 8 ,9] ] 
target = 6
# result = searchIn2DMat(arr , target)
# print("Binary search In 2D " , result ) 
                    
##OR 
# Tc is O(log(m*n)) , Sc is O(1) #
def searchIn2D(arr , target):
    n = len(arr[0])
    m = len(arr)
    left = 0 
    right = m * n - 1
    # found = False
    result = []
    while left < right  :
        mid  = left + (right - left) // 2
        midEle = arr[mid//n][mid%n]
        if midEle == target :
            # found = True 
            row = mid // n
            col = mid % n 
            return (row , col)
        elif midEle < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1               
arr = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
] 
target = 19
res = searchIn2D(arr , target)
# if res != -1 :
#     print("found at" , res)
# else:
#     print("not found") 



#48.SearchInsertedPosition#
# Tc is O(logn) , Sc is O(1)#
def SearchInsertedPosition(arr , target):
    i = 0 
    j = len(arr) - 1
    while i <= j :
        mid = i + (j - i )// 2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            i = mid + 1
        else:
            j = mid - 1
    return i
arr = [1 , 2 , 3, 4, 6] 
k = 5  #Output >> 4
# result  = SearchInsertedPosition(arr , k ) 
# print("Searched Inserted Order of Element is : " , result )                    


#49.SearchInRotatedSortedARR#
# Tc is O(logn) , Sc is O(1) #
def searchInRotatedMat(arr , target ):
    i = 0 
    j = len(arr) - 1
    while i <= j :
        mid = i + (j-i )// 2
        if arr[mid] == target :
            return mid 
        if arr[i] <= arr[mid]:
            if arr[i] <= target and target <= arr[mid]:
                 j = mid - 1
            else:
                i = mid + 1
        else:
            if arr[mid] <= target and target <= arr[j] :
                i = mid + 1
            else :
                j = mid  - 1
    return -1 
arr = [ 7 , 8 , 9 , 1, 2, 3 , 4 , 5 , 6]  
k = 9
# result = searchInRotatedMat(arr , k)                    
# print("Sorted Arr " , result )  


##*SearchIndexOfFirstInfiniteInARR*##
# Tc is O(logn) , Sc is O(1) #
def searchInfInArr(arr):
    inf = float('inf')
    i = 0 
    j = len(arr)- 1
    while i <= j :
        mid = i + (j-i) // 2
        if arr[mid] != inf :
            i = mid + 1
        else:
            if mid == 0 or arr[mid-1] != inf :
                return mid
            else:
                j = mid - 1
arr = [2 , 1 , -3 , 5 , 4 , float("inf") , float('inf') , float('inf')]   
result = searchInfInArr(arr) 
# print("Index of First Infinite is " , result )



##SQRT(X) Without using (x ** 0.5)##
# Tc is O(n) , SC is O(1) #
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right 



#50.InsertionInLL#
#AtFront##AtEnd##AtAnyNode#
# Tc is O(1), O(n), O(n) # Sc is O(1), O(1) ,O(1) #
class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def frontInsertionLL(self , new_data ):
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertionAtEnd(self , new_data):
        new_node = Node(new_data)
        temp = self.head
        if temp is None :
            self.head = new_node
        while temp.next :
            temp = temp.next 
        temp.next = new_node 

    def insertionAtAnyNode(self , new_data, prev_node):
        new_node = Node(new_data)
        prev = None 
        new_node.next = prev_node.next 
        prev_node.next = new_node 


    def printList(self):
        temp = self.head
        while temp :
            print(str(temp.data)+ " " , end=" ")
            temp = temp.next  

# listing  =LinkedList()   
# print("Insertion At Front")              
# listing.frontInsertionLL(12)
# listing.frontInsertionLL(11)
# listing.frontInsertionLL(10)
# listing.frontInsertionLL(9)
# listing.frontInsertionLL(8)
# listing.printList()
# print()
# print("Insertin At End")
# listing.insertionAtEnd(15)
# listing.printList()
# print()
# print("Insertion At Any Node")
# listing.insertionAtAnyNode(14 ,listing.head.next.next.next.next)
# listing.printList()



#51.DeletionInLL#
#AtAnyNodeGivenPosition##OfNodeGivenNodeVal,Head##OfNodeGivenNodeVal##NthFromtheEnd#
# Tc is O(n) , O(n), O(n) , O(n),   SC is O(1), O(1), O(1) ,O(1)  #
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 

    def deletionAtAnyNode_Pos(self , pos):
        temp = self.head
        if temp is None :
            return 
        for i in range(pos-1):
            temp = temp .next 
        temp.next = temp.next.next 

    def deletionOfNode_ValandHead(self , val):
        prev = None 
        if self.head is None:
            return 
        else:
            temp = self.head
            while temp :
                if temp.data == val :
                    if prev is None :
                       self.head = self.head.next 
                    else:
                        prev.next = temp.next 
                else:        
                    prev = temp            
                temp = temp.next        
            return self.head

# class LinkedList:
#     def __init__(self , x):
#         self.val = x  

    def deletionOfNode_Val(self , node):
        if node is None :
            return 
        elif node.next is not None:
            node.val = node.next.val 
            node.next = node.next.next 
        else:
            node = None 

    def deleteOfNthNodeFromEnd(self , n ):
        fast = self.head
        slow = self.head 
        for i in range(n):
            fast = fast.next
        if fast is None:
           self.head = self.head.next     
        while fast.next and fast and slow :
            slow = slow.next 
            fast = fast.next
        slow.next = slow.next.next

    def printList(self):
        temp = self.head
        while temp :
            print(str(temp.data)+ " " , end=" ")
            temp = temp.next

# Helper function to append a new node at the end
def append_to_list(linked_list, data):
    new_node = Node(data)
    if linked_list.head is None:
        linked_list.head = new_node
        return
    last = linked_list.head
    while last.next:
        last = last.next
    last.next = new_node

# Create a linked list and populate it
# listing2 = LinkedList()
# append_to_list(listing2, 1)
# append_to_list(listing2, 2)
# append_to_list(listing2, 3)
# append_to_list(listing2, 4)
# append_to_list(listing2, 5)
# print()
# print("Initial List:")
# listing2.printList()
# print()

# # Delete node at position 2
# print("Deleting node at position 2:")
# listing2.deletionAtAnyNode_Pos(2)
# listing2.printList()
# print()

# # Delete node by value 4 with head 
# print("Deleting node with value 4 with head :")
# listing2.deletionOfNode_ValandHead(4)
# listing2.printList()
# print()

# # Delete the 2nd node from the end
# print("Deleting the 2nd node from the end:")
# listing2.deleteOfNthNodeFromEnd(2)
# listing2.printList()


##DELETE DUPLICATES IN SORTED LL##
# TC is O(n) , Sc is O(1)#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None :
            return None
        curr = head
        while curr and curr.next  :
            if (curr.val == curr.next.val) :
                curr.next = curr.next.next
            else:    
                curr = curr.next 
        return head       




#52.ReverseLL#
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def reverseList(self, head):
        curr = head
        next = None 
        prev = None 
        while curr :
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev


#53.MergeTwoSOrtedLL#

#53.1 Using Recursion #
# Tc is O(n) , Sc is O(1)
def mergeSortedLL1(list1 , list2):
    temp = None
    if list1 is None:
        return list2
    elif list2 is None :
        return list1
    else:
        if list1.val <= list2.val :
           temp = list1
           temp.next = mergeSortedLL1(list1.next , list2)
        else:
            temp = list2
            temp.next = mergeSortedLL1(list1 , list2.next)
    return temp 

#53.2 Using DummyList #
# Tc is O(n) , Sc is O(1) #
class Node :
    def __init__(self , val):
        self.val = val 
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 
    def mergeSortedLL2(self , list1 , list2):
        dummyList = Node(0)            
        temp = dummyList 
            
        while list1 and list2 :
            if list1.val <= list2.val :
                temp.next = list1 
                list1 = list1.next 
            else:
                temp.next = list2
                list2 = list2.next 
            temp = temp.next 

        if list1 :
            temp.next = list1
        elif list2 :
            temp.next = list2  

        return  dummyList.next 

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(4)
list2.next = Node(6)
list2.next.next = Node(8)
llists = LinkedList()
resultant = llists.mergeSortedLL2(list1 , list2)
# while resultant :
#     print(resultant.val , end=" ")
#     resultant = resultant.next 

#54.MiddleOfLL#
# Tc is O(n) , SC is O(1)#
class Solution(object):
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and slow and fast.next :
            fast = fast.next.next
            slow = slow.next
        return slow    

#55.PalindromeLL#
# Tc is O(n) , Sc is O(1) #
class Solution(object):
  
  def isPalindrome(self , head):
    if head is None or head.next is None :
        return True
    middle = self.middleOfLL(head)
    head2 = self.halfReversedLL(middle.next)
    result = self.comparisonLL(head , head2)
    return result
     
  def middleOfLL(self, head):
    slow = head
    fast = head
    while fast.next and fast.next.next :
        fast = fast.next.next 
        slow = slow.next 
    return slow

  def halfReversedLL(self,head):
    curr = head
    prev = None 
    next = None 
    while curr :
        next = curr.next 
        curr.next = prev 
        prev = curr
        curr = next 
    return prev

  def comparisonLL(self ,head1 , head2):
    while head1 and head2:
        if head1.val != head2.val :
            return False
        head1 = head1.next
        head2 = head2.next 
    return True                

#56.LinkedListCycle-I#
# Tc is O(n) , SC is O(1) #
class Solution(object):
    def hasCycle(self, head):
        tortoise = head
        hare = head
        while tortoise and hare and hare.next :
            tortoise = tortoise.next 
            hare = hare.next.next 
            if hare == tortoise :
                return True 
        return False      

#57.LinkedListCycle-II#
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def detectCycle(self, head):
        if head is None :
            return None 
        fast = head
        slow = head
        entry = head
        while slow and fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
            if fast == slow :
                while entry != slow :
                    entry = entry.next 
                    slow = slow.next 
                return entry 
                    
#58.MaximumTwinSum#
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def pairSum(self, head):
        sum = 0
        maxSum = 0
        if head is None :
            return 0

        elif head and head.next is None :
            return head.val

        middle = self.middleLL(head) 
        head2 = self.halfReversalHead(middle)
        while head and head2 :
            sum = head.val + head2.val
            maxSum = max(maxSum , sum)
            head = head.next 
            head2 = head2.next 
        return maxSum 

    def middleLL(self , head):
            fast = head
            slow = head
            while fast and fast.next :
                fast = fast.next.next 
                slow = slow.next
            return slow

    def halfReversalHead(self , head):
            next = None
            prev = None 
            curr = head
            while curr :
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next 
            return prev

#59.AddTwoLL#
# Tc is O(n) , Sc is O(n) #
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy 
        carry = 0
        while l1 or l2 or carry :
            sum = carry 
            if l1 :
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val  
                l2 = l2.next
            carry = sum // 10
            temp.next = ListNode(sum%10)
            temp = temp.next 
        return dummy.next   

#60.ODDandEVENLL#
# Tc is O(n) , Sc is O(1) #
class Solution(object):
    def oddEvenList(self, head):
        if head is None :
            return 
        elif head.next is None :
            return head
        else:
            odd = head
            even = head.next 
            evenhead = head.next 
            while even and even.next :
                    odd.next = odd.next.next 
                    odd = odd.next 
                    even.next = even.next.next 
                    even = even.next 
            odd.next = evenhead
        return head            

##*AlternateSumInLL*##
# Tc is O(n) , Sc is O(1)#
def alternateSumInLL(head):
    # If list is empty or one node or two node 
    if head is None or head.next is None or head.next.next is None :
        return head
    curr = head.next.next 
    prev = head    
    while curr :
        curr.data += prev.data
        curr = curr.next 
        prev = prev.next 
    return head 
#input-> 1>2>3>5>6>7    
#output-> 1>2>4>7>9>12

#61.ValidParenthesis#
# Tc is O(n) , Sc is O(n) #
class Solution(object):
    def isValid(self, s):
      stack = []
      openParams = set(["{" , "(" , "["])
      dictionary = {"{" : "}" ,
                   "[" : "]" ,
                   "(" : ")" , }
      for char in s: 
        if char in openParams :
            stack.append(char)            
        elif stack and char == dictionary[stack[-1]]:
            stack.pop()
        else:
            return False    
      return stack == []

#62.MakeStrGreat#
# Tc is O(n) , Sc is O(n) #
class Solution(object):
    def makeGood(self, s):
      stack = []
      for char in s :
        if stack and abs(ord(char)- ord(stack[-1])) == 32 :
            stack.pop()
        else:
            stack.append(char)    
      return ''.join(stack) 


#63.RemoveAllAdjacentDupli#
# Tc is O(n) , Sc is O(n) #
class Solution(object):
    def removeDuplicates(self, s):
      stack = []
      for char in s :
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
      return ''.join(stack)  


#64.ImplementQueueUsingStack#
# Tc is O(n) ,Sc is O(n) #
class MyQueue(object):
    def __init__(self):
        self.stack1 =[]
        self.stack2 = []
        self.front = 0      
           
    def push(self, x):
        if not self.stack1 :
            self.front = x    
        self.stack1.append(x)
    def pop(self):
        if not self.stack2:
            while self.stack1 :
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()        
    def peek(self):
        if self.stack2 :
            return self.stack2.peek()
        return self.front    
    def empty(self):
        return not self.stack1 and not self.stack2


#65.ImplementStackUsingQueue#
# Tc is O(n) , Sc is O(n) #
from collections import deque
class MyStack :
    def __init__(self):
      self.q = deque()
    def push(self , x):
        self.q.append(x)
    def pop(self):
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()    
    def top(self):
        if self.q :
            return self.q[-1]
    def empty(self):
        return not self.q


#66.OnlineStocks#
# Tc is O(n) , Sc is O(n) #
class StockSpanner(object):
    def __init__(self):
        self.stack = []
    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price :
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price , span))    
        return span 

##*ReverseArrayUsingStack*##
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
# print(resultant)     


#67.TimeNeededToBuyTickets#
# Tc is O(n*max(tickets)) , Sc is O(n) #
from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
       time = 0
       q = deque(range(len(tickets)))
       while q :
         indx = q.popleft()
         tickets[indx] -= 1
         time += 1
         if tickets[indx] > 0 :
            q.append(indx)
         if tickets[indx] == 0 and indx ==k :
            break 
       return time      

#68.ProductsOfLastKNum#
# Tc is O(n) , Sc is O(n) #
from collections import deque
class ProductOfNumbers(object):
    def __init__(self):
        self.q = deque([1])
        self.product = 1
    def add(self, num):
        if not num :
            self.q = [1]
            self.product = 1
        else:
            self.product *= num
            self.q.append(self.product)        
    def getProduct(self, k):
        if k >= len(self.q):
            return 0 
        else:
            return self.product//self.q[-k-1]    


 #69.TopKFrequentEle#
 # Tc is O(n) , Sc is O(n) #
from collections import Counter
import heapq
def topKfrequentEle(nums , k):
    if k >= len(nums):
        return set(nums)
    else:
        count = Counter(nums) 
        return heapq.nlargest(k , count.keys() , key = count.get)
nums = [ 2, 2 , 3, 3, 3 ,4, 5]
k = 2    
result = topKfrequentEle(nums , k)
# print("Top K Frequent Elem " , result )


#70.KthClosestEle#
# Tc is O(nlogk) , Sc is O(n) #
from heapq import heappop , heappush 
def kthClosestEle(arr , k , x):
    n = len(arr)
    maxHeap = []
    for i in range(n):
        heappush(maxHeap , (abs(arr[i]- x), arr[i]))
    result = 0
    for i in range(k):
        result = (heappop(maxHeap)[1] )  
    return result 
arr = [2, 4, 5 ,6 , 8]
k = 3
x =  2       
resultant = kthClosestEle(arr , k , x)
# print("KthClosest Ele " , resultant)


##GETCLOSERTO_ZERO-TEMPERATURE##
from heapq import heappush , heappop
import heapq
def closestNum(arr):
    x = 0
    k =1
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap , (abs(arr[i] - x ) , arr[i] if arr[i] >= 0 else float('inf') , arr[i]))
    response = []
    for i in range(k):
        response.append(heapq.heappop(heap)[2])
    return response
        
arr = [ -3, 8, 4, -6 , 3]
result = closestNum(arr)
print(result)



#71.KthClosestPoints#
# Tc is O(nlogn) , Sc is O(n+k) #
import math
from heapq import heappush , heappop
def getDistance(x , y ):
    return math.sqrt(x**2 + y**2)
def kthClosestPoints(points , k):
    result = []
    maxHeap = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        heappush(maxHeap , (getDistance(x , y ), points[i]))
    for i in range(k):
        result.append(heappop(maxHeap)[1])   
    return result 
points = [(1 , 2) , (3, 4) , (5, 6)]
k = 2    
resultant = kthClosestPoints(points , k )
# print("Kth Closest Points ", resultant )


#72.kthSmallestPositiveMissingNum#
# Tc is O(n) , Sc is O(n) #
def kthSmallestPositiveNum(nums):
    numset = set()
    for num in nums :
        if num > 0 :
            numset.add(num)
    for i in range(1 , len(nums) + 2):
        if i not in numset:
            return i     
nums = [1 , 2, 3, 4, 5, 6]
resultant = kthSmallestPositiveNum(nums)
print("KthSmallest Positive Nums" , resultant)                


#**KthMissingInsortedARR**#
# Tc is O(n) , Sc is O(1) #
def KthMissingInsortedARR(nums , k):
    for num in nums :
        if num <= k :
            k += 1
        else:    
            break
    return k   

nums = [1 , 3, 5, 7, 10]
k= 4
resultant  = KthMissingInsortedARR(nums , k )
# print("kth Missing In sorted Arr" , resultant )


#73.CommonEleInThreesortedArr#
# Tc is O(n) , Sc is O(k) #
def commonEleInThreeSortedArr(arr1 , arr2 , arr3):
    n1 = len(arr1)-1
    n2 = len(arr2)-1
    n3 = len(arr3)-1
    i, j , k = 0 , 0 , 0
    common = []
    while i <n1 and j < n2 and k < n3 :
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] <arr2[j] :
            i += 1
        elif arr2[j] < arr3[k] :
            j += 1
        else:
            k += 1
    return common 
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 =[ 3, 4, 15, 20, 30, 70, 80, 120]
# result = commonEleInThreeSortedArr(arr1 , arr2 , arr3 )
# print("Common Elements In three Sorted Arr " , result )                                 


#74.InversionOfAnArr#
# Tc is O(nlogn) , Sc is O(n) #
def inversionOfAnArr(arr , p , q):
    __ , inv_count = mergeSort(arr , p , q)
    return inv_count
def mergeSort(arr , p , q):
    if p < q:
        mid = p + (q-p) // 2
        leftArr, leftCnt  = mergeSort(arr , p , mid)
        rightArr, rightCnt = mergeSort(arr , mid+1 , q)
        mergeArr , mergedCnt = merged(leftArr , rightArr)
        return mergeArr , leftCnt + rightCnt + mergedCnt 
    else:
        return [arr[p]] , 0

def merged(left , right ):
    i = 0 
    j = 0
    count = 0 
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i 
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result , count

nums = [ 2 , 4, 1, 3, 5]
p = 0
q = len(nums) - 1
getInvCount = inversionOfAnArr(nums , p , q)
# print("Number of inversions To sort the Array" , getInvCount)  





##---Extra----##

##*GenerateSeries*##
#Conditions:-
#1.PrimePositions>pow(2)
#2.PerfectSquare>pow(3)
#3.reamining> sum(lastTwo)
# Tc is O(n) , Sc is O(n) #
import math
def isPrime(n):
    if n <=1 :
        return False 
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False 
    return True         

def isPerfectSquare(n):
    if n < 0 :  
       return False 
    sqrtnum = int(math.sqrt(n))
    return sqrtnum * sqrtnum == n

def generateSeries(n):
    powertwo = 1
    powerthree = 1
    arr = [0] * n  # Initialize the array with `n` elements

    for i in range(0, n):
        if isPrime(i + 1):
            arr[i] = powertwo
            powertwo *= 2
        elif isPerfectSquare(i + 1):
            arr[i] = powerthree
            powerthree *= 3
        else:
            arr[i] = arr[i-1] + arr[i-2]

    return arr[n-1]
num = 15
resultant = generateSeries(num)
print("Resultant" , resultant )



##*SwapSingleEleFromArr1andArr2TogetSimilarSumValues*##
#Tc is O(n1 + n2) , Sc is O(n2) #
def swapSingleEle(arr1 , arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff = sum1 - sum2
    if (diff % 2) != 0 :
        return False
    targetDiff = diff // 2
    set2 = set(arr2)
    for num1 in arr1 :
        num2 = num1 - targetDiff 
        if num2 in set2:
            index1 = arr1.index(num1)
            index2 = arr2.index(num2)
            arr1[index1] , arr2[index2] = arr2[index2] , arr1[index1]
            return True 
    return False
arr1 = [4, 1, 2, 1, 1, 2]
arr2 = [3, 6, 3, 3]
# result = swapSingleEle(arr1 , arr2)
# print("Swap the Single  Ele In Arr" , result )        



##*AddingElementsInARR*##
# Tc is O(nlogn) , Sc is O(1) #
def addingEle(arr, elements):
    arr.sort()
    for element in elements:  #comment this for singleEle insertion 
        left = 0 
        right = len(arr) 
        while left < right :
            mid  = left + (right - left) // 2
            if arr[mid] < element:
                left = mid + 1
            else:
                right = mid 
        arr.insert(left , element)
    return arr         
arr = [6, 3, 4, 5, 2]
key = (1 , 7)
result = addingEle(arr, key)
# print("Adding Ele", result)


##GetTwoLegsandFourLegsNumberOfAnimals##
# Tc is O(1) , Sc is O(1) #
def getTwoandFourlegsAnimals(N , L):
    # x + y = N  --Eq1
    # 2x + 4y = L  --Eq2
    # y = (L-2*N)/2(Four Legs) , x = N-y (Two legs)
    x = 0 
    y = 0    
    y = int(((L - 2*N)/2))
    x = N - y 
    return x , y 
# N = int(input("Total Animals"))
# L = int(input("Total Legs"))
# result = getTwoandFourlegsAnimals(N , L)
# print(f'{result[0]} {result[1]}') #space separated Results

##ProfitPercentGainedByTopSuperVisor##
# Tc is O(n) , Sc is O(1) #
def profitPercent(n , m , p):
    while n-1 > 0:
        pval = (p/100) * m
        m = pval
        n = n-1 
    return int(pval)    
n = 4 #number of superVisors tree(A,B,C)
m = 2000 #profitEarnedByLastNode(C)    
p = 50 #Profit(Ineachlevels)
result = profitPercent(n , m , p)  #((10/100) *100 = 10(EarnedByB) , 10/100 * 10 = 1(EarnedByA) ==> 1)
print("Profit gained by A superVisor", result)


##CountOccurenceOfSecondLargestElement##
# Tc is O(n) , Sc is O(n) #
def countOccurrence(n , arr):
    uniqueEle = list(set(arr))
    count = 0 
    if len(uniqueEle) == 1:
        return 0
    secondLargeEle = uniqueEle[-2]    
    for i in range(n):
        if arr[i] == secondLargeEle:
            count += 1
    return count            
# n = int(input("Enter size :"))
# arr = list(map(int , input().split()))
# print(countOccurrence(n , arr))
#    


#Encrypted By +2#
# Tc is O(n) , Sc is O(n) #
def encryptStr(strings):
    encrypt = ""
    for char in strings :
        if char == "Z":
            encrypt += "B"
        else:
            encrypt += chr(ord(char) + 2)
    return encrypt        
words = "ABCD"
result = encryptStr(words)
print(result )


#If odd return 3*N +1 else n/2 till 4 , return ratio#
# Tc is O(logn) , Sc is O(1) #
def isODD(n):
    if (n % 2 == 0) :
        return False
    return True     
def performOperationIFODD(n):
    if (n == 8) :
        return str(1)+":"+"0"
    newVal = 0    
    while n > 4 :
        if isODD(n):
            n = 3*n + 1
        else:
            newVal = n 
            n = n / 2
    firstRatio = int(newVal / 4)
    return str(firstRatio)+":"+"1"
n = 17   
result = performOperationIFODD(n)
print("Ratios are" , result)    



##ExchangeFirstCharToSecondCharAndSecondToFirst##
# Tc is O(n) , Sc is O(n) #
def exchange_FToS_CharandReverse(string,  firstChar , secondChar):
    if not string :
        return []
    s = list(string)
    for i in range(len(s)):
        if s[i] == firstChar:
            s[i] = secondChar
        elif s[i] == secondChar:
            s[i] = firstChar 
    return ''.join(s)           
string = "codebashers"
firstChar = "c"
secondChar = "b"
result = exchange_FToS_CharandReverse(string , firstChar, secondChar)
print(result )


##LeftMonkeysIntree##
#Tc is O(1) , Sc is O(1)#
def leftMonkeys(n, m, p, k, j):
    atePeanuts = j
    ateBananas = k 
    if n<0 or m<0 or p<0 or k<0 or j<0 :
        print('Invalid Input')
    else:
        ateBananas = m // k
        atePeanuts = p // j
        n = n - (atePeanuts + ateBananas)  #return Monkeys Left In Tree
        print("left Monkeys on tree ", n) 
        

n = 20 # Total Monkeys 
m = 12 # Number of banana
p = 12 #Number of Peanuts
k = 2  #AteBananaATaTime
j = 3  #AtePeanutsATaTime
# leftMonkeys(n, m, p, k, j)
  
##CandiesSoldandLeftInJar##
# Tc is O(1) , Sc is O(1) #
def candiesSoldandLeftInJar(N , k):
    input =  0 #candies ordered by customer 
    if input >=1 and input <= 5 :
        print("num of Candies sold" , input)
        print("Num of left Candies" , N-input)
    else:
        print("INVALID INPUT")
        print("Num of left Cnadies " , N) 
N , K = 10 , 5
# result = candiesSoldandLeftInJar(N , K)        


##VennDiagramProblem##
# Tc is O(1) , Sc is O(1) #
def vennDiagram(p1, p2, p3, q, r, e):
    res_abcExactly = e - (p1+p2+p3 - 2*q + r)   # (e = 3x + p1-q + p2-q + p3-q + q + r)
    One_a = int((res_abcExactly / 3)) + (p1-q + p3-q + q) #CompleteCircleA
    return res_abcExactly , One_a
p1 = 30#(A intersects B)
p2 = 26 #(B intersects C)
p3 = 28#(A intersects C)
q = 14#(A , B , C intersects)
r = 43#(Not Inside)
e = 345#(Total)
# result = vennDiagram(p1,p2,p3,q,r,e) #(1.Exactly One of them (only A + only B + Only C)    2. A (One))
# print(f"{result[0]} {result[1]}")


##*ARMSTRONG_NUM*##
# Tc is O(n) , Sc is O(1) #
import math
def numPower(n):
    return math.pow(n , 3)
def armstrongNum(n):
    originalNum = n
    result = 0 
    while n > 0 :
        lastDigit = n % 10 
        cubeNum = numPower(lastDigit)
        result += cubeNum 
        n = n//10
    if result == originalNum:
        return True
    else:
        return False
n = 153       
result = armstrongNum(n)
# print("Is Armstrong Num ", result)


##*PythagoreanTriplet*##
# Tc is O(n) , Sc is O(1) #
def PythagoreanTriplet(a , b , c):
    a , b , c = sorted([a , b , c])
    return a**2 + b**2 == c**2


##*PrimeNumber*##
# Tc is O(n) , Sc is O(k) #
import math
def primeNum(num):
    if num <= 1 :
        return False
    for i in range(2 , int(math.sqrt(num)) + 1):
        if (num % i)== 0 :
            return False
    return True
def findPrimeInArr(nums):
    resultant = []
    for num in nums :
        if primeNum(num):
            resultant.append(num)
    return resultant

nums = [2, 5 ,3 ,6 , 9 , 11 , 13]      
result = findPrimeInArr(nums)    
# print("Get Prime" , result ) 


##SwappingBtTwoNumWith_Or_WithoutTemp##
# Tc is O(1) , Sc is O(1)#
def swapNum(n1 , n2):
   temp = n1  #n1 = n1 + n2
   n1 = n2    #n2 = n1 - n2
   n2 = temp  #n1 = n1 - n2
   return n1 ,n2
result = swapNum(2 , 3)
# print("Swap" , result )


##ConvertBinaryToDecimal##
# Tc is O(n) , Sc is O(1) #
import math
def convertBinToDeci(n):
    index = 0 
    res = 0 
    while n > 0 :
       lastDigit = n % 10 
       if lastDigit != 0 :
            res += math.pow(2 , index)
       index += 1
       n = n //10
    return int(res)
            
n = 1010                
result = convertBinToDeci(n)
# print("DecimalNum" , result )


##*PATTERNS*##
#1.* * * *
#  * * * *
#  * * * *
#  * * * *
def pattern1(n):
    pat = ""
    for i in range(n):
        for j in range(n):
            pat += " * "
        pat += "\n"
    return pat
# n = int(input("Enter Nums"))        
# result = pattern1(n)
# print(result)

#2. *
#   * *
#   * * *
#   * * * *
def pattern2(n):
    pat = ''
    for i in range(n):
        for j in range(i+1):
            pat += " * "
        pat += "\n"    
    return pat
# n = int(input("Enter Nums"))        
# result = pattern2(n)
# print(result)

#3. * * * * *
#   * * * *
#   * * * 
#   * *
#   *
def pattern3(n):
    pat =''
    for i in range(n):
        for j in range(n-i):
            pat += " * "
        pat += '\n'
    return pat          
# n = int(input("Enter Nums"))        
# result = pattern3(n)
# print(result)

#4. 
# *********
#  ******* 
#   *****  
#    ***   
#     *  
def pattern4(n):
    pat = ""
    for i in range(n):
        for j in range(i):
            pat += " "
        for j in range(2*n - (2*i+1) ) :
            pat += "*"
        for j in range(i):
            pat += " "
        pat += "\n"
    return pat 
# n = int(input("Enter Nums"))        
# result = pattern4(n)
# print(result)                 

#5.
#     *    
#    ***   
#   *****  
#  ******* 
# *********
def pattern5(n):
    pat = ''
    for i in range(n) :
        for j in range(n-i-1):
            pat += " "
        for j in range(2*i+1):
            pat += "*"    
        for j in range(n-i-1):
            pat += " "
        pat += '\n'    
    return pat        
# n = int(input("Enter Nums"))        
# result = pattern5(n)
# print(result)            


## Add the total sum of pyramid(1 , 212 , 32123 , ....)##
def palindrome_pyramid_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        # Construct the increasing part (i to 1)
        increasing_part = ''.join(str(j) for j in range(i, 0, -1))
        # Construct the decreasing part (2 to i)
        decreasing_part = ''.join(str(j) for j in range(2, i + 1))
        
        # Form the full palindrome
        full_palindrome = increasing_part + decreasing_part
        
        # Print the current row's palindrome (optional, for visualization)
        print(full_palindrome)
        
        # Manually sum the digits of the full palindrome
        for digit in full_palindrome:
            total_sum += int(digit)
    
    return total_sum

# Example usage
n = 3  # Height of the pyramid
total_sum = palindrome_pyramid_sum(n)
print(f"The sum of the palindrome pyramid of height {n} is: {total_sum}")



#6.
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
def pattern6(n):
    pat = '' 
    for i in range(n):
        for j in range(n-i-1):
            pat += " "
        for j in range(2*i + 1):
            pat += "*"
        for j in range(n-i-1):
            pat += " " 
        pat += "\n"        
    for i in range(1 , n):           
        for j in range(i):
            pat += " "
        for  j in range(2*(n) - (2*i+1 )) :
            pat += "*"
        for j in range(i):
            pat += " "
        pat += "\n"
    return pat    
n = int(input("Enter Nums"))    
result = pattern6(n)
print(result)                     



## PASCAL's TRIANGLE - I ##
# Tc is O(n^2) , Sc is O(n^2) #
class Solution(object):
    def generate(self, numRows):
       triangle = []
       for i in range(numRows):
         row = [1] * (i+1)
         for j in range(1 , i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
         triangle.append(row)  
       return triangle    


## PASCAL's TRIANGLE - II ##
# Tc is O(n^2) , Sc is O(n^2) #
class Solution(object):
    def getRow(self, rowIndex):
        getTriangle = self.getTri(rowIndex)
        return getTriangle[rowIndex]
    def getTri(self , numRows): 
        triangle = []
        for i in range(numRows+1):
            row = [1] * (i+1)
            for j in range(1 , i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle          





##
from collections import Counter
def countMoves(string):
    res = 0 
    count = Counter(string)
    for char in count :
        res += count[char]//2
    return res    
string = "baabacaa"    
res = countMoves(string) 
# print(res)  


##
def findIsdivisible(nums , n):
 res = 0  
 result = []
 for i in range(n-2):
    for j in range(i+1 ,n-1):
        for k in range(j+1 , n):
            total = nums[i] + nums[j] + nums[k]
            if isDivisible(total):
                result.append([ nums[i] , nums[j] , nums[k]])
                res += 1   

 return res , result                    
def isDivisible(n):
    if n % 5 == 0 :
        return True 
    else :
        return False    

# getDivi = findIsdivisible([3,3,4,7,8] , 5)
# print(getDivi)


##
def printFizz(n):
    for i in range(1 , n+1):
        if isMultOf3(i):
            print("Fizz")

        elif isMultOf5(i):
            print("Buzz")

        elif isMultOf3_5(i):
            print("FizzBuzz")

        else:
            print(i)            
def isMultOf3(n):
    return n % 3 == 0 and n% 5 !=0 
def isMultOf5(n):
    return n%3 !=0 and n % 5 == 0 
def isMultOf3_5(n):
    return n%3==0 and n%5==0
printFizz(15)



##GEtTriangle##
def triangle(trigle):
      res = []
      for sides in trigle :  
        if isValid(sides):
            if sides[0] == sides[1] and sides[1] == sides[2]:
                res.append("Equilateral")
            elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
                res.append( "Isosceles")
            else:
                res.append("None")
        else:
            res.append("None")               
      return res
def isValid(sides): 
   side1, side2, side3 = sides
   return (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2)
trigle = [[2,2,1],[3,3,3],[1,1,3],[1,3,4]]
getTriangle = triangle(trigle)
print(getTriangle)
 

 