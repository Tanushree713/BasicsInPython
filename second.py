## Implementation Of Binary Search
## Sorted Array
## Time Complexity is O(logn)
arr = [ 2, 3, 4, 5, 6, 7, 8, 11, 40]
## Targeted Value
x = 10
i = 0 
j = len(arr) - 1 
## function calling (Recursion)

# def binarySearch(arr , i , j , x):
#   while i<=j :
#       mid = (i+(j-i))//2
#       if arr[mid] == x:
#        return mid 

#       elif arr[mid] < x:
#        return binarySearch(arr , mid+1 , j , x) 

#       else:
#        return binarySearch(arr , i , mid-1 , x) 
       
#   return -1  


## Time Limit Exceeded due to excessive function calls

### Alternative Approach :-
def binarySearch(arr , i , j , x):
    while i<=j :
     mid = i+(j-i)//2 
     if arr[mid] == x:
      return mid
     elif arr[mid] < x:
       i = mid +1 
     else:
       j = mid -1
    return -1 
result =  binarySearch(arr , i , j, x)
print ("Searching element is present at index " , result ) 

##### Given Unsorted Array Apply BinarySearch on it Thinking Logically ####
array = [1, 49, 23, -21, 64, 2, 0, 13, 47,float("inf"), float("inf"), float("inf")]
i = 0 
j = len(array) - 1 

def firstInfiniteIndex(array , i , j):
  while i<=j:
    mid = i+(j-i)//2
    if array[mid] != float("inf"):
      i = mid +1 
    else:
      if mid == 0 or array[mid-1] != float("inf") :
        return mid 
      else:
        j = mid -1 
  return -1 

resultant = firstInfiniteIndex(array , i , j)
print("firstInfiniteIndex" ,resultant)     
       


    

  

