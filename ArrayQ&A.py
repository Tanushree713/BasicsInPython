## 1. Min And Max Element  in given Array ##
# Time Complexity is O(nlogn) 
# Space complexity is O(1)
arr = [11, 23, 12, 13 , 36 , 40 , 9]
def minAndMax(arr):
 arr.sort()
 print(arr)
 minAndmax = { "min": arr[0] , "max": arr[len(arr)-1 ]}
 return minAndmax

resultant = minAndMax(arr)
print("min element is :" , resultant["min"] )
print("max element is :" , resultant["max"] )

## OPTIMIZED Approach :- DIVIDE And CONQUER
# Time Complexity is O(n)
# space Complexity is O(1)

def findMinandMax(arr  , i , j):
    # small problem 
    if i == j: # single element is present in array
        max_value = arr[i]
        min_value = arr[i]
    elif i == j-1 : # i= 0 j=1 having 2 elements
        # Do one comparison 
        if arr[i]< arr[j]:
            max_value = arr[j]
            min_value = arr[i]  
        else:
            max_value = arr[i]
            min_value = arr[j]
    #Big problem
    else:
        # Divide
        mid = i + (j-i)//2
        # Recursion --> Conquer
        max_l , min_l  = findMinandMax(arr , i , mid)
        max_r , min_r = findMinandMax(arr , mid+1 , j)
        # combine
        # final max_value
        if max_l < max_r :
            max_value = max_r
        else:
            max_value = max_l
        # final min_value    
        if min_l < min_r :
            min_value = min_l
        else:
            min_value = min_r    
            
    return max_value , min_value


arr = [70 , 56  ,45 , 62 , 31, 29 , 15 , 10 , 3 , 13 , 97] 
i = 0 
j = len(arr) - 1
max_value , min_value = findMinandMax(arr , i , j)
print("Max and Min element is:" , max_value , min_value)                     





## 2. Best Time to Buy and sell the Stock ##
# Time Complexity is O(n)
# Space Complexity is O(1) 
prices = [ 7, 1, 5, 4, 6, 3]
def buysellStock(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit :
            max_profit = prices[i] - min_price    
    return max_profit

result = buysellStock(prices)
print("Max Profit is :" , result )  



## 3. Max Product of SubArray ##
# Time complexity is O(n^2)
# Space Complexity is O(n^2)
## Approach 1 ##
def find_subArray(arr):
    subArrays = []
    n = len(arr)
    for i in range(n):
        subArray = []
        for j in range(i , n):
            subArray.append(arr[j])
            subArrays.append(subArray.copy())
    return subArrays
def productOfSubArray(subarrays):
    products = []
    for subarray in subarrays:
        product = 1
        for element in subarray:
            product *= element
        products.append(product)
    return products

arr = [ 1, 2, 3]
subarrays = find_subArray(arr)
products =  productOfSubArray(subarrays)
subArraysAndProducts = list(zip(subarrays , products))
maxSubArrayProductIs = max(subArraysAndProducts , key = lambda x: x[1])
max_product = maxSubArrayProductIs[1]
print("max product is:" , maxSubArrayProductIs)
print("product of subarray " , max_product)

## Approach2 (OPTIMIZE)##

## 4. 3Sums
# Getting triplets sum is equal to zero return that subarray #
#  Two pointer Approach
# Time Complexity is O(n^2)
# Space Complexity is O(k) where k depneds on number of subarray 

def tripletSum(nums):
    nums.sort() # use sorting so proceed with 2 pointer approach 
    results = []

   #To confirm that we have three element atleast in an array
    for i in range(len(nums)-2):
        # find duplicates
        if i > 0 and nums[i] == nums[i-1]: 
            # skip duplicates 
            continue
        # start implementation of 2 pointer approach
        left , right = i + 1 , len(nums) - 1
        while left < right :
            total  = nums[i] + nums[left] + nums[right]
            if total == 0 :
                results.append([nums[i] , nums[left] , nums[right]])
                # removing duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1
    return results 

nums = [ 1 , 2, -1 , 0 , -2 , 4 , -3]                    
resultants = tripletSum(nums)
print ("triplet whose sum is zero is " , resultants)



## 5. Kth Smallest Element 
# Approach 1 --> sort array then kindex = k-1  -> print array[kindex]
# Approach 1 : Time complexity is O(nlogn) , Space Complexity is O(1)
# Approach 2 --> Divide and conquer with QuickSelectionSort 
# Approach 2 : Time complexity is O(n) , Space Complexity is O(1)

#definition for selectionPartition
def selectionPartition( arr , p, q , k):
    i = p 
    pivot = arr[p]
    for j in range(i+1 , q+1) :
        if arr[j] <= pivot :
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[p] =arr[p] , arr[i] 
    return i+1  # returning position not index       


# definition for quickSorting
def quickSort(arr , p , q , k):
    #Divide
    m = selectionPartition( arr , p , q , k) # m = provide position
    #check 
    if m == k :
        return arr[m-1] # m-1 bcoz , m-1 =index of that element
    elif m < k :
        return quickSort(arr , m , q , k) # m is just right element of getting element 
    else:
        return quickSort(arr , p , m-2 , k) # just left element (m-1 = element)


givenArr = [ 7, 1, 5, 4, 6, 3]
p = 0
q = len(givenArr)- 1
k = 5
result = quickSort(givenArr , p  , q , k)
print("Kth smallest element is :" , result )



## 6th Kth Largest Element ##
# Time complexity is O(n)  , Space Complexity is O(1) 
def selectionPartition( arr , p, q , k):
    i = p 
    pivot = arr[p]
    for j in range(i+1 , q+1) :
        if arr[j] >= pivot :
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[p] =arr[p] , arr[i] 
    return i+1  # returning position not index       


# definition for quickSorting
def quickSort(arr , p , q , k):
   
    #Divide
    m = selectionPartition( arr , p , q , k) # m = provide position
    #check 
    if m == k :
        return arr[m-1] # m-1 bcoz , m-1 =index of that element
    elif m < k :
        return quickSort(arr , m , q , k) # m is just right element of getting element 
    else:
        return quickSort(arr , p , m-2 , k) # just left element (m-1 = element)


givenArr = [ 7, 1, 5, 4, 6, 3] #[3, 1, 5, 4, 6, 7] if have this array then , tjis is worst case(descending order) .So , Time complexity is O(n^2).
p = 0
q = len(givenArr)- 1
k = 5
result = quickSort(givenArr , p  , q , k)
print("Kth Largest  element is :" , result )





















