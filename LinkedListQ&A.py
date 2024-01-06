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


## 






