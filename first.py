arr = [2, 5, 2, 4, 3, 6]

# Random Access
print(arr[2]) 
print(len(arr)) 
print(range(len(arr)))

# Search an element , if element of an array is present at index of array return index else return -1 
# Function definition
#  Time complexity is O(n)
#  Space Complexity is O(1)

def linearSearch(arr , x):
 for i in range(len(arr)):
   if arr[i] == x :
    return i 
 return -1 
 
print(arr)
x = 20
result = linearSearch( arr, x)
print("Search element is present at index" ,result)

# Insert element in an array
# arr.insert(index , element)
# Time Complexity  is O(n)
arr.insert(2,3)
print(arr)

# Remove an element from an array by providing an element
# arr.remove(element)
# Time Complexity is O(n)

arr.remove(4)
print(arr)

# Frequency of an element in an array 
# arr.count(element)

counter = arr.count(2)
print(counter)

# Delete an element from an array by providing index 
# arr.pop(index)
# Time Complexity is O(n)

arr.pop(3)
print(arr)

# Sort an array
arr.sort()
print(arr) 

# to extract index of an elemnet 

indexing = arr.index(5)
print(indexing)

# To extend the original array at the end of list 

arr.extend([ 8 , 9 , 10 , 11]) 
print(arr) 

# To Reverse the entire List 

arr.reverse()
print(arr) 
