## 1. Arrays ##
# 1. Maximum And Minimum Ele #
# TC is O(n) , SC is O(1)
def maxAndmin(arr , i , j):

    if i == j :
        max_val = arr[i]
        min_val = arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]    

    else:
        mid = i + (j - i) // 2   
        max_l , min_l  = maxAndmin(arr , i , mid)
        max_r , min_r = maxAndmin(arr , mid + 1, j ) 
        if max_l < max_r :
            max_val = max_r
        else:
            max_val = max_l

        if min_l < min_r :
            min_val = min_l 
        else:
            min_val = min_r

    return max_val , min_val                      
arr = [ 2, 6 , 8 , 1, 19 , 5 , 3]
i = 0
j = len(arr) - 1
# maxValue , minValue  = maxAndmin(arr , i , j)
# print("Max and Min " , maxValue , minValue)


# 2. Best time To Sell And Stock #
# TC is O(n) , SC is O(1) #
def timeToSell(price):
    max_profit = 0
    min_price = float('inf')
    n = len(price)
    for i in range(n):
        if price[i] < min_price :
            min_price = price[i]
        elif price[i] - min_price > max_profit:
            max_profit = price[i] - min_price
    return max_profit
nums = [ 7 , 1, 4 , 7 , 15]
# result = timeToSell(nums)
# print("Max profit " , result )



# 3. Max Product SubArray #
# TC is O(n) , SC is O(1)  #
def maxProductSubArr(arr):
    suffix = 1
    prefix = 1
    product = 0 
    n = len(arr)
    for i in range(n):
        if suffix == 0 :
            suffix = 1
        elif prefix == 0 :
            prefix = 1  
        else:
            prefix = prefix * arr[i]
            suffix = suffix * arr[n -i - 1] 
            product = max(product , max(prefix , suffix))
    return product 
arr = [2 , 3 , 4, -1 , 0 , 7 , 2]   
# result = maxProductSubArr(arr)
# print("MaxSubArrProduct" , result)         


# 4. 3Sum #
# TC is O(n^2) , SC is O(k) #
def TripleSum(nums):
    i = 0 
    n = len(nums)
    result = []
    nums.sort()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 
        left = i + 1
        right = n - 1
        while  left < right :
            total = nums[i] + nums[left] + nums[right]
            if total == 0 :
                result.append([nums[i] , nums[left] ,  nums[right]]) 
                while left < right and nums[left] == nums[left + 1]:
                    left += 1 
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1 
                left += 1
                right -= 1          
            elif total < 0 :
                left += 1
            else:
                right -= 1
    return result                     

arr = [ 1 , 0 , -1 , 2, -3 , 5]
# result = TripleSum(arr)
# print("TripleSum" , result )


# 5. kth Smallest #
#APP1>>
# TC is O(nlogn) , SC is O(1) #
def kthSmallest1(arr , p , q , k ):
    if  p < q :
        m = partition(arr , p , q)
        if m == k :
            return arr[m - 1]
        elif m < k :
             return kthSmallest1(arr , m , q , k)
        else:
             return kthSmallest1(arr , p , m - 2, k) 
def partition(arr , p , q):
    i = p
    pivot = arr[p]
    for j in range(i + 1, q+1 ):
        if arr[j] < pivot :
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]  
    arr[i] , arr[p] = arr[p] , arr[i]
    return i + 1

arr = [ 6 , 8 , 1, 19 , 3]
p = 0
q = len(arr) - 1
k = 3
# result = kthSmallest1(arr , p , q, k)
# print("Kth Smallest Number is " , result )



#APP2>>
# TC is O(nlogk ) , SC is O(k) #
from heapq import heappop , heappush 
def kthSmallest2(nums , k ):
    heap = []
    for num in nums :
        if len(heap) < k :
            heappush(heap , -num)
        else:    
            if  num <  -heap[0] :
                heappop(heap) 
                heappush(heap , -num)
    return -heap[0]  
arr = [ 6 , 8 , 1, 19 , 3]
k = 2
# result = kthSmallest2(arr , k)
# print("KthSmallest2" , result )




# 6. Repeat And Missing Number Arr #
# TC is O(n) , SC is O(1) #
def repeatAndmissEle(nums):
    repeat = 0
    missing = 0 
    n = len(nums)
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0 :
            repeat = abs(num)
        else:
            nums[index] = -nums[index]    
    for i in range(n):
        if nums[i] > 0:
            missing = i+1
    return repeat, missing


nums = [ 7, 1, 5, 4, 6, 3 , 3]    
# result = repeatAndmissEle(nums)
# print("Repeat And Missing:", result)




# 7. Merge Intervals #
# TC is O(nlogn ) , SC is O(1) #
def mergeIntervals(intervals)  :
    result = []
    if not intervals :
        return []
    intervals.sort(key = lambda x : x[0])
    merged = [intervals[0]]    
    for i in range(1 , len(intervals)) :
        curr_interval = intervals[i]
        last_merged_interval = merged[-1]
        if curr_interval[0] <= last_merged_interval[1]:
            merged[-1] = [last_merged_interval[0] , max(curr_interval[1] , last_merged_interval[1])]
        else:
            merged.append(curr_interval) 
    return merged        
intervals = [[2, 3] , [3 , 8 ] , [1, 6] , [7, 10]]               
# result = mergeIntervals(intervals)
# print("Mergeintervals" , result)            



# 8. Merge Sorted Arr #
# TC is O(n) , SC is O(1)  #
def mergeSortedArr(arr1 , arr2 ):
     m = len(arr1) -1 
     n = len(arr2) - 1
     merge_indx = len(arr1) + len(arr2) - 1
     arr1.extend([0] * len(arr2))
     while m >= 0 and n >= 0 :
        if arr1[m] > arr2[n]:
            arr1[merge_indx] = arr1[m]
            m -= 1
        else:
            arr1[merge_indx] = arr2[n]
            n -= 1
        merge_indx -= 1
     while m >= 0 :
        arr1[merge_indx] = arr1[m]
        m -= 1
        merge_indx -= 1
     while n >= 0 :
        arr1[merge_indx]  = arr2[n]
        n -= 1
        merge_indx -= 1

     return arr1    

arr1 = [ 2  , 4 , 6, 8] 
arr2 = [ 1 , 3, 5, 7]
# result = mergeSortedArr(arr1 , arr2 ) 
# print("Merged Sorted Arr " , result )   



# 9. Majority  Elements #
# TC is O(n) , SC is O(1)  #
def findMajority(nums):
    cand = None
    count = 0
    for num in nums :   
        if count == 0 :
            cand = num
        count += (1 if num == cand else -1 )   
    return cand 

def isMajority(nums , cand):
    n = len(nums)
    cnt = 0 
    for i in range(n):
        if nums[i] == cand :
            cnt += 1
    if cnt > n//2 :
        return True
    else:
        return False               

def majorityEle(nums):
    cand = findMajority(nums)
    result = isMajority(nums , cand)
    if result :
        print("Is Majority " , cand)
    else:
        print("Not Majority ")    
# nums = [2 , 3 ,3, 3, 2, 5 , 3]
# result = majorityEle(nums)


# 10 . Find Duplis #
#APP1>>
# TC is O(n) , SC is O(n) #
def findDupli1(nums) :
    seen = set()
    dupli = []
    for num in nums :
        if num in seen :
            dupli.append(num)
        seen.add(num)  
    return dupli  
nums = [ 7, 1, 5, 4, 6, 3 , 3]  
# result = findDupli1(nums)   
# print("Duplicates1 are " , result )       


#APP2>>
# TC is O(n) , SC is O(1) #
def findDupli2(nums):
    xor_res = 0
    for num in nums :
        xor_res ^= num 
    for i in range(1 , len(nums)):
        xor_res^= i 
    return xor_res

# nums = [ 2, 1, 5, 4, 6, 3 , 3]  # won't work when elements >= n
# result = findDupli2(nums)   
# print("Duplicates2 are " , result ) 



# 11. Space Optimization #
# TC is O(b-a) , SC is O(k)  #
def spaceOptimize( a, b ):
    marked  = 0 
    for num in range(a , b + 1) :
        if num % 2 == 0 or num % 5 == 0 :
            marked |= (1 << (num - a))
    multiples = []        
    for i in range(b - a + 1):
        if (marked & (1 << i)) != 0:
            multiples.append(a + i)
    return multiples
a = 10
b = 20
# result = spaceOptimize(a, b)
# print("multiples of 2 and 5 b/w a to b" , result )            


# 12. MergeOperationTo make palindromeARR #
# TC is O(n) , SC is O(1) #
def makePalindrome(arr) :
    i = 0 
    j = len(arr) - 1
    cnt = 0 
    while i < j :
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            arr[i+1] = arr[i] + arr[ i+ 1] 
            cnt += 1
            i += 1
        else:
            arr[j-1] = arr[j] + arr[j-1]
            cnt += 1
            j -= 1
    return cnt 
arr = [ 1, 2, 3 , 8 , 4 ,  5 , 1]
# result = makePalindrome(arr) 
# print(" MergeoperationTo make palindrome ARR :" , result )             


# 13. Power(a , n)   #
# TC is O(logn ) , SC is O(1)  #
def power(a , n ):
    if n ==  0 :
        return 1
    elif n == 1 :
        return a   
    elif n < 0 :
        n = -n 
        a = 1 / a
        return power(a , n)      
    else:
        mid = n // 2
        b = power(a , mid )
        result = b * b 

    if n % 2 :
        return  a * result 
    else :
        return result  
a = 2
n = 6
# result = power(a , n )
# print("Value of power of a is :" , result)




# 14. Next Permutation #
# TC is O(n) , SC is O(1)  #
def nextPermute(arr) :
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[ i + 1]:
        i -= 1
    if i == -1 :
        return reversed(arr)
    else:
        j = len(arr) - 1
        while arr[i] > arr[j]:
            j -= 1
        arr[i] , arr[j] = arr[j] , arr[i]    
        arr[i+1:] = reversed(arr[i+1:])  
        return arr         
arr = [ 1, 3, 2]
# result = nextPermute(arr)
# print("resultant is " , result )


# 15. Sum Pairs #
# TC is O(n) , SC is O(1) #
def sumPairs(arr  , key ):
    n = len(arr)
    for i in range(n):
        if arr[i ] > arr[i+1]:
            break
    left = (i+1 ) % n 
    right = i  
    while left != right :
        if arr[left] + arr[right] == key :
            return True 
        elif arr[left] + arr[right] < key :
            left  = (left + 1 ) % n 
        else:
            right  = (n + right - 1) % n 

    return False             
arr =[ 11, 15, 26, 38, 9, 10]
key  = 26
# result = sumPairs(arr , key )
# print("Sum Pairs " , result )


# 16. Sort Colors #
# TC is O(n) , SC is O(1) #
def sortColors(nums):
    curr = p0 = 0
    p2 = len(arr) - 1
    while curr < p2 :
        if nums[curr] == 0 :
            nums[p0] , nums[curr] = nums[curr] , nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2 :
            nums[p2] , nums[curr] = nums[curr] , nums[p2]
            p2 -= 1
        else:
            curr += 1

    return nums 
arr = [ 2 , 1 , 0 , 1, 2, 0]       
# result = sortColors(arr)
# print("Sorted Colors " , result)  



# 17. Rotate Array #
# TC is O(n) , SC is O(1) #
def reverseArr(arr , start , end ) :
    while start < end :
         arr[start] , arr[end] = arr[end ] , arr[start]
         start += 1
         end -= 1
    return arr 
def rotateArr(arr , k ) :
    n = len(arr)
    k = k % n
    reverseArr(arr , 0 , n - 1)
    reverseArr(arr , 0 , k - 1)
    reverseArr(arr , k , n - 1)
    return arr
arr = [ 2 , 3, 4 , 5, 7 , 8 , 10 ]
k = 5
# result = rotateArr(arr , k)
# print("Rotated k Arr" , result )





# 18. Consecutive Ones #
# TC is O(n) , SC is O(1)  #
def countConsectveOnes(arr):
    n = len(arr)
    count = 0 
    maxcnt = 0 
    for i in range(n):
        if arr[i] == 1:
            count += 1
            maxcnt = max(maxcnt , count )
        else:
            count = 0 
    return maxcnt 
arr = [ 1 , 1, 1 , 0 ,0 , 1, 1, 3, 1, 0]    
# result = countConsectveOnes(arr)    
# print("The Consecutive Ones is " , result )       


##----------------------------------------##

# 19. Spiral Matrix #
# TC is O(m*n) , SC is O(m*n)  #
def spiralMatrix(arr):
    left = 0
    right = len(arr[0]) - 1
    top = 0
    bottom = len(arr) - 1
    result = [ ]
    while left <= right and top <=  bottom :
        for i in range(left , right +  1):
            result.append(arr[top][i])
        top += 1
        for i in range(top , bottom + 1 ):
            result.append(arr[i][right])
        right -= 1  
        if top < bottom  :    
            for i in range(right , left - 1, -1 ):
                result.append(arr[bottom][i]) 
            bottom -= 1
        if left < right :    
            for i in range( bottom , top - 1 , -1 ) :
                result.append(arr[i][left])  
            left += 1
    return result 
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = spiralMatrix(arr)
# print("SpiralMatrix", result )




# 20. Matrix Diagonal Sum #
# TC is O(n) , SC is O(1) #
def matrixDiagSum(arr) :
    res = 0
    n = len(arr)
    for i in range(n):
        res += arr[i][i]
        res += arr[i][n-i-1]
    if n  % 2 :
        res -= arr[n//2][n//2]
    return res    
arr = [[1, 2, 3 , 0], [4, 5, 6 , 0], [7, 8, 9 , 0] , [11, 12, 13 , 0]]
# result = matrixDiagSum(arr)
# print("Matrix Diagonal Sum " , result )



# 21. Count Negative Numbers In a Sorted Matrix #
# TC is O(m+n) , SC is O(1)  #
def countNegNum(arr) :
    rows = len(arr[0])
    cols  = len(arr)
    i = 0 
    j = rows - 1
    count = 0 
    while i < cols and j >= 0 :
        if arr[i][j] < 0 :
            count += cols - i 
            j -= 1
        i += 1
    return count           
arr = [ [1, 2, 3, -4],
    [5, 6, -7, -8],
    [9, 10, -11, -12]]
# result = countNegNum(arr)
# print("Count Neg Num " , result )


#  22. Richest Customer wealth #
# TC is O(m*n), SC is O(1) #
def richestWealth(accounts) :
    maxSum = 0 
    for wealth in accounts :
        total =  sum(wealth)
        maxSum = max( maxSum  , total )
    return maxSum
arr = [[1, 2, 3, -4],
    [5, 6, -7, -8],
    [9, 10, -11, -12]]    
# result = richestWealth(arr)
# print("Richest wealth " , result )         



# 23. Toeplitz Matrix #
# TC is O(m*n) , SC is O(1)  #
def toeplitzMat(arr) :
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows - 1):
        for j in range(cols-1):
            if arr[i][j] != arr[i+1][j+1]:
                return False
    return True 
# arr = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# result = toeplitzMat(arr)    
# print("Toeplitz Mat " , result )            



# 24. Rotate Image #
# TC is O(n^2) , SC is O(1)  #
def rotateImage(mat) :
    n = len(mat)
    for i in range(n - 1):
        for j in range(i+1 , n):
            mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
    for i in range(n) :       
        mat[i] = list(reversed(mat[i]) )  
    return mat 
mat = [[1, 2, 3 ], [4, 5, 6 ], [7, 8, 9 ]]      
# result = rotateImage(mat)
# print("Matrix is Rotated" , result )



# 25. Transposal Matrix #
# TC is O(m*n)  , SC is O(m*n)  #
def transposalMat(mat):
    rows = len(mat) 
    cols = len(mat[0])
    res = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = mat[i][j] 
    return res        
mat = [[1,2,3],[4,5,6],[7,8,9]]
# result = transposalMat(mat)
# print("Transposal Matrix  " , result )



# 26. Set Matrix Zeroes #
# TC is O(n^2)  , SC is O(1)  #
def setMatrixZeroes(arr):
    m = len(arr)
    n = len(arr[0])
    col0 = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0 :
                arr[i][0] = 0 
                if j != 0 :
                    arr[0][j] = 0
                else:    
                    col0 = 0 
    for i in range(m-1 , -1 , -1 ) :
        for j in range(n - 1, 0 , -1 ):
            if arr[i][j] != 0 :
                if arr[i][0] == 0  or arr[0][j] == 0 :
                     arr[i][j] = 0 
    if arr[0][0] == 0 :
        for j in range(n):
            arr[0][j] = 0 
    if col0 == 0 :
        for i in range(m) :
            arr[i][0]  = 0 
    return arr                                             

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# result = setMatrixZeroes(matrix)
# print("Set matrix" , result )



# 27. Reshape Matrix #
# TC is O(m*n) , SC is O(m*n ) #
def reshapeMat(mat , r, c):
    m = len(mat)
    n = len(mat[0])
    res = [[0] * c for _ in range(r)]
    originalLen = m * n 
    if originalLen != r*c :
        return mat
    for i in range(originalLen):
        res[i // c][i % c] = mat[i // n ][ i % n] 
    return res
mat = [[1,2],[3,4]]
# result = reshapeMat(mat , 1, 4 )
# print("Reshaped" , result  )         



# 28. Flip Image #
# TC is O(n^2) , SC is O(1) #
def flipImage(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(n):
        mat[i] = list((reversed(mat[i])))
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 :
                mat[i][j] = 0 
            else:
                mat[i][j] = 1
    return mat
mat = [[1,1,0],[1,0,1],[0,0,0]]  
# result = flipImage(mat)
# print("Flpi Image " , result )                         


##-------------------------------------##

# 29. Reverse String #
# TC is O(n) , SC is O(n) #
def reverseStr(string):
    left = 0
    right = len(string) - 1 
   # string = list(string) 
    while left < right :
        string[left] , string[right] = string[right] , string[left]
        left += 1
        right -= 1
    return string  # return ''.join(string)
string = ["h","e","l","l","o"] 
# res = reverseStr(string)
# print("Reversed string " , res)       



# 30. First Unique Char #
# TC is O(n) , SC is O(n)  #
from collections import Counter 
def firstUniqueChar(string):
    countChar = Counter(string)
    for index , char in enumerate(string):
        if countChar[char] == 1:
            return index, char
    return -1         
string = "leetcode"
# result = firstUniqueChar(string)
# print("FirstUnique Char" , result )



# 31. Reverse Words In String #
# TC is O(n)  , SC is O(n) #
def reverseWords(string):
    getwords = string.split(" ")
    getreversedWords = getwords[::-1]
    getReversal = ' '.join(getreversedWords)
    return getReversal
string = "the sky is blue" 
# result = reverseWords(string)
# print("Reversed Words : " , result )        


# 32. Length Of Last Words #
# TC is O(n) , SC is O(n)  #
def lengthOfLastWords(string):
    getWords = string.split(" ")
    getLastwords = getWords[len(getWords) - 1]
    return len(getLastwords)
string = "Tanu is good and smart women"
# result = lengthOfLastWords(string)
# print("Length of last String" , result)


# 33. Longest common Prefix #
# TC is O(n*m*log(k)) , SC is O(k)  #
def longestCommonPrefix(string) :
    common = []
    if not string :
        return ""
    string.sort()
    firstW = string[0]
    lastW = string[len(string) - 1]
    for i in range(len(firstW)):
        if i < len(lastW) and firstW[i] == lastW[i] :
            common.append(firstW[i])
        else:
            break 
    return ''.join(common)
string = ["flower","flow","flight"]
# result = longestCommonPrefix(string)
# print("Longest Common Prefix : " , result)



# 34. Longest substring Without Repeat Char #
# TC is O(2n) , SC is O(n)  #
def longestSubstr(string):
    maxlen = 0 
    left = 0
    charset = set()
    for right in range(len(string)):
        if string[right] in charset:
            charset.remove(string[left])
            left += 1
        charset.add(string[right])
    maxlen = max(maxlen , right-left + 1)    
    return maxlen
string = "abcabcbb"    
# result = longestSubstr(string)   
# print("LongestSubstr" , result )             


# 35. Jewels And Stones #
# TC is O(s+j)  , SC is O(j)  #
def jewelsAndStones(jewels , stones):
    jewelSet = set(jewels)
    count = 0
    for s in stones:
        if s in jewelSet :
            count += 1
    return count 
jewels = "aA"
stones = "aAABBBb"
# result = jewelsAndStones(jewels , stones)
# print("Jewels And Stones" , result )            
 

# 36. Valid Anagram #
# TC is O(2n)) , SC is O(2n) #
from collections import Counter
def validAnagram(str1 , str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    if counter1 == counter2 :
        return True 
    return False 
str1 = "anagram"
str2 = "nagara"
# result = validAnagram(str1 , str2 )
# print("ValidAnagram is" , result )


# 37. Reverse Vowels of string #
# TC is O(n) , SC is O(1) #
def reverseVowels(string):
    vowels = "AEIOUaeiou"
    left = 0
    right = len(string) - 1
    string = list(string)
    while left < right :
        while left < right and string[left] not in vowels :
            left += 1
        while left < right and string[right] not in vowels :
            right -= 1
        string[left], string[right] = string[right], string[left]     
        left += 1
        right -= 1
            
    return ''.join(string)        
string = "hello"
# result = reverseVowels(string)
# print("Reverse vowels :" , result )



# 38. Valid Palindrome #
# Tc is O(n) , Sc is O(1)  #
def sanitized(s):
    sanitize = ""
    for char in s :
        if char.isalnum():
            sanitize += char.lower()
    return sanitize      
def validPalindrome(string):
    string = sanitized(string)
    left = 0
    right = len(string) - 1
    while left < right :
       if string[left] != string[right]:
        return False
       left += 1
       right -= 1
    return True 
string = "race a car"
# result = validPalindrome(string)
# print("ValidPalindrome" , result )       


# 39. Redistribute Make Equal Char #
# Tc is O(n)  , Sc is O(n) #
def redistributemakeEqual(words):
    charcount = Counter()
    n = len(words)
    for w in words :
        charcount.update(w)
    for count in charcount.values():
        if count % n != 0 :
            return False 
    return True 
string = ["abc" , "abc", "aabc"]
# result = redistributemakeEqual(string)
# print("redistribute Make Equal :" , result )


# 40. Balance String #
# Tc is O(n) , SC is O(1)  #
def balanceStr(string):
    count = 0 
    r = 0
    for i in range(len(string)):
        if string[i] == "R":
            r += 1
        elif string[i] == "L":
            r -= 1
        if r == 0 :
            count += 1
    return count        
string = "RLRLRLLL"
# result = balanceStr(string)
# print("Split balanced String" , result)




##-------------------------------------##

# 41. Fibonacci number #
# TC is O(n) , SC is O(1)  #
def fibonacciNum(n):
    if n == 0 or n == 1:
        return n 
    else:
        return fibonacciNum(n-1) + fibonacciNum(n-2)  
n =  3  
# result = fibonacciNum(n)
# print("Fibonacci Num" , result)



# 42. find Power of Four #
# Tc is O(n) , Sc is O(1)  #
def findPowerFour(n):
    if n <= 0  :
        return False
    elif n == 1:
        return True
    else:
        return n % 4 == 0 and findPowerFour(n // 4)      
n = 20
# result = findPowerFour(n)
# print("Find power Four" , result )        


# 43. Sum of Digits #
# TC is O(n) , Sc is O(1)  #
def sumOfDigit(n):
    if n == 0 or n == 1 :
        return n 
    else :
        return n % 10 + sumOfDigit(n//10) 
n =  4321          
# result = sumOfDigit(n)
# print("Sum Of Digit :" , result )


# 44. Find GCD or HCF Of Two Number #
# Tc is O(log(min(a , b))) , Sc is O(1)  #
def findGCD(a , b):
    if b == 0 :
        return a
    else:
        return findGCD(b , a%b ) 
a = 2 
b = 5        
# result = findGCD(a , b)           
# print("Finding GCD :" , result )



# 45. All Subsets Sum #
# Tc is O(2^n) , Sc is O( n + 2^n) #
def sumOfAllSubsets(arr  , i , sum , result):
    if i == len(arr):
        result.append(sum)
        return 
    else :
        sumOfAllSubsets(arr , i + 1, sum + arr[i] , result) 
        sumOfAllSubsets(arr , i + 1 , sum , result)         

nums = [1 , 2, 3]
result = []
i = 0 
sum = 0
sumOfAllSubsets(nums , i , sum , result)
resultant = list(set(result))
resultant.sort()
# for r in resultant:
#     print(r , end=" ")


##---------------------------------------##


# 46. 2-D Binary Search #
# TC is O() , SC is O() #
def binarysearch2D(arr , target):
    m = len(arr) 
    n = len(arr[0])
    left = 0
    right = m*n - 1
    while left <= right :
        mid = left + (right - left )// 2
        mid_Ele = arr[mid//n][mid%n]
        if mid_Ele == target :
            return True
        elif mid_Ele < target :
            left = mid + 1
        else :
            right = mid - 1
    return False 
arr = [[ 1, 2 ,3 ] , [4, 5, 16] , [7, 8 ,9] ] 
target = 6
# result = binarysearch2D(arr , target)
# print("Binary search In 2D " , result )                     



# 47. Search Position(Index of target) #
# Time Complexity is O(logn) , Space Complexity is O(1) #
def searchPos(arr , k ):
    i = 0
    j = len(arr) - 1
    while i < j :
           mid  = i + (j -i) // 2
           if arr[mid] == k :
             return mid
           elif arr[mid] < k :
              i = mid + 1
           else:
            j = mid - 1
    return -1         
arr = [1 , 2 , 3, 4, 5] 
k = 4
# result  = searchPos(arr , k ) 
# print("Searched Element " , result )               



# 48. Search In Rotated sorted Array #
# Time Complexity is O(logn) , Space complexity is O(1) #
def searchRotatedArr(arr , k):
   i = 0
   j = len(arr) - 1
   while i <= j :
        mid  = i + (j- i) // 2
        if arr[mid] == k:
            return mid
        if arr[i] <= arr[mid]:
            if arr[i] <= k and k <= arr[mid] :
                j = mid - 1
            else:
                i = mid + 1
        else:
            if arr[mid] <= k and k <= arr[j]:
                i = mid + 1
            else:
                j = mid - 1
   return -1
arr = [ 7 , 8 , 9 , 1, 2, 3 , 4 , 5 , 6]  
k = 9
result = searchRotatedArr(arr , k)                    
print("Sorted Arr " , result )            




    
