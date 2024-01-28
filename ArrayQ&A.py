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
# Time Complexity is O(n) , Space Complexity is O(1) #
def findMaxSubarrayProduct(self ,arr):
    n = len(arr)
    res = float('-inf')  # Contain Max Value
    prefix = 1
    suffix = 1
    for i in range(n):
        if prefix == 0 :
            prefix = 1
        if suffix == 0 :
            suffix = 1
        prefix *= arr[i]
        suffix *= arr[n-i-1]
        res = max(res , max(prefix, suffix))          

    return res    




## 4. 3Sums  #
# Getting triplets sum is equal to zero return that subarray #
# Approach1>> Brute Force Approach #
# Time Complexity is o(n^3) , Space Complexity is O(1)
#  traverse Loop i from 0 to n-1
# traverse Loop j from i + 1 to n-1
# traverse Loop k from j + 1 to n-1 
# check , if arr[i] + arr[j] + arr[k] == 0 
# result = [ arr[i] , arr[j] , arr[k] ]
# return set(sort(result))


# Approach2>>  Two pointer Approach
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



## 6. Kth Largest Element ##
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



## 7. Repeat And Missing Elements 
# Time complexity is O(n) , Space complexity is O(1)
#definition for repeatAndMissing
#LOGIC# -ve to each elements atleast once if found more than once becomes +ve , that +ve having repeated elements and also having that ,
#  i + 1 = missing element

def repeatAndMissing(nums):
    repeat  = 0 
    missing = 0
    n = len(nums)
    for num in nums:
        index = abs(num) - 1  # Storing index from 1 instead of 0
        if nums[index] < 0 :  # Check each element is visited ( becomes -ve)
          repeat = abs(num)   # if a number is encountered whose corresponding index has already been marked as negative, it means that this number is a repetition, and its absolute value is assigned to the repeat variable
        else:
            nums[index] = -nums[index] # -ve to each elements 
    for i in range(n) :
        if nums[i] > 0 :
            missing = i+1
    return repeat , missing



array = [ 7, 1, 5, 4, 6, 3 , 3] 
results = repeatAndMissing(array)

print("Repeated And Missing Element" , results)



## 8. Merge Intervals 
# Approach 1 >> create Stack -> store updated( index[0] of 1st interval ,[whatever max of index[1] of 1st interval and index[1] of 2nd interval] if end >= start)intervals get stored inside created stack 
# else append the intervals as it is
# Time Complexity is O(nlogn) , Space Complexity is O(n)
# Approach 2 
# No need to create stack , take merged which created list by comparing and updating 
#Time Complexity is O(nlogn) , Space Complexity is O(1)

# definition for mergeIntervals
def mergeInterval(intervals):
    if not intervals: #small problem 
        return []
    merged = [intervals[0]]  #intialise containing 1st interval of intervals array
    intervals.sort(key = lambda x:x[0])  # sort according to [0] index of interval of intervals
    #Big Problem 
    for i in range( 1, len(intervals)):
        current_interval = intervals[i] # current_interval = (interval with 1 index )
        last_merge_interval = merged[-1] # last_merge_interval = (interval with 0 index)

        #check overlap 
        #{current_interval[0] = start intv of interval of intervals }{#last_merge_interval[1] = end intv of interval of intervals }
        if current_interval[0] <= last_merge_interval[1] : #check and update 
            merged[-1] = [last_merge_interval[0] , max(current_interval[1] , last_merge_interval[1])]
        else:  # No overlap, add the current interval to the merged list
            merged.append(current_interval)

    return merged        

intervals = [[2, 3] , [3 , 8 ] , [1, 6] , [7, 10]]
results = mergeInterval(intervals)
print("The Merge Intervals Are :", results)


## 9. Merge Sorted Array ##
# Approach 1>> Create new array then , Compare both 1 nd 2 array , find greater one then  ,Append in last index of new array 
# Time Complexity is O(n) , Space Complexity is O(n) 
# Approach 2 >> Create preAllocate List having one element then push elements in that preallocate list according to Comparisons.
# Time complexity is O(nlogn) , Space complexity is O(1)

def merge_Sorted_Array(arr1, arr2):
    m , n = len(arr1) - 1, len(arr2) - 1  #getting last index of both arr1 and arr2  
    merged_index = len(arr1) + len(arr2) - 1 #for index of new extending arr1

    # Resize arr1 to accommodate the merged elements
    arr1.extend([0] * len(arr2))

    while m >= 0 and n >= 0:
        if arr1[m] > arr2[n]:  # comparing from last index of both arr1 and arr2  
            arr1[merged_index] = arr1[m]   # put obtain largest element after comparison into last index of extend arr1
            m -= 1
        else:
            arr1[merged_index] = arr2[n]
            n -= 1
        merged_index -= 1
    # Remaining elements in arr1 copy that as it is
    while m >= 0:
        arr1[merged_index] = arr1[m]
        m -= 1
        merged_index -= 1
    # Remaining elements in arr1 copy that as it is
    while n >= 0:
        arr1[merged_index] = arr2[n]
        n -= 1
        merged_index -= 1    

    return arr1

# Example
arr1 = [1, 2, 3  , 4]
arr2 = [2, 5, 7]
result = merge_Sorted_Array(arr1, arr2)
print("Sorted Array is by merging:", result)





## 10. Majority Elements (frequency > n/2) ##
# Time Complexity is O(n) , Space Complexity is O(1)
def findMajority(array):
    count = 0
    cand = None
    for arr in array :
         if count == 0 :
            cand = arr
         count += ( 1 if arr == cand else -1)
    return cand
def isMajority(array , cand):
    n = len(array)
    cnt = 0
    for i in range(n) :
     if array[i] == cand :
        cnt += 1
    if cnt > n/2 :
        return 1
    else :
        return 0        

def printMajority(array) :

    cand = findMajority(array)
    if isMajority(array , cand):
      print("majority Elements is " , cand)
    else :
      print("Not exist Candidates ")


array = [ 2, 2, 2, 2 ,3, 3 , 2, 1]      
result = printMajority(array)



## 11. Find All Duplicates Number i Array ##((IF "FIND DUPLICATE then , use LINKEDLIST CYCLE{TORTOISE , HARE Method}"))
# Approach 1>> sort array , traverse 2 loops from i and i+1 , check arr[i] == arr[i+1] if yes return arr[i]
# Time Complexity is O(nlogn)  , Space Complexity is O(1)
# Approach 2>> Repeat Approach
# # Time Complexity is O(n) , Space Complexity is O(1)
def find_duplicates(nums):
    duplicates = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:  # give visited element
            duplicates.append(index + 1) #add that element indx in duplicate list
        else:
            nums[index] = -nums[index]

    return duplicates

# Example
arr = [1, 2, 3, 4, 2, 5, 6 , -4 ]
arr = [abs(num) for num in arr]
result = find_duplicates(arr)
print("Duplicates in the array:", result)


## 12. Space Optimization using Bit manipulation ##
# Find all the elements between a and b which are divisible by 2 and 5  
# Time Complexity is O(b-a) and Space Complexity is O(k)
# Initial values
a = 10
b = 20
marked = 0

# Mark multiples of 2 or 5
for num in range(a , b+1):
    if num % 2 == 0 or num % 5 == 0:
        marked |= (1 << num - a)

# In this loop, the following bits will be set in 'marked':
# 0b00000001110 (indices 2, 4, 5, 6, 8 in binary)

multiples = []

# Retrieve marked multiples
for i in range(b+1):
    if (marked & (1 << i)) != 0:
        multiples.append(a+i)

# 'multiples' will contain the numbers corresponding to the set bits in 'marked'
# [2, 4, 5, 6, 8]

# Final result
print("Elements that are multiples of 2 or 5:", multiples)


## 13.Find Min. number of merge operation make an array Palindrome ##
# Two Pointer Approach 
# Time complexity is O(n) , Space Complexity is O(1)
def CountOperation(arr):
    count = 0 
    i = 0
    j = len(arr) - 1
    while i < j:
       if arr[i] == arr[j]:
         i += 1
         j -= 1
       elif arr[i] < arr[j]:  #{ i = 2 , j = 4 , where i < j }
        arr[i+1] = arr[i+1] + arr[i] # {indx2 = 6}
        i += 1
        count += 1
       else :
        arr[j-1] = arr[j-1] + arr[j]
        j -= 1
        count += 1

    return count       

nums = [1, 2 , 3 , 4 , 1] 
result = CountOperation(nums)
print("Minimum number of operations to make an Array palindrome is " , result )


## 14. Find Power(x , n)
# Divide and Conquer Approach 
# Time Complexity is O(logn) , Space Complexity is O(1)

def findPower(x , n):
    # Small Problems 
    if n == 0 :
      return 1 
    elif n < 1:
        n = -n 
        x = 1/x    # '/' for Integer division and '//' for float-point division 
        return findPower( x , n)
    elif n == 1 :
       return x
    # Big Problems 
    else:
        # Divide    
        mid = n//2
        # conquer >> recursive calls
        y = findPower(x , mid)
        ans = y * y
        if n % 2 == 0 :
            return ans

    return ans * x

x = 2 #base
n = 7   #power
result = findPower(x , n)
print("Find Power Value of given Element " , result)    

## 15.Next Permutation 
#Approach1 >> Take All combinations and then , find out just after given combo 
# Time Complexity is O(n!) , Space Complexity is O(n!)
#Approach2 >> 2Pointer Type 
# Time Complexity is O(n) , Space Complexity is O(1)
def next_permutation(permute):
   i = len(permute) - 2 #second last element
   while i >= 0 and permute[i] >= permute[i+1]:   #second Last ele is greater than last one 
    i -= 1 # move towards LHS
   if i == -1 :
     permute.reverse() # reverse Whole descending array
   else:     # if yes then  
    j = len(permute)- 1 # last ele 
    while permute[j] <= permute[i]:  # check is any last ele present just greater after pointer elem
        j -= 1
    permute[i] ,permute[j] = permute[j] , permute[i] #Swap that ele with pointer ele
    permute[i + 1:] = reversed(permute[i+1:]) # reverse rest subarray present just after pointer ( i )

   return permute 

permutations= [ 1 , 2 ,3]
permute = [2, 3 , 1 ]
result = next_permutation(permute)
print("Next Permutation is" , result )



## 16.Find Sum Pairs In sorted Rotated Array is Present or not
# Time Complexity is O(logn) , Space Complexity is O(1)

def pairInSortedArray(arr , x ):
    # finding pivot element 
    n = len(arr) 
    for i in range(n):
       if arr[i] > arr[i+1] :
        break 
    l = (i + 1 )% n  # minimum element 
    r = i            # maximum element

    while l != r :
       if arr[l] + arr[r] == x :
        return True
       elif arr[l] + arr[r] < x :
          l =  (l + 1) % n
       else:
          r = (n+ r-1 )% n   
    return False

nums = [11, 15, 26, 38, 9, 10]
x = 22
result  = pairInSortedArray(nums , x)
if result :
    print("Yes !Sum Pairs is Present " )
else:
    print("No! not found sum pairs")    


## 17. Sort Colors 
# Time Complexity is O(n) , Space Complexity is O(1)

def sortArr(arr):
    p0 = curr = 0
    p2 = len(arr) - 1
    while curr < p2:
       if arr[curr] == 0 :
        arr[p0] , arr[curr] = arr[curr] , arr[p0]
        p0 += 1
        curr +=1
       elif arr[curr] == 2 :
        arr[p2] , arr[curr] = arr[curr] , arr[p2]
        p2 -= 1
       else:
        curr = curr +1  
    return arr       
 
array =  [2,0,2,1,1,0]
result = sortArr(array)
print("Sorted Array is " , result)

## 18. Rotate Array After Kth Steps
#Time Complexity is O(n) , Space Complexity is O(1)
# 
def rotatedArray(arr , start , end):
      while start < end:
        arr[start], arr[end] = arr[end], arr[start] #swaps 
        start += 1
        end -= 1
      return arr
def printRotatedArray(arr ,  k ):
    n = len(arr)
    k = k % n 
    rotatedArray(arr, 0, n - 1)  #reverse whole Array 
    rotatedArray(arr , 0 , k - 1) #reverse left subarray
    rotatedArray(arr , k , n-1)   #reverse right subarray 
   
    return arr

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = printRotatedArray(nums , k)
print("Rotated subarray after Kth Steps " , result)


## 19. Count Consecutive One's 
# Time Complexity is O(n), Space complexity is O(1)
def findOnesCount(nums):
   currCount = 0
   maxCount = 0
   for i in range(len(nums)): # traversing loop
    if nums[i] == 1:    #find ones in array 
        currCount += 1  #counts
        maxCount = max(maxCount , currCount) #getting max Count
    else:
        currCount = 0     # set count = 0 
   return maxCount

nums = [1, 1, 1, 1, 4, 1, 5, 1]    
result = findOnesCount(nums)
print("MAx Number of consecutive One's " , result)










####------------------------------------------------2D MATRIX ARRAY --------------------------------------------------------####

## 20. Spiral Matrix 
# Time Complexity is O(n*m) , Space Complexity is O(n*m)
def spiralMatrix(arr):
    result = []
    if not arr:
     return result 
    m = len(arr)  #rows
    n = len(arr[0]) #columns
    top = 0
    left = 0
    right = n - 1  # columns 
    bottom = m- 1 # rows
     # traverse till the elements remaining inside an array 
  
    while top <= bottom and left <=right :  
        # traverse from left to right where top is Constant
        for i in range(left , right + 1):
            result.append(arr[top][i])
        top += 1
        # traverse from top to bottom where right is Constant
        for i in range(top , bottom + 1): 
            result.append(arr[i][right])
        right -= 1
        # traverse from right to left where bottom is Constant
        # Make Sure that this run only, when element remains for moving left to right .Suppose having only one row remains then no need to traverse 
        if top <= bottom : 
         for i in range(right , left - 1 , -1):
            result.append(arr[bottom][i])
         bottom -= 1
        # traverse from bottom to top where left is Constant
        if left <= right :
         for i in range(bottom , top - 1 , -1): # (last -1 )indicates that the loop should decrement the index by 1 with each iteration.
            result.append(arr[i][left])
         left += 1

    return result                    

nums =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultant = spiralMatrix(nums)
print("Spiral Matrix is :" , resultant )




## 21. Matrix Diagonal Sum 
# Time Complexity is O(n) , Space Complexity is O(1)
def diagonalSumMatrix(mat):
    res = 0
    n = len(mat)  #last ele of matrix
    for i in range(n):
        res +=  mat[i][i] #(0,0)(1, 1)(2,2)
        res += mat[i][n-1-i] #(0,2)(1,1)(2,0)
    # if n(row and colmn) is odd there substract by repeated elem that is added in res(during diagonal from both direction)
    # if n(rows and colmn) is even there is no repeated elem added in res(sum of diagonal elem).So, return only res  
    return res - mat[n//2][n//2] if n % 2  else res  #1. odd   #2. even

matrix_even = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11]
]
result = diagonalSumMatrix(matrix_even )
print("Diagonal Sum Matrix is " , result)




## 22. Count the negative Numbers in sorted 2-D Array ##
## Time Complexity is O(m + n) , Space Complexity is O(1)
# Approach >>
#> 1. use Binary Search to search first negative element index
#> 2. substract and store in findNeg that index from the length of column 
#> 3. count = count + findNeg

def binarySearch(arr):
    def countNegNumber(row):
        n = len(row) #rows
        left = 0
        right = n - 1
        count = 0

        while left <= right :
            mid = left + ( right -left)// 2 
            mid_ele = row[mid]
            if mid_ele < 0 :
                count = (right - mid) + 1
                right = mid - 1
            else :
                left = mid + 1

        return count 

    total_count = 0 
    for row in arr :
        total_count = total_count + countNegNumber(row)

    return total_count    

mat = [
   [1, 2, 3, -4],
    [5, 6, 7, -8],
    [9, 10, 11, -12],
]

result = binarySearch(mat)
print("Matrix " , result )

# Alternative Approach >> 
# Time Complexity is O(n) , Space Complexity is O(1)
def countNegNum(arr):
    row_len = len(arr[0])
    col_len = len(arr)
    count = 0 
    i = 0
    j = row_len - 1

    while i < col_len and j >= 0 :
        if arr[i][j]  < 0:
            count += col_len - i 
            j -= 1

        else:
            i += 1
    return count            
mat = [
   [1, 2, 3, -4],
    [5, 6, -7, -8],
    [9, 10, -11, -12],
]

result = countNegNum(mat)
print("Matrix1 " , result )




      
## 23. Richest Customer wealth ##
# Time complexity is O(m*n) , Space Complexity is O(1) 
# Here taking list so , use sum function 
def richestwealth(accounts):
    total = 0
    maxSum = 0
    for wealth in accounts :
        total = sum(wealth)
        maxSum = max(maxSum , total)

    return maxSum
arr = [
    [1,2,3],[3,2,1]
]    
result = richestwealth(arr)
print("Richest Man " , result)












