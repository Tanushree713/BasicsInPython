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



## 63. Implement Stack to Queue ##
# Time Complexity is O() , Space Complexity is O()
class MyStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        se;f.front = 0 

    def push(self , x) :
        if self.stack1:
            self.stack1.append(x)
        else:    
            self.front = x   
    
    def pop(self):
        if not self.stack2 :
            while self.stack1 :
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()        

    def  peek(self):
        if self.stack2 :
            return self.stack2.peek()
        return self.front    


    def empty(self):
        return not self.stack1 and not self.stack2 


