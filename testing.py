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
result = kthSmallest2(arr , k)
print("KthSmallest2" , result )




