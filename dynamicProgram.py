## OverCome Overlapping SubProblems ##
## Memoization OR  Top_Down Approach ##
# Tc is O(n) , Sc is O(n)
# Increases Depth Of tree for complex Num # 
def fib_Num(n , memo):
    result = []
    if memo[n]:
        return memo[n] 
    if n == 1 or n == 2 :
        result = 1
    else :   
        result = fib_Num(n-1 , memo) + fib_Num(n-2 , memo)
    memo[n] = result 
    return result       
def fib_memo(n):
    memo = [None] * (n+1)
    return fib_Num(n , memo)


# n = 100
# result = fib_memo(n)
# print(result )


#----------$$$---------------#

## OverCome the Depth of Tree ##
## Tabulation OR Bottom-Up Approach ##
# Tc is O(n) , Sc is O(n)
def fib_Tab(n):
    if n == 1 or n == 2:
        return 1
    bottom = [None] * (n+1)    
    bottom[1] = 1
    bottom[2] = 1
    for i in range(3 , n+1):
        bottom[i] = bottom[i-1] + bottom[i-2]
    return bottom[n]    

# n = 1000
# result = fib_Tab(n)
# print(result )




##------------------------------------------------------##
                             
## Extra Questions ##               ## Extra Questions ##

##------------------------------------------------------##    



##1. Isomorphic Strings ##
# Tc is O(n) , Sc is O(n)  #
def isIsomorphicStr(s , t):
    if len(s) != len(t):
        return False 
    map_s_to_t = {}
    map_t_to_s = {}
    for char_s , char_t in zip(s , t):  #simultaneous move in both str
       map_s_to_t.setdefault(char_s , char_t)  #returns the value associated with the key
       map_t_to_s.setdefault(char_t , char_s)

       if map_s_to_t[char_s] != char_t or  map_t_to_s[char_t] != char_s :
        return False
    return True 

s2, t2 = "foo", "baa"
print(isIsomorphicStr(s2, t2))  # Output: False



##2. ADD TWO Number In LL ##
# Tc is O(n) , Sc is O(1) #
class ListNode:
    def __init__(self , val):
        self.next = None 
        self.val = val 

    def addTwoNumInLL(self,  l1 , l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0 
        while l1 or l2 or carry :
            sum = carry 
            if l1 :
                sum += l1.val
                l1 =l1.next
            if l2 :
                sum += l2.val 
                l2 = l2.next 
            carry = sum // 10 
            temp.next = ListNode(sum % 10)
            temp = temp.next 

        return dummy.next 
    
    def printLL(self):
        temp = self 
        while temp:
            print(str(temp.val)+ " " , end="")
            temp = temp.next 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next= ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = ListNode(0).addTwoNumInLL(l1 , l2)
result.printLL()
print()

##3. ODD EVEN LinkedList ##
# Tc is O(n) , Sc is O(1) #

class Node:
  def __init__(self , val):
    self.next = None
    self.val = val

def oddEvenLL(head):
    if head is None or head.next is None:
        return head
    
    odd = head
    even = head.next
    evenHead = head.next 
    
    while even and even.next:
        odd.next = odd.next.next  
        odd = odd.next 
        even.next = even.next.next 
        even = even.next  
        
    odd.next = evenHead  
    return head


def printList(head):
    temp = head 
    print("ODD EVEN IN LL")
    while temp:
        print(str(temp.val)+ " " , end="")
        temp = temp.next 

listNode = Node(1)
listNode.next = Node(2)
listNode.next.next = Node(3)
listNode.next.next.next = Node(4)
listNode.next.next.next.next = Node(5)
listNode.next.next.next.next.next = Node(6)

result = oddEvenLL(listNode)
printList(result)





