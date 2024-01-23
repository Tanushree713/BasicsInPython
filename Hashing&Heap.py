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
        


