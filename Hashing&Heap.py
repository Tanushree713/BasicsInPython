## 69. Find  K-Frequent Elements ##
# Time Complexity is O(n) , Space Complexity is O(n) #
from collections import Counter
import heapq
class Solution(object):
    def kFrequentElements(self , nums , k):
         # Base Condition 
        if k == len(nums):
            return set(nums)   # unique elements
        count = Counter(nums)
        return heapq.nlargest(k , count.keys() , key=count.get)    


## 70. Kth Largest Element ##
# Time Complexity is O(nlogk) , Space Complexity is O(log k)

class Solution(object):
    def findKthLargest(self , nums , k):
        heap = []   #minHeap
        for num in nums :
            if len(heap)  < k :   # constraints k ,only k-elements push inside the heap 
                heapq.heappush(heap , num)
            else:
                if num > heap[0] :  #smallest Ele in heap and curr Ele , if heap[0] is smaller then pop it 
                 heapq.heappop(heap)
                 heapq.heappush(heap , num)  # push that num ELe into heap , if num is greater 
        return heap[0]           


## 71. Kth Smallest  Element ##
# Time Complexity is O(nlogk) , Space Complexity is O(logk)
class Solution(object):
    def findKthSmallest(self , nums , k):

        heap = []  #maxHeap
        for num in nums :
            if len(heap) < k :
                heapq.heappush(heap , -num)
            else:
                if num < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap , -num)

            return -heap[0]            


## 72. kth Closest Elements to given Value In Array ##
# Time Complexity is O(n log k) , Space Complexity is O(log k ) #
# Given k , x , arr ...according to x value return kth smallest elements #
from heapq import heappush , heappop
class Solution(object):
    def kthClosest(self , arr , k ,x):
        n = len(arr)
        heap = [] # MaxHeap
        for i in range(n):
            heappush(heap , (abs(arr[i] - x) , arr[i]))
        result = []
        for i in range(k):
            result.append(heappop(heap)[1])    
        return  sorted(result) 
arr = [1 , 2, 3, 4 , 5]
k = 4        
x = 3
solution1 = Solution()
result1 = solution1.kthClosest(arr , k , x)
print("kth closest Ele " , result1)



## 73. Smallest Positive Number Missing In unsorted Array ##
# Time Complexity is O() , Space Complexity is O() #
class Solution(object):
    def miss_smallestPositiveNum(self, arr1 ):
        numset = set() # hashset
        n = len(arr1)
        for i in range(n):
            if arr[i] > 0 :
                numset.add(arr[i])
        for i in range(1 , n + 2): # We iterate up to n+2 because the smallest missing could be n+1
            if not i in numset :
                return i 
arr = [ 1, 2 , 3, 4, 5]
solution2 = Solution()
resultant = solution2.miss_smallestPositiveNum(arr)
print("MissedSmallPositive-Ele",resultant)


