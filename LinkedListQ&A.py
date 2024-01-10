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
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    # Helper function to reverse a linked list
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    # Helper function to find the middle of the linked list
    def find_middle(node):
        slow = node
        fast = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    if not head or not head.next:
        # An empty list or a single-node list is a palindrome
        return True

    # Find the middle of the linked list
    middle = find_middle(head)

    # Reverse the second half of the linked list
    reversed_second_half = reverse_list(middle)

    # Compare the reversed second half with the first half
    while reversed_second_half:
        if head.value != reversed_second_half.value:
            return False
        head = head.next
        reversed_second_half = reversed_second_half.next

    return True

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
result = is_palindrome(linked_list)
print(result)  # Output: True











