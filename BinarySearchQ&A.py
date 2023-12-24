## 47. Search Element in 2D Matrix 
# Time Complexity is O(log m*n) , Space Complexity is O(1)
def searchElement(arr , target ):
  m = len(arr)
  n = len(arr[0])
  left = 0
  right = m*n -1 
  while left <= right :
    mid = left + (right - left) //2
    matrixElem = arr[mid//n][mid%n]
    if matrixElem == target:
        return True
    elif matrixElem < target:
        left = mid + 1     
    else:
        right = mid - 1  
  return False           
matrix = [[1, 2, 3,] ,[4, 5 ,6 ], [7 , 8, 9]]
target = 0
result = searchElement(matrix, target)
print("Elemnet searched in an Array " , result)




## 48. Search Inserted Position(index of target)
# Time Complexity is O(logn) , Space Complexity is O(1)
def indexSearchEle(arr , target):
  i = 0 
  j = len(arr) - 1

  while i <= j:
    mid = i + (j -i )//2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target :
      i = mid + 1
    else:
      j = mid - 1
  return -1 
arr = [1, 2, 3, 4, 5, 6 ,8]
target = 3 
result = indexSearchEle(arr , target)
print("Position of Searched Element is " , result)




## 49. Search In Rotated Sorted duplicates ele In Array 
# Either left hand side is sorted or right hand side sorted 
# Time Complexity is O(log n) , Space complexity is O(1)
def sortedSearchArr(arr , target ):
 # if have duplicate ele then Need To convert " arr = list(set(arr))"
   i = 0
   j = len(arr) - 1 
   mid  = i +( j - i)// 2
   while i <= j :
    if arr[mid] == target:
      return mid
  # sorted Array LHS
    if arr[i] <= arr[mid]: # check element from lower to mid one
      if arr[i] <= target and  target <= arr[mid] : # if target lies between lower to mid 
        j = mid - 1 # remove the right half 
      else:
        i = mid + 1

    else: # if target lies between mid to right 
      if  arr[mid] <= target and target <= arr[j] : #target lies between mid to higher 
        i = mid + 1
      else:
        j = mid  - 1  

   return -1 

nums = [ 7 , 8 , 9 , 1, 2, 3 , 3 , 4 , 5 , 6 , 6]  
target = 9
result = sortedSearchArr(nums , target)
print("Searched Element by k th rotated sorted unique Array  " , result)

