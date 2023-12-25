## Insertion At Front ##
## Time Complexity is O(1) , Space complexity is O(1)

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
# llist  = LinkedList()
# llist.insertAtBeginning(12)
# llist.insertAtBeginning(10)
# llist.insertAtBeginning(8)          
# llist.printList()  


## Insertion At End  ##
# Traversing loop here
# Time Complexity is O(n) , Space Complexity is O(1)

# Class Constructor For Node
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

# Class Constructor For LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

# Function Def for Insertion at End 
    def insertionAtEnd(self , new_data):   
        new_node = Node(new_data)
      # if no elements then put new node value inside it
        if self.head is None :
           self.head = new_node
           return
        else:
          temp = self.head
          while temp.next : #traversing till not getting None next value in node
             temp = temp.next
          temp.next = new_node #insert new_node value in next value in node

# printing Node
    def printListing(self):
        temp = self.head
        while temp :
            print(str(temp.data) + " " ,end = " ")     
            temp = temp.next 

# lilist = LinkedList()
# lilist.insertionAtEnd(12)
# lilist.insertionAtEnd(9)
# lilist.insertionAtEnd(7)
# lilist.printListing()



## Insertion After Any Node ##
# Time Complexity is O() , Space Complexity is O()

# Class Constructor for Node
class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
# Class constructor for LinkedList 
class LinkedList :
    def __init__(self):
        self.head = None
  # function definition for insertion at end 
    def insertionAtEnd(self , new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node 
            return
        temp = self.head     
        while temp.next != None :
            temp = temp.next
        temp.next = new_node    


  # function definition for insertion at any node
    def insertionAtAnyNode(self , prev_node , new_data):
        new_node = Node(new_data)
        if prev_node is None :
            print("given node is available at Likedlist")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
    # function definition for printing LinkedList
    
    def printLists(self):
        temp = self.head
        while temp :
            print(str(temp.data) + " " , end=" ")
            temp = temp.next            
   
llists = LinkedList()
llists.insertionAtEnd(12)
llists.insertionAtEnd(13)
llists.insertionAtEnd(15)
llists.insertionAtAnyNode(llists.head.next.next , 16)
llists.printLists()





          