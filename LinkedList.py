## Insertion At Front ##
## Time Complexity is O(n)

#Class Constructor for Node
class Node :
  def __init__ (self , data):
    self.data = data
    self.next = None
# Class Constructor for LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
# Insertion in front of LinkedList 
    def insertAtBeginning(self , new_data):
    # creating new node
        new_node = Node(new_data) 
    # Insertion at beginning 
        new_node.next = self.head 
        self.head = new_node
# printing LinkedList
    def printList(self):
        temp = self.head
        while temp :
            print(str(temp.data) + " " , end=" ")  #str to add spaces , end print data in horizontal manner
            temp =  temp.next

# Driver Code 
llist  = LinkedList()
llist.insertAtBeginning(12)
llist.insertAtBeginning(10)
llist.insertAtBeginning(8)          
llist.printList()  


          