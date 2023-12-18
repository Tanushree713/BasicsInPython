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


## 49. 