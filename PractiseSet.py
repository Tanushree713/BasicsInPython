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
    n = len(arr) - 1
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
# result = reverseWordsInStr(string)
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
s2, t2 = "foo", "baa"
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
##*
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
# Tc is O(n) , Sc is O(n)
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
# Tc is O(n) , Sc is O(n) #
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

#


