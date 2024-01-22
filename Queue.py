## 66. Time Needed To Buy Tickets ##
# Time Complexity is O(n) , Space Complexity is O(1) #
## Approach 1>>> without QUEUE
class Solution(object):
    def timeNeededToBuy(self , tickets , k):  # k = 2 
        time = 0 
        while i in range(len(tickets)):   #[2, 8 , 5, 8]
            if tickets[i] < tickets[k]:   #[  time = 2 as 2 < 5]
                time += tickets[i]
            else:                         # [  time = 5 as 8 > 5]
                time += tickets[k]
            if i > k and tickets[i] >= tickets[k] :
                time = time - 1
        return time 


## Approach 2>>>  With QUEUE
# Time Complexity is O(n) , Space  Complexity is O(n)
from collections import deque 
class Solution(object):
    def timeNeededBuyTickets(self , tickets , k):
        time = 0 
        q = deque(range(len(tickets)))  # initialize and push al person inside the queue
        while q :
            index = q.popleft()
            tickets[index]-= 1
            time += 1

            if tickets[index] == 0 and index == k :
                break 
            q.append(index)

        return time 
queue = [  2, 3, 2] 
k = 2           
solutions = Solution()
result = solutions.timeNeededBuyTickets(queue ,  k)
print("Person Needed Time To buy Tickets " , result)
        






