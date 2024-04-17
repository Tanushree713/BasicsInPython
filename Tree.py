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
# print("Inorder Traversal :")  
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
# print("Preorder Traversal :")  
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
# print("Postorder Traversal :") 
# root.postOrder()



##----------------------------Interview Q/A----------------------------------------##
## Building Tree >> TC is O(n^2)  , SC is O(n)  ##

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def buildTree(inorder, postorder):
#     if not inorder or not postorder:
#         return None
    
#     root_val = postorder.pop()
#     root = TreeNode(root_val)
#     root_index = inorder.index(root_val)
    
#     root.right = buildTree(inorder[root_index+1:], postorder)
#     root.left = buildTree(inorder[:root_index], postorder)
    
#     return root

# def inorderTraversal(root):
#     if root is None:
#         return []
#     return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# def postorderTraversal(root):
#     if root is None:
#         return []
#     return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

# def printTree(root, level=0, prefix='Root:'):
#     if root:
#         print(' ' * (level * 4) + prefix, root.val)
#         printTree(root.left, level + 1, prefix='L--:')
#         printTree(root.right, level + 1, prefix='R--:')

# # Example usage:
# inorder = [4, 2, 5, 1, 6, 3, 7]
# postorder = [4, 5, 2, 6, 7, 3, 1]
# root = buildTree(inorder, postorder)

# print("Inorder traversal:", inorderTraversal(root))
# print("Postorder traversal:", postorderTraversal(root))

# print("\nTree Structure:")
# printTree(root)






##------------BST-----------------------##


# 1. Insertion and Inorder BST  And Maximum And Minimum BST and  BST Searching #
# Time complexity is O(n) , Space Complexity is O(n)  ---> Worst Case #
# TC is O(logn) , Space Complexity is O(logn) --> Best or Average Case #
class Node  :
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
# For insertion BST #
#  TC is O( n ) , SC is O(1 ) #  
def insertionBST(root , key):
    if root is None:
        return Node(key)
    else:
        if root.data == key :
            return root
        elif root.data < key :
            root.right = insertionBST(root.right , key )      
        else:
            root.left = insertionBST(root.left , key )    
    return root 

# For Finding Min In BST #
# TC is O(logn or n ) , SC is O(1) #    
def  findMin(root):
    curr = root
    while curr.left :
        curr = curr.left
    return curr.data  

# For Finding Max In BST #
# TC is O(logn or n ) , SC is O(1) #
def  findMax(root):
    curr = root
    while curr.right :
        curr = curr.right
    return curr.data

# For Search key  In BST #
# TC is O((n) --> UnBalanced  , (logn) --> Balanced) , SC is O(1)#
def searchBST(root , key ):
    if root is None or root.data == key :
        return root 
    elif root.data > key :
        return searchBST(root.left , key )
    else:
        return searchBST(root.right , key )     

# For Inorder BST #
#  TC is O( n ) , SC is O(n ) #  
def inorderBST(root):
    if root :
        if root.left :
            inorderBST(root.left)
        print(str(root.data) + " " , end="")
        if root.right :
            inorderBST(root.right)  


root = Node(100)
root = insertionBST(root , 80)
root = insertionBST(root , 110)
root = insertionBST(root , 50)
root = insertionBST(root , 90)
# print("Inorder Traversal" )
# inorderBST(root)
print()
# print("Minimum Value In BST " , findMin(root)) 
# print("Maximum Value In BST " , findMax(root))
# key = 100  
# result = searchBST(root , key )   
# if result : 
#     print("Searching Key Is Present In BST" )
# else:
#     print("Not present In BST ")      




# 2. Find Num Of UniqueBST #
# TC is O(n^2) , SC is O(1) #
def findUniqueBST(n) :
    n1 , n2 , sum_Val = 0 , 0 , 0 
    if n == 0 or n == 1:
        return 1
    else :
        for i in range(1 , n+1):
            n1 = findUniqueBST(i - 1)    #c0
            n2 = findUniqueBST(n - i)   #cn
            sum_Val += n1*n2             #catalan Series 
        return sum_Val
n = 3        
# result = findUniqueBST(n)            
# print("Number Of Unique BST " , result )





# 3. Deletion IN BST #
# TC is O(n) , SC is O(n) --> In worst case  #
class Node :
    def __init__(self , data ) :
        self.data = data
        self.left = None 
        self.right = None 

def insertionInBST(root , key):
    if root is None:
        return Node(key)
    else:
        if root.data == key :
            return root
        elif root.data < key :
            root.right = insertionBST(root.right , key )      
        else:
            root.left = insertionBST(root.left , key )    
    return root 

def minValInBST(root):
    curr = root 
    while curr.left:
        curr= curr.left
    return curr.data 

def deleteNode(root , key ):

        if root is None :
            return root
        if key < root.data :
            root.left = deleteNode(root.left , key )
        elif key > root.data :
            root.right = deleteNode(root.right , key )   
        else:
            if root.left is None :
                temp = root.right
                root = None 
                return temp
            elif root.right is None :
                temp = root.left 
                root = None
                return temp 
            temp = minValInBST(root.right)
            root.data = temp
            print("Min Value " , temp )
            root.right = deleteNode(root.right, temp )
        return root 

def inorderInBST(root):
    if root :
        if root.left :
            inorderInBST(root.left)
        print(str(root.data) + " " , end = "")
        if root.right :
            inorderInBST(root.right)

# insertion of node 
root = Node(100)
root = insertionInBST(root , 80)
root = insertionInBST(root , 110)
root = insertionInBST(root , 50)
root = insertionInBST(root , 70)
root = insertionInBST(root , 20)
root = insertionInBST(root , 145)
root = insertionInBST(root , 120)

# Inorder BST 
print("Inorder Traversal" )
inorderInBST(root)

# deleteNode In BST #

# deleteNode has no child 
print()
deleteNode(root , 20 )
print("Inorder traversal modified tree")
inorderInBST(root)

# deleteNode has 1 child
print() 
deleteNode(root , 120)
print("Inorder traversal modified tree")
inorderInBST(root)

# deleteNode has 2 child 
print()
deleteNode(root , 100)
print("Inorder traversal modified tree")
inorderInBST(root)





# 4. Max Sum No Adjacent Node #
# Approach 1>> Inc & Exc Method #
# Tc is O(n) , Sc is O(1) #
def maxSumNoAdjacent1(arr):
    if arr is None :
        return 0
    elif len(arr) == 1:
        return arr 
    else:
        inc = arr[0]
        exc = 0 
        for i in range(1 , len(arr)):
            new_exc = max(inc , exc)
            inc = exc + arr[i]   
            exc = new_exc
        return max(inc , exc )   
arr = [3, 2, 7, 20 ]
result = maxSumNoAdjacent1(arr)
print()
print("MaxSum No Adjacent " , result )




#Approach 2 >> BST 
# Tc is O(n) , Sc is O(n) #
class Node :
    def __init__(self , val):
        self.val = val 
        self.left = None 
        self.right = None 
        
def maxSumNoAdjacent2(root):   
    if root is None :
        return 0 , 0
        
    left_inc , left_exc = maxSumNoAdjacent2(root.left)  
    right_inc , right_exc = maxSumNoAdjacent2(root.right)
    inc_sum = root.val + left_exc + right_exc
    exc_sum = max(left_inc , left_exc ) + max(right_inc , right_exc)
    return inc_sum , exc_sum 
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7) 
max_incSum, max_excSum = maxSumNoAdjacent2(root)    
print("Maximum Sum No Adjacent Root Node  ",max(max_incSum , max_excSum ))    


# 5. Construct BST From PreOrder Traversal #
# TC is O(n) , Sc is O(n) #
INT_MIN = -float('inf')
INT_MAX = float('inf')

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def buildBST(preorder, preIndex, key, min_val, max_val, size):
    if preIndex[0] >= size:
        return None
    
    root = None
    
    if key > min_val and key < max_val:
        root = Node(key)
        preIndex[0] += 1
        
        if preIndex[0] < size:
            root.left = buildBST(preorder, preIndex, preorder[preIndex[0]], min_val, key, size)
            root.right = buildBST(preorder, preIndex, preorder[preIndex[0]], key, max_val, size)
    
    return root 

def bstFromPreorder(preorder):
    size = len(preorder)
    preIndex = [0]
    return buildBST(preorder, preIndex, preorder[0], INT_MIN, INT_MAX, size)

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Example usage:
preorder = [8, 5, 1, 7, 10, 12]
root = bstFromPreorder(preorder)
print("Preorder Traversal of Constructed BST:")
preorder_traversal(root)




# 6. PreOrder To PostOrder #
# Tc is O(nlogn) , Sc is O(n)  #

class Node:
    def __init__(self , val):
        self.left = None
        self.right = None 
        self.val = val 

def buildBST(start , end , preorder):
    if start > end :
        return None 
    root = Node(preorder[start])    
    mid = start 
    while mid <= end and preorder[mid] <= preorder[start]:
        mid += 1
    root.left = buildBST(start + 1 , mid - 1, preorder)
    root.right = buildBST(mid , end , preorder)    
    return root

def postOrderTraversal(root):
    if root is None :
        return []
    return postOrderTraversal(root.left) + postOrderTraversal(root.right) + [root.val]  

def constructPostOrder(arr):
    root = buildBST(0 , len(arr) - 1 , arr)
    return postOrderTraversal(root)

arr1 = [8 , 7 , 1, 10 , 6]
print()
print("Input:", arr1)
print("Output:", constructPostOrder(arr1))    