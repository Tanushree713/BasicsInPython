### Ternary Search in an array ###
## Divide into 3 parts ##
## Time Complexity is O(log3n) ##
# Sorted Array

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 19
i= 0 
j= len(arr) - 1

def ternarySearchInSortedArray(arr , i , j ,target ):
    while i<=j :
        mid1 = i+ (j-i)//3
        mid2 = j-(j-i)//3
        if arr[mid1] == target: 
         return mid1
        elif arr[mid2] == target:
            return mid2
  # First Search Space           
        elif arr[mid1] > target:
            j = mid1-1
  # Third Seacrh Space 
        elif arr[mid2] < target :
            i = mid2 +1 
  # Second search Space 
        else:
            i = mid1 + 1 
            j = mid2 - 1
    else :
        return -1

result = ternarySearchInSortedArray(arr , i , j , target)    
print(result)                               
                   
    
