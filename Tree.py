## ------------------------Introduction of Tree --------------------------- ##
# 1.Inorder Tree Traversal Algo #
# Time Complexity is O(n) , Space Complexity is O(n)
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
root.inOrder()  
