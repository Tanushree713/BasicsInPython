## 1st Application >> Find Min and Max in an array ##
# Time Complexity is O(n) , Space Complexity is O(1)
def findMaxandMin(arr , i , j):
    # Small Problem #
    # having single element pushing that element in both value
    if i == j :
        max_value = arr[i]
        min_value = arr[i]
    # having 2 elements do one comparison     
    elif i == j -1 : 
        if arr[i] < arr[j]:
          max_value = arr[j]
          min_value = arr[i]
        else:
            max_value = arr[i]
            min_value = arr[j]
    # Big problem #        
    # Divide
    else: 
        mid = i + (j-i)//2
    # recursion -> conquer 
        max_l , min_l  = findMaxandMin(arr , i , mid)
        max_r , min_r  = findMaxandMin(arr , mid+1 , j)   

    # combine
        max_value  = max(max_l , max_r)
        min_value  = min(min_l , min_r)

    return max_value , min_value

arr = [ -2 , 100 , 76 , 436 , 89 , -33 , 0  ]
i = 0
j = len(arr) - 1
max_value , min_value = findMaxandMin(arr , i , j)
print("Max and Min" , max_value  , min_value)


## 2nd Application >> Find Power of an element 
# Time Complexity is O(logn) , Space Complexity is O(1)

def findPowerOfElement(a , n) :
    # small problem 
    if n == 0 :
        return 1
    elif n == 1 :
        return a 
    elif n < 0 :
        a = 1/a # 1/2 like that 
        n = -n # making positive power
        return findPowerOfElement(a , n) # fun calling with new base 1/a and power -n
    # Big Problem    
    else:
        # Divide
        mid = n//2
        # conquer (recursive call) 
        b = findPowerOfElement(a , mid)
        result = b * b # 2^2 = 2*2 = 4 (on both side in tree getting same value 4 , no need to do same calculation again , so just multiply with itself again )-> 4*4 = 16 -> 16*16 -> 256
        if n % 2 == 0: # even Case
            return result 
        else:
            # odd Case
            return result * a   

a = 3
n = 3
results  = findPowerOfElement(a , n)
print("Find power of element is :" , results)



## 3rd Application >> BinarySearch 
# Time Complexity is O(logn) , Space Complexity is O(1)

def binarysearch(arr , k ) :
    i = 0 
    j = len(arr) - 1 
    # small problem 
    if len(arr) == 1:
        return arr
    # big Problem 
    while i <= j :
        mid = i + (j-i) //2

        if arr[mid] == k:
            return mid 

        elif arr[mid] < k:
            i = mid +1 

        else:
            j = mid - 1

    return -1 

array = [20 , 23 , 24 , 25 , 9 ]
k = 9
searchElement = binarysearch(array , k )
print("Search Element is :", searchElement )

## 4th Application >> Merge Sort ##
# Time Complexity is O(nlogn) , Space Complexity is O(n) #


# definition of mergeProcedure function
def mergeProcedure( arr , i , mid , j):
    # n1 -> no. of elements in leftSubarray (i , mid)
    n1 = mid - i + 1
    # n2 -> no. of elements in rightSubarray (mid + 1 , j)
    n2 = j - mid 
    # Initialize left and right Subarray
    leftSubarray = [0] * n1
    rightSubarray = [0] * n2
    # copy elements from (original )array to (as) subarray 
    for m in range(n1):
        leftSubarray[m] = arr[i + m]
    for n in range(n2):
        rightSubarray[n] = arr[mid + 1 + n]
    p = 0
    q = 0 
    k = i
    ## returning sorted subarray
    while p < n1 and q < n2 :
        if leftSubarray[p] <= rightSubarray[q]:
            arr[k] = leftSubarray[p]
            p += 1


        else:
             arr[k] = rightSubarray[q]
             q += 1

        k += 1

     ## copy entire elements from leftsubarray
    while  p < n1:
        arr[k] = leftSubarray[p]
        p += 1
        k += 1

     ## copy entire elements from rightsubarray
    while q < n2 :
        q += 1
        k += 1


# definition of mergeSort function
def mergeSort(arr , i , j):
    # small Problem 
    if i == j :
     return arr
    # Big Problem  (i < j)
    else: 
      # Divide
      mid = i + (j-i )// 2  
      # conquer -> recursive call
      mergeSort(arr , i , mid)
      mergeSort(arr , mid+1 , j)
      # combine 
      mergeProcedure( arr , i , mid , j)
    return arr


sortarray = [50 , 70, 65, 13 , 80 , 62 , 98 , 17]
i = 0 
j = len(sortarray) - 1
result = mergeSort(sortarray , i , j)
print("Sorted Array is :" , result)



## 5th Application >> QuickSort >> Best Method For Highly Unsorted Array 
# Time {Average} complexity is O(nlogN ) , Space Complexity O(1)
def partition(arr , p , q):
    i = p 
    pivot = arr[p]
    for j in range(i+1 , q+1 ):
        if arr[j]<= pivot :
            i = i+1 
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i] , arr[p] = arr[p ],arr[i]
    return i         


def quickSort( arr , p , q) :
    if p < q :
        mid = partition(arr , p , q)
        quickSort(arr , p , mid -1 )
        quickSort(arr , mid+1 , q)
    return arr   

unSortedArr = [ 70 , 50 , 47 , 99 , 147 , 34 , 85 , 21]
p = 0 
q = len(unSortedArr) -1
gettingSortedArray = quickSort(unSortedArr , p , q)
print("Sorted Array is by appying quicksort:" , gettingSortedArray)


## RANDOM QuickSort Algo ##
# Time Complexity is O(nlogN) and space Complexity is O(1) #

import random
# definition for random_Partition 
def randomPartition(unArr , p , q):
    # taking random values
    random_pivot = random.randrange(p , q) 
    # swap random_value and element at zeroth index
    unArr[p] , unArr[random_pivot] = unArr[random_pivot] , unArr[p] 
    return partition(unArr , p , q)


# definition for Partition 
def partition( unArr , p , q):
     i = p 
     pivot = unArr[p]
     for j in range(i+1 , q+1):
        if unArr[j] <= pivot:
            i += 1
            unArr[i] , unArr[j] = unArr[j] , unArr[i]
     unArr[i] , unArr[p] = unArr[p], unArr[i]
     return i        


# definition of Random  QuickSort 
def randomQuickSort(unArr , p , q):
    # big Problem 
    if p < q :
        mid = randomPartition(unArr , p , q)
        randomQuickSort(unArr , p , mid-1 ) # mid-1 >> rest one Element taking as pivot element , which comes in correct place after 1st step #
        randomQuickSort(unArr , mid+1 , q)
    return unArr


unArr = [70 , 50 , 47 , 99 , 147 , 34 , 85 , 21]
p = 0 
q = len(unArr) - 1
result = randomQuickSort(unArr , p , q)
print("Soterd Array using random quickSort" , result)




## 6th Application >> QuickSelection Procedure 
####  Kth Smallest Element in an Array 
## Time complexity : 1. Best Case(equal element division)>>O(n)
##                   2. Worst Case(either left element is more than Right or right one than left)>> O(n^2)
## Space Complexity is O(1)

def selectionProcedure(arr , p ,q , k):
    # Small problem (having single element )
    if len(arr) == 1 :
        return arr[p]
    # Big Problem 
    else :
        m = partition(arr , p , q) # partition returns Position(m = i+1) of Pivot in sorted Array 
        if m == k :
            return arr[m-1] # m-1 bcoz, m-1 = index of pivotElement in sorted Array 
        elif m < k : # need to move Right Side (range (m , q))
            return selectionProcedure(arr , m , q , k) # m bcoz,m-1 = pivot index and we need to move right side 
        else: # need to move left side 
            return selectionProcedure(arr , p , m-2 , k) # m-2 bcoz, m-1 =pivotElement index and need to move just left 

def partition(arr , p ,q):
    i = p 
    pivot = arr[p]
    for j in range (i+1 , q+1): # q+1 bcoz, on taking q only last one element is missed 
        if arr[j] <= pivot :
            i += 1
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i] , arr[p] = arr[p]  , arr[i]
    return i+1 # return position instead of index                       


unArray = [ 30 , 70 , 50 , 98 , 24 , 12 , 43 , 48]
p = 0 
q = len(unArray) - 1
k = 4
result = selectionProcedure(unArray , p , q , k)
print("Kth Smallest Elemnt in an Array is " , result)



## Count The Number Of Inversions , using Divide and Conquer Approach ##
# Time complexity is O(nlogn) , Space complexity is O(n)

# definition of inversionCount getting count 
def inversionCount(arr, p, q):
    _, inv_count = mergesort(arr, p, q)
    return inv_count

def mergesort(arr, p, q):
    # Divide
    if p < q:
        mid = p + (q - p) // 2
        # Conquer >> recursive calls
        left, inv_left = mergesort(arr, p, mid)
        right, inv_right = mergesort(arr, mid + 1, q)
        # Combine
        merged, inv_merge = merge(left, right)
        return merged, inv_left + inv_right + inv_merge
    # Small problem
    else:
        return [arr[p]], 0

def merge(left, right):
    result = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # left subArr is sorted
            result.append(left[i])
            i += 1
        else:  # right subarray element is lesser than left, so need to invert
            result.append(right[j])
            inv_count += len(left) - i  # len(left)-i: remaining elements of left Arr that are greater than the element present in right arr
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count

unsortArr = [30, 18, 5, 36, 9, 25, 72 , 2]
p = 0
q = len(unsortArr) - 1
count = inversionCount(unsortArr, p, q)
print("The inversion count of an Array is ", count)


 














