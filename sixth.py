## Selection Sort ##
## Time Complexity is O(n^2) ##
# First Elemnet in each passes get sorted . No need to Update 1st element in each #
arr = [20 , 39 , 13 , 17 , 11 , 75 , 5]
def selectionSort( arr ):
    n = len(arr)
    for i in range(n):
        mid_indx = i
        for j in range(i+1,n):
            if arr[j] < arr[mid_indx]:
                # update the value of mid_indx 
                mid_indx = j
                # Swap the element of an array
        arr[i] , arr[mid_indx] = arr[mid_indx] , arr[i]
    return arr 

result = selectionSort(arr) 
print(result)    
