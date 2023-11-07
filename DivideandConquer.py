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

## 4th Application >>





