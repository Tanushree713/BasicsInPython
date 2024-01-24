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
        heap = []
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
    def findKthLargest(self , nums , k):

        heap = []
        for num in nums :
            if len(heap) < k :
                heapq.heappush(heap , -num)
            else:
                if num < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap , -num)

            return -heap[0]            


## 72. 