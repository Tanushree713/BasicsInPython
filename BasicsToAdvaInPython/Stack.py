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


## 62. 