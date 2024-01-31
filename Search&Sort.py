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