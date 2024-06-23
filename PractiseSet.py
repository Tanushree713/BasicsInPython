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


#3.MaximumProductSubArr#
# Tc is O(n) , Sc is O(1) #
def maxProductSubArr(arr):
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
arr = [2 , 3 , -4, -1 , 0 , 7 , 2]      
# result = maxProductSubArr(arr)
# print("Max Product SubArr " , result )


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
result = tripletSum(arr)
print("Triplet Sum " , result )


#5.KthSmallestEle#

# Using QuickSelection Sort #
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
result = kthSmallest1(arr , p , q, k)
print("Kth Smallest Element1" , result)   

# Using HeapSort #
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
result = kthSmallest2(arr , k)
print("Kth Smallest Element2" , result )

# Using BSTConcept #
# Tc is O(nlogn) , Sc is O(k)#




        









 






