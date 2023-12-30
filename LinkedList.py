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
# Time Complexity is O(1) , Space Complexity is O(1)

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
    def insertionAtEnd(self , new_data):    #{TC = O(n) ,SC = O(1)}
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node 
            return
        temp = self.head     
        while temp.next != None :
            temp = temp.next
        temp.next = new_node    


  # function definition for insertion at any node
    def insertionAtAnyNode(self , prev_node , new_data):  #{TC = O(1) ,SC = O(1)}
        new_node = Node(new_data)
        if prev_node is None :
            print("given node is available at Likedlist")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
    # function definition for printing LinkedList
    
    def printLists(self):        #{TC = O(n) ,SC = O(1)}
        temp = self.head
        while temp :
            print(str(temp.data) + " " , end=" ")
            temp = temp.next            
   
# llists = LinkedList()
# llists.insertionAtEnd(12)
# llists.insertionAtEnd(13)
# llists.insertionAtEnd(15)
# llists.insertionAtAnyNode(llists.head.next.next , 16)
# llists.printLists()


## Deletion Of Any Node 
# Time Complexity is O(n) , Space Complexity is O(1)
# Class constructor for Node
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertionAtFront(self , new_data) :
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else :    
          temp = self.head
          new_node.next = self.head 
          self.head = new_node

    def deletionAtAnyNode(self , pos):
       
        # Base Case Condition 
        if self.head is None : #empty LinkedList
            return
        temp = self.head 
        # if pos == 0:
        #    self.head = temp.next
        #    temp = None
        #    return
        for i in range(pos -1 ):
            temp = temp.next 
            # if temp is None : # pointer points out of bound 
            #     return 
            # if temp.next is None:
            #     return    
        new_ptr = temp.next.next # creating new ptr starts pointing nextValue of curr node to nextValue of just after currnode  
       # store nextValue of just after currnode by making none its value firstly 
        temp.next = new_ptr

    def printLinkedList(self):
        temp = self.head
        while temp :
            print(str(temp.data) + " " , end =" ")
            temp = temp.next

# linkedList = LinkedList()
# linkedList.insertionAtFront(21)
# linkedList.insertionAtFront(22)
# linkedList.insertionAtFront(23)
# linkedList.insertionAtFront(25)
# linkedList.deletionAtAnyNode(2)
# linkedList.printLinkedList()            




## Searching Element In an LinkedList ##
# Only Linear Search Is Possible #
# Time Complexity is O(n) , Space Complexity is O(1)

# class constructor for Node
class Node:
    def __init__(self , data):
        self.next = None
        self.data = data

# class constructor for LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion At End #
    def insertionAtEnd(self , new_data):
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_node
            return 
        else:
            temp  =  self.head 
            while temp.next :
                temp = temp.next 
            temp.next = new_node
    # Search At Any Node (Using Linear Search)
    def searchData(self , key):
        temp = self.head
        while temp :
            if temp.data == key :
                return True 
            else: 
               temp = temp.next 
        return False 


    def printInsertedList(self):
        temp = self.head 
        while temp :
            print(str(temp.data) + " " , end =" ")
            temp = temp.next

# llist = LinkedList()
# llist.insertionAtEnd(32)
# llist.insertionAtEnd(33)
# llist.insertionAtEnd(35)
# llist.insertionAtEnd(38)
# llist.insertionAtEnd(13)
# llist.printInsertedList()
# print()
# key = 30
# result = llist.searchData(key)
# if result :
#     print("Data is Found ")
# else:
#     print("Data is Not Found")    





## Reversal Of LinkedList ##
###########
## Count Number of Nodes  ##
###########
# Time complexity is O(n) , Space Complexity is O(1)
# class Constructor For Node
class Node:
    def __init__(self , data):
        self.next = None
        self.data = data
# class Constructor For LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  
# definition function for insertion at front         
    def insertAtBegin(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
# definition For Reversal LinkedList
    def reverseLinkedList(self):
        curr = self.head
        prev = None
        next_ptr = None
        while curr :
            next_ptr = curr.next 
            curr.next = prev 
            prev = curr
            curr = next_ptr
        # Need To add Condition For Linkage of Last Node with head node
        self.head = prev

# definition function For Count The Nodes In LinkedList
    def countNodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

# defintion for Printing List        
    def  printOut(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " " , end =" ")
            temp = temp.next 


# likedList = LinkedList()
# likedList.insertAtBegin(1)
# likedList.insertAtBegin(2)
# likedList.insertAtBegin(3)
# likedList.insertAtBegin(4)
# likedList.insertAtBegin(5)
# print("Original LinkedList")
# likedList.printOut()
# likedList.reverseLinkedList()
# print()
# print("Reversed LinkedList are :")
# likedList.printOut()
# print()
# count = likedList.countNodes()
# print("Count Nodes In linkedList :" , count)





## Floyd's Cycle Algorithm ##
# Also called Tortoise and hare , Slow and fast ptr Algo
# Time Complexity is O(n) , Space Complexity is O(1)
# class Constructor For Node
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
# class constructor For LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # definition For Insertion At Starting
    def insertionAtStart(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node

    # definition For Floyd's Algo
    def detectedLoopInLinkedList(self):
        tortoise = self.head  # move one steps
        hare = self.head # move two steps 
        while hare and tortoise and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False

     # definition For printing 
    def printingListLinked(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end =" " )
            temp = temp.next   

lnkedList = LinkedList()
lnkedList.insertionAtStart(7)     
lnkedList.insertionAtStart(6)
lnkedList.insertionAtStart(5)
lnkedList.insertionAtStart(4)
lnkedList.insertionAtStart(3)
lnkedList.printingListLinked()
print()
lnkedList.head.next.next.next.next = lnkedList.head
if lnkedList.detectedLoopInLinkedList():
    print("Detected Loop Found In LinkedList") 
else:
    print("Not Found")                    













## SKip List , Concepts Based on modified Binary-Search Used In LinkedList For searching Any Node










          