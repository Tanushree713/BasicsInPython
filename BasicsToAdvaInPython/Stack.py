## 60. Valid Parenthesis  ##
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

