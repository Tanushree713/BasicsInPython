## BUBBLESORT Array ##
## Time complexity is O(n^2) ##

arr = [ 87 , 20 , 50 , 70 , 5, 15 , 90]
n = len(arr)

def bubbleSortAlgo(arr) :
    for i in range(n):
        # No Need To update last element(already get sorted in 1st pass) again nad again use Logic # 
        for j in range(n-i-1):
         if arr[j] > arr[j+1]:
            #Swaps the elements #
            arr[j], arr[j+1] = arr[j+1] , arr[j]
    return arr 

result  = bubbleSortAlgo(arr)
# print(result)


def searchIn2D(arr , target):
    n = len(arr[0])
    m = len(arr)
    left = 0 
    right = m * n - 1
    found = False
    result = []
    while left < right  :
        mid  = left + (right - left) // 2
        midEle = arr[mid//n][mid%n]
        if midEle == target :
            found = True 
            row = mid // n
            col = mid % n 
            return (row , col)
        elif midEle < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1               
arr = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
] 
target = 9
res = searchIn2D(arr , target)
if res != -1 :
    print("found at" , res)
else:
    print("not found")    