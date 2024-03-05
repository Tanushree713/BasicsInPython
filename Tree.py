## ------------------------Introduction of Tree --------------------------- ##

## 1.Inorder Tree Traversal Algo ##
# Time Complexity is O(n) , Space Complexity is O(n) #
class Node :
    def __init__(self , data):
        self.data = data
        self.left = None 
        self.right = None


    def inOrder(self):
        if self:
            # recursive call for left subtree 
            if self.left:
                self.left.inOrder()
            print(str(self.data) + " ", end = "")
            # recursive call for right subtree
            if self.right:
                self.right.inOrder()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder Traversal :")  
# root.inOrder()  


## 2. PreOrder Tree traversal Algo ##
# Time Complexity is O(n) , Space Complexity is O(h) # where , h = height of binary tree
class Node :
    def __init__(self , data):
        self.data = data 
        self.left = None
        self.right = None 
    def preOrder(self):
        if self:
            print(str(self.data) + " " , end = '')
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder Traversal :")  
# root.preOrder()  
                

## 3. PostOrder Tree Traversal Algo ##
# Time complexity is O(n) , Space Complexity is O(n) #
class Node :
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    def postOrder(self):
       if self:
        if self.left :
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(str(self.data) + " " , end = "")  

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Postorder Traversal :") 
root.postOrder()
