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






