## 73. Find Three Common Elements In Three Sorted Array ##
## APPROACH-1>> Use Extra space , take intersection b/w arr1 and arr2 store it temp1 and after that take intersection b/w temp1 and arr3 store it temp 2 and return temp2 , TC= O(n1+n1+n3) , SC= O(temp1 + temp2 ) ##
## APPROACH-2>> Don't use Extra Space 
# Time Complexity is O(n1 + n2 + n3), Space Complexity is O(1) #   
def findCommonEle(arr1 , arr2 , arr3):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    i = 0 
    j = 0
    k = 0 
    while i < n1 and j < n2 and k < n3 :
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            print(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i ]< arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k+= 1
    
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 =[ 3, 4, 15, 20, 30, 70, 80, 120]
result = findCommonEle(arr1 , arr2 , arr3 )
print("Common Elements In three Sorted Arr " , result )



## 74. Count Inversion In An Array ##
# Time Complexity is O(n logn) , Space Complexity is O(n) #
def invCount(arr , p , q):
    __ , inv_count = mergeSort(arr , p , q)
    return inv_count

def mergeSort(arr , p , q):
    if p < q:
        mid = p + (q - p) //2
        leftArr , left_cnt = mergeSort(arr , p , mid)
        rightArr , right_cnt = mergeSort(arr , mid + 1 , q)
        merge , merge_cnt = merged(leftArr , rightArr)
        return merge , left_cnt + right_cnt + merge_cnt
    else:
        return [arr[p]] , 0    

def merged(leftArr , rightArr):
    i = 0 
    j = 0 
    cnt = 0
    result = []
    while i < len(leftArr) and j < len(rightArr) :
        if leftArr[i] <= rightArr[j]:
            result.append(leftArr[i])
            i += 1
        else:
            result.append(rightArr[j])
            cnt += len(leftArr) - i
            j += 1  
    result.extend(leftArr[i:])
    result.extend(rightArr[j:])
    return result , cnt

nums = [ 2 , 4, 1, 3, 5]
p = 0
q = len(nums) - 1
getInvCount = invCount(nums , p , q)
print("Number of inversions To sort the Array" , getInvCount)



## 79. MergeSorted Array ##
# Time Complexity is O(2n) , Space Complexity is O(1) #
def mergeSortArr(arr1 , arr2 ):
    m = len(arr1) - 1
    n = len(arr2) - 1 
    merge_ind = len(arr1) + len(arr2) - 1
    arr1.extend([0] * len(arr2) )
    while m >= 0 and n >= 0 :
        if arr1[m] > arr2[n]:
            arr1[merge_ind] = arr1[m]
            m -= 1
        else:
            arr1[merge_ind] = arr2[n]
            n -= 1
        merge_ind -= 1
    return arr1

    while m > 0 :
        arr1[merge_ind] = arr1[m]
        m -= 1
        merge_ind -= 1

    while n > 0 :
        arr1[merge_ind] = arr2[n]
        n -= 1
        merge_ind -= 1
num1 = [1, 5, 9, 10, 15, 20]
num2 = [1, 2, 3, 5, 8, 9]        
resultant = mergeSortArr(num1 , num2)     
print("Mergeed Sorted Array" , resultant)                   








## 80. Majority Element ##
# Time Complexity is O(n) , Space Complexity is O(1) #
def findMajority(nums):
    cand = None 
    count = 0
    for num in nums :
        if count == 0 :
            cand = num 
        count += ( 1 if num == cand else -1 )
    return cand 
def isMajority(nums , cand):
    n = len(nums)
    cnt = 0
    for i in range(n):
        if nums[i] == cand:
            cnt += 1
    if cnt > n//2 :
        return 1
    else :
        return  0           

def MajorityEle(arr):
    cand = findMajority(arr)
    result = isMajority(arr , cand)
    if result:
        print("Majority Ele" , cand)
    else:
        print("No Majority Ele" )    
arr = [ 3, 3, 4, 2, 4, 4, 2, 4, 4 ]
MajorityEle(arr)