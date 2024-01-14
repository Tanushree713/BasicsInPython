## 50. Deletion Of Node But the twist is Head is Not given , So not able to access the address of Previous node  ##
## Only given Node(its Value) ##
## Time Complexity is O(n)  , Space Complexity is O(1)
# use Logic:- For kth element deletion  ::condition::
#  1. Loop node.next is not None -> node.val = node.next.val (Interchanging NodeValues) , node.next = node.next.next (Linking Formantion)
#  2. If Last Node is remain then ,{ if node.next is None   -->  node = None }
class Node:
    def __init__(self ,data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self , x):
        self.val = x  # Value of Node 

        
    def deleteNodeWithoutHead(self , node):
       
    # Logic
        if node is None :
            return 
        if node.next is not None :
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None


## 51. Removal of Element from the LinkedList ##
# Time Complexity is O(n) , Space Complexity is O(1)
def removeElement(self , head , val ):
    if self.head is None:
        return 
    curr = self.head
    prev = None 
    while curr != None:
        if curr.val == val :
            if prev is not None : 
              prev.next = curr.next
            else:
              self.head = curr.next
        else:      
           prev = curr      
        curr = curr.next 

    return self.head        





## 52. Reversal Of LinkedList ##
# Time Complexity is O(n) , Space Complexity is O(1)

# Logic #
if self.head is None :
    return 
prev = None    
curr = self.head
next = None  
while curr != None :
    next = curr.next
    curr.next = prev 
    prev = curr
    curr = next

return prev



## 53. Merge Two Sorted LinkedList ##
# Time Complexity is O(m+n) , Space Complexity is O(m+n)

#logic#
def mergeTwolist(self, list1 , list2):

   if list1 is None :
      return list2

   if list2 is None :
       return list1
    
   temp = None
   if list1.val <= list2.val :
       temp = list1 
       temp.next = self.mergeTwolist(list1.next , list2)
   else:
       temp  = list2
       temp.next = self.mergeTwolist(list1 , list2.next)

   return temp     



## 54. Middle node of the LinkedList ##
# Time complexity is O(n/2) , Space Complexity is O(1)
# Approach using Hare-Tortoise Method

#logic#
def middleNode(self , head ):
    hare = self.head
    tortoise = self.head
    while hare != None and hare.next != None :
        tortoise = tortoise.next
        hare = hare.next.next

    return tortoise


## 55. LinkedList is Palindrome or Not ##
## Approach 1>> Use StackDS To Store temp one by one then take temp = head pointer , start pop from stack and do comparisons b/w poping element and temp
## Time Complexity is O(N) , Space Complexity is O(N)
# Approach 2>> a). Find Mid(diff cases in Even and Odd) of LL
#              b). Reversing remaining list from Mid.next
#              c). Do comparisons     
## Time Complexity is O(N) , Space Complexity is O(1)


# Palindrome LL 
def palindromeLL(self , head):
    
    if head is None and head.next is None :
        return True 

    middle = self.findMiddle(head)
    newhead = self.reverseHalf(middle.next) # second half LL new head 
    comparisonsResult  = self.comparisonInLL(head , newhead)
    return comparisonsResult

# Finding middle of LL 
def findMiddle( self , head):
    slow  = head
    fast = head
    while fast.next is not None and fast.next.next is not None :
        slow  = slow.next 
        fast = fast.next.next 
    return slow 
# Reversal of Half LL    
def reverseHalf(self , head):
    next = None
    curr = head
    prev = None
    while curr != None :
        next = curr.next 
        curr.next = prev
        prev = curr
        curr = next

    return prev

# Comparisons between List1 and List2
def comparisonInLL(self , head1 , head2): #firstHalf-->head1 and secondHalf-->head2
    while head1 is not None and head2 is not None :
        if head1.val  != head2.val :
            self.reverseHalf(head2)
            return False
        head1 = head1.next
        head2 = head2.next
    self.reverseHalf(head2) #getting back  original LL 
    return True



## 56. Check LinkedList Cycle-I ##
## Time complexity is O(m+n+c(i)) , Space complexity is O(1) ##
def testPresenceOfCycle(self , head):
    hare = head
    tortoise = head
    while tortoise is not None and hare is not None and hare.next is not None :
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise :
          return True 
    return False      


## 57. Check LinkedList Cycle-II (Find Starting point In LL) ##
## Time Complexity is nearlyto O(N)  , Space Complexity is O(1) 
# Appraoch>>
# >>1.Find Presence of Cycle   
# >>2.Take Another head then start moving head by one step and same time meetpoint by one step 
# >>3. Again Point where they meet is starting point of the cycle 
def findStartPositionOfCycle(self , head):
    if head is None or head.next is None :
        return None
    entry = head
    slow = head
    fast = head
    # cycle exist or not 
    while fast is not None and fast.next is not None  :
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            while slow != entry:
                entry = entry.next
                slow = slow.next
            return entry
        return None         






## 58. Maximum Twin Sum ##
## First node (0 indexed) & last node(n-i-1 indexed) , second node(1 indx) & second last node(n-i-2 indx) ##
## Add them return max of them 
## Time complexity is O(n) , Space Complexity is O(1)
##Approach >>
#>>1. FindMiddle
#>>2. ReverseHalf give new head
#>>3.Add them , sum = head.val + newhead.val
#>>4.Find Maxsum = max(Maxsum , sum) and return Maxsum
def maxTwinSum(self ,head):
    sum = 0
    maxSum = 0
    if head is None and head.next is None: # empty
        return 0
    if head.next is not None and head.next.next is None : # two nodes are present
        sum = head.val + head.next.val
        return sum

    middle = self.findMiddle(head)
    reversedHead = self.reversehalf(middle) #not middle.next 
    while head is not None and reverseHead is not None :
        sum = head.val + reversedHead.val
        maxSum = max(maxSum, sum)
        head = head.next
        reversedHead = reversedHead.next
    return maxSum

    def findMiddle(self ,head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next

        return slow
    def reversehalf(self , head):
        prev = None
        curr = head
        next = None
        while curr is not None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        return prev               




## 59. Remove the nth Node from the end of LL ##
## Time Complexity is O(n) , Space Complexity is O(1)
##Approach>> 
##>> take fast pointer run till then n(position) 
##>> Take slow = head and fast = getting node from outside the loop
##>> start moving again till fast.next != None
##>> point where slow is stop that is our prev node , where need put value pointing next--> next and store in deletenode
##>> Return head
def removeNnodeAtEnd(self , head):
    fast = head
    slow = head
    for i in range(n): #starts from 0 till nth node , where n= position of node to be deleted
        fast = fast.next
    if fast is None :
        return head.next #reaching at Last pointer

    while fast.next is not None :
        slow = slow.next 
        fast = fast.next
    deletenode = slow.next
    slow.next = slow.next.next  

    return  head 










        














