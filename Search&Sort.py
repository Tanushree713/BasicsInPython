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