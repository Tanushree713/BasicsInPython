# Sorting Algo #
#1. BubbleSort# 
# Tc is O(n^2), Sc is O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr 
arr = [ 6 , 4 , 2 , 1 , 5]
result = bubbleSort(arr)
print("Sorted arr Using BubbleSort" , result )


#2. SelectionSort#
# Tc is O(n^2) , Sc is O(1) #
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mid_indx = i 
        for j in range(i+1 , n):
            if arr[mid_indx] > arr[j]:
                mid_indx = j 
        arr[i] , arr[mid_indx] = arr[mid_indx] , arr[i]
    return arr
arr = [ 6 , 4 , 2 , 1 , 5]
result = selectionSort(arr)
print("Sorted arr Using SelectionSort ", result )


#3. InsertionSort#
# Tc is O(n^2) , Sc is O(1) #
def insertionSort(arr):
    n = len(arr)
    for i in range(1 , n):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j- 1
        arr[j+1] = key 
    return arr 
arr = [ 6 , 4 , 2 , 1 , 5]  
result = insertionSort(arr)
print("Sorted arr Using InsertionSort ", result )       


#4. HeapSort#
# Tc is O(nlogn) , Sc is O(1) #

#5. Quicksort#
# Tc is O(nlogn) , Sc is O(1) #
def quickSort(arr , p , q):
    if p < q :
        mid = partition(arr , p , q)
        quickSort(arr , p , mid - 1)
        quickSort(arr , mid + 1 , q)
        return arr 
def partition(arr , p , q):
    i = p 
    pivot = arr[p]
    for j in range(i+1 , q+1):
        if pivot > arr[j]:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[p] = arr[p] , arr[i]
    return i 
arr = [ 6 , 4 , 2 , 1 , 5] 
p = 0 
q = len(arr) - 1 
result = quickSort(arr , p , q)
print("Sort arr Using QuickSort" , result)
 


#

       






