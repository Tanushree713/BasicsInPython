## 1. Arrays ##
# 1. Maximum And Minimum Ele #
# TC is O(n) , SC is O(1)
def maxAndmin(arr , i , j):

    if i == j :
        max_val = arr[i]
        min_val = arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]    

    else:
        mid = i + (j - i) // 2   
        max_l , min_l  = maxAndmin(arr , i , mid)
        max_r , min_r = maxAndmin(arr , mid + 1, j ) 
        if max_l < max_r :
            max_val = max_r
        else:
            max_val = max_l

        if min_l < min_r :
            min_val = min_l 
        else:
            min_val = min_r

    return max_val , min_val                      
arr = [ 2, 6 , 8 , 1, 19 , 5 , 3]
i = 0
j = len(arr) - 1
# maxValue , minValue  = maxAndmin(arr , i , j)
# print("Max and Min " , maxValue , minValue)


# 2. Best time To Sell And Stock #
# TC is O(n) , SC is O(1) #
def timeToSell(price):
    max_profit = 0
    min_price = float('inf')
    n = len(price)
    for i in range(n):
        if price[i] < min_price :
            min_price = price[i]
        elif price[i] - min_price > max_profit:
            max_profit = price[i] - min_price
    return max_profit
nums = [ 7 , 1, 4 , 7 , 15]
# result = timeToSell(nums)
# print("Max profit " , result )

# 3. Max Product SubArray #
# TC is O(n) , SC is O(1)  #
def maxProductSubArr(arr):
    suffix = 1
    prefix = 1
    product = 0 
    n = len(arr)
    for i in range(n):
        if suffix == 0 :
            suffix = 1
        elif prefix == 0 :
            prefix = 1  
        else:
            prefix = prefix * arr[i]
            suffix = suffix * arr[n -i - 1] 
            product = max(product , max(prefix , suffix))
    return product 
arr = [2 , 3 , 4, -1 , 0 , 7 , 2]   
# result = maxProductSubArr(arr)
# print("MaxSubArrProduct" , result)         


# 4. 3Sum #
# TC is O(n^2) , SC is O(k) #
def TripleSum(nums):
    i = 0 
    n = len(nums)
    result = []
    nums.sort()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 
        left = i + 1
        right = n - 1
        while  left < right :
            total = nums[i] + nums[left] + nums[right]
            if total == 0 :
                result.append([nums[i] , nums[left] ,  nums[right]]) 
                while left < right and nums[left] == nums[left + 1]:
                    left += 1 
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1 
                left += 1
                right -= 1          
            elif total < 0 :
                left += 1
            else:
                right -= 1
    return result                     

arr = [ 1 , 0 , -1 , 2, -3 , 5]
# result = TripleSum(arr)
# print("TripleSum" , result )


# 5. kth Smallest #
#APP1>>
# TC is O(nlogn) , SC is O(1) #
def kthSmallest1(arr , p , q , k ):
    if  p < q :
        m = partition(arr , p , q)
        if m == k :
            return arr[m - 1]
        elif m < k :
             return kthSmallest1(arr , m , q , k)
        else:
             return kthSmallest1(arr , p , m - 2, k) 
def partition(arr , p , q):
    i = p
    pivot = arr[p]
    for j in range(i + 1, q+1 ):
        if arr[j] < pivot :
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]  
    arr[i] , arr[p] = arr[p] , arr[i]
    return i + 1

arr = [ 6 , 8 , 1, 19 , 3]
p = 0
q = len(arr) - 1
k = 3
# result = kthSmallest1(arr , p , q, k)
# print("Kth Smallest Number is " , result )

#APP2>>
# TC is O(nlogk ) , SC is O(k) #
from heapq import heappop , heappush 
def kthSmallest2(nums , k ):
    heap = []
    for num in nums :
        if len(heap) < k :
            heappush(heap , -num)
        else:    
            if  num <  -heap[0] :
                heappop(heap) 
                heappush(heap , -num)
    return -heap[0]  
arr = [ 6 , 8 , 1, 19 , 3]
k = 2
# result = kthSmallest2(arr , k)
# print("KthSmallest2" , result )




# 6. Repeat And Missing Number Arr #
# TC is O(n) , SC is O(1) #
def repeatAndmissEle(nums):
    repeat = 0
    missing = 0 
    n = len(nums)
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0 :
            repeat = abs(num)
        else:
            nums[index] = -nums[index]    
    for i in range(n):
        if nums[i] > 0:
            missing = i+1
    return repeat, missing


nums = [ 7, 1, 5, 4, 6, 3 , 3]    
# result = repeatAndmissEle(nums)
# print("Repeat And Missing:", result)




# 7. Merge Intervals #
# TC is O(nlogn ) , SC is O(1) #
def mergeIntervals(intervals)  :
    result = []
    if not intervals :
        return []
    intervals.sort(key = lambda x : x[0])
    merged = [intervals[0]]    
    for i in range(1 , len(intervals)) :
        curr_interval = intervals[i]
        last_merged_interval = merged[-1]
        if curr_interval[0] <= last_merged_interval[1]:
            merged[-1] = [last_merged_interval[0] , max(curr_interval[1] , last_merged_interval[1])]
        else:
            merged.append(curr_interval) 
    return merged        
intervals = [[2, 3] , [3 , 8 ] , [1, 6] , [7, 10]]               
# result = mergeIntervals(intervals)
# print("Mergeintervals" , result)            



# 8. Merge Sorted Arr #
# TC is O(n) , SC is O(1)  #
def mergeSortedArr(arr1 , arr2 ):
     m = len(arr1) -1 
     n = len(arr2) - 1
     merge_indx = len(arr1) + len(arr2) - 1
     arr1.extend([0] * len(arr2))
     while m >= 0 and n >= 0 :
        if arr1[m] > arr2[n]:
            arr1[merge_indx] = arr1[m]
            m -= 1
        else:
            arr1[merge_indx] = arr2[n]
            n -= 1
        merge_indx -= 1
     while m >= 0 :
        arr1[merge_indx] = arr1[m]
        m -= 1
        merge_indx -= 1
     while n >= 0 :
        arr1[merge_indx]  = arr2[n]
        n -= 1
        merge_indx -= 1

     return arr1    

arr1 = [ 2  , 4 , 6, 8] 
arr2 = [ 1 , 3, 5, 7]
# result = mergeSortedArr(arr1 , arr2 ) 
# print("Merged Sorted Arr " , result )   



# 9. Majority  Elements #
# TC is O(n) , SC is O(1)  #
def findMajority(nums):
    cand = None
    count = 0
    for num in nums :   
        if count == 0 :
            cand = num
        count += (1 if num == cand else -1 )   
    return cand 

def isMajority(nums , cand):
    n = len(nums)
    cnt = 0 
    for i in range(n):
        if nums[i] == cand :
            cnt += 1
    if cnt > n//2 :
        return True
    else:
        return False               

def majorityEle(nums):
    cand = findMajority(nums)
    result = isMajority(nums , cand)
    if result :
        print("Is Majority " , cand)
    else:
        print("Not Majority ")    
# nums = [2 , 3 ,3, 3, 2, 5 , 3]
# result = majorityEle(nums)


# 10 . Find Duplis #
#APP1>>
# TC is O(n) , SC is O(n) #
def findDupli1(nums) :
    seen = set()
    dupli = []
    for num in nums :
        if num in seen :
            dupli.append(num)
        seen.add(num)  
    return dupli  
nums = [ 7, 1, 5, 4, 6, 3 , 3]  
# result = findDupli1(nums)   
# print("Duplicates1 are " , result )       


#APP2>>
# TC is O(n) , SC is O(1) #
def findDupli2(nums):
    xor_res = 0
    for num in nums :
        xor_res ^= num 
    for i in range(1 , len(nums)):
        xor_res^= i 
    return xor_res

# nums = [ 2, 1, 5, 4, 6, 3 , 3]  # won't work when elements >= n
# result = findDupli2(nums)   
# print("Duplicates2 are " , result ) 



# 11. Space Optimization #
# TC is O(b-a) , SC is O(k)  #
def spaceOptimize( a, b ):
    marked  = 0 
    for num in range(a , b + 1) :
        if num % 2 == 0 or num % 5 == 0 :
            marked |= (1 << (num - a))
    multiples = []        
    for i in range(b - a + 1):
        if (marked & (1 << i)) != 0:
            multiples.append(a + i)
    return multiples
a = 10
b = 20
result = spaceOptimize(a, b)
print("multiples of 2 and 5 b/w a to b" , result )            


# 12. MergeOperationTo make palindromeARR #
# TC is O(n) , SC is O(1) #
def makePalindrome(arr) :
    i = 0 
    j = len(arr) - 1
    cnt = 0 
    while i < j :
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            arr[i+1] = arr[i] + arr[ i+ 1] 
            cnt += 1
            i += 1
        else:
            arr[j-1] = arr[j] + arr[j-1]
            cnt += 1
            j -= 1
    return cnt 
arr = [ 1, 2, 3 , 8 , 4 ,  5 , 1]
result = makePalindrome(arr) 
print(" MergeoperationTo make palindrome ARR :" , result )             





