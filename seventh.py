## Insertion Sorting ##
# Time Complexity is O(n^2) ##
## As a Deck Of Cards ##

arr = [ 9 , 5, 1, 4 ,3]
def insertionSort(arr):
    n = len(arr) 
    for i in range(1 , n):
        # define key is arr[1] and j is representing 0 index
        key = arr[i]
        j = i-1
        # this loop checks arr[1] = key is lesser than arr[0] then insert it at arr[1] 
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            # update j value if get -1 then come out from while loop 
            j = j -1 
        # swaps the element after completing loop
        arr[j+1] = key 
    return arr

result = insertionSort(arr) 
print(result)            