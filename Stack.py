## 60. Valid Parenthesis  ##
# Time Complexity is O(n) , Space complexity is O(n)
def validparenthesis(string):

   stack = []
   open_params = set(["(" , "{" , "[" ])
   dictionary = { "{" : "}" ,
                 "[":"]" , 
                 "(" : ")"  }
   for char in string :
     # stack store the open paranthesis
    if char in open_params :
        stack.append(char)
     # start Empty stack one by one if there exist close parenthesis     
    elif stack and char == dictionary[stack[-1]]:
        stack.pop()
    else:  
        return False
   return stack == []                            
# Driver
string1 = "{[(})]}"
if validparenthesis(string1):
    print("valid String")
else:
    print("Invalid String")    



## 61. Make a great String ##
# Time Complexity is O(n) , Space complexity is O(n)
class Solution:
  def makeGreatStr(self, s):
    stack = []
    if not s :
        return ""

    for char in s :
        if stack and abs(ord(char) - ord(stack[-1])) == 32 :
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)        




strings = "leeEetcode" 
solution = Solution() 
resultant = solution.makeGreatStr(strings)  
print("Make Great str" , resultant)


## 62. Remove Duplicates In String ##
# Time  Complexity is o(n) , Space Complexity is O(n)
class Solution(object):

 def removeDuplicates(self, string):
    stack = []
    if not string :
        return ''
    for char in string :
        if stack and char == stack[-1] :
            stack.pop()
        else:
            stack.append(char)  
    return ''.join(stack)   
stringas = 'aaassthaa'  
solution = Solution()
result = solution.removeDuplicates(stringas)
print("Remove the str" , result )         



## 63. Implement Queue using Stack  ##
# Time Complexity is O(n) , Space Complexity is O(n)
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        se;f.front = 0 
    # Time Complexity is O(1) , Space Complexity is O(n)
    def push(self , x) :
        if self.stack1:
            self.stack1.append(x)
        else:    
            self.front = x   
    # Time Complexity is O(n) , Space Complexity is O(2n)
    def pop(self):
        if not self.stack2 :
            while self.stack1 :
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()        
    # Time Complexity is O(1) , Space Complexity is O(n)
    def  peek(self):
        if self.stack2 :
            return self.stack2.peek()
        return self.front    

    # Time Complexity is O(1) , Space Complexity is O(n)
    def empty(self):
        return not self.stack1 and not self.stack2 




## 64. Implement stack using Queue
# Time Complexity is O(n) , Space Complexity is O(n)
class MyStack() :
    def __init__(self):
        self.q = deque
    # Time Complexity is O(n) , Space Complexity is O(n)
    def push(self , x):
        self.q.append(x)
    # Time Complexity is O(1) , Space Complexity is O(n)
    def pop(self):
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())    
        return self.q.popleft()
    # Time Complexity is O(1) , Space Complexity is O(n)
    def top(self):
        return self.q[-1]      
    # Time Complexity is O(1) , Space Complexity is O(n)
    def empty(self ):
        return not self.q       



  ## 65. Online Stock Span ##
  # # Time Complexity is O(n) , Space Complexity is O(n)     
class StockSpanner(objects):
    def __init__(self):
        self.stack = [] # contains pairs of price and span >> [ price , span ]
    
    def next(self, price): # curr price = price here
        span = 1
        while self.stack and self.stack[-1][0] <= price :
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price , span))
        return span      


