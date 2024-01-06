## Deletion Of Node But the twist is Head is Not given , So not able to access the address of Previous node . 
## Only given Node(its Value)
## Time Complexity is O(1)  , Space Complexity is O(1)
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


## Reversal Of LinkedList ##
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


## Merge Two Sorted LinkedList ##
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








