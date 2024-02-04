## 30. Reverse string ##
# Time Complexity is O(n) , Space Complexity is O(1) #
def reversedString(s):
    left = 0
    right = len(s) - 1
    while left <= right :
        s[left],s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s     
string = ["h","e","l","l","o"]
result = reversedString(string)
print("Reversed string is ",result)




## 31. First Unique Characters In String ##
# Time Complexity is O(n) , Space Complexity is O(n)  #
from collections import Counter 
def firstUniqueChar(string):
    counts = Counter(string)
    for index,char in enumerate(string):
        if counts[char] == 1:
            return index
    return -1
string = "aabb"    
uniqueCharIndex = firstUniqueChar(string) 
print("firstUnique Char Index" , uniqueCharIndex)      




## 32. Reversed Words Of String ##
# Time Complexity is O(n) , Space complexity is O(n) #
def reversalOfWords(s):
    words = s.split() #getting words
    reversedWords = words[::-1] # reversing Words using Splicing 
    reversedString = ' '.join(reversedWords) # Join the words 
    return reversedString
string = "the Sky is blue"
reversalOfWords = reversalOfWords(string)   
print('reversed words are :' , reversalOfWords)




## 33. Length Of Last Words ##
# Time Complexity is O(n) , Space Complexity is O(n)#
class Solution(object):
    def lengthLastWords(self , s):
        words = s.split()
        lastWords = words[-1]
        lengthLastWords = len(lastWords)
        return lengthLastWords
solution = Solution()        
string = "hello Motto"
result = solution.lengthLastWords(string)
print("lastWords Length" , result)        



## 34. Common Prefix Length ##
# Time Complexity is O(n * m ) , Space complexity is O(k) #  where k is len(commonPrefix)
class Solution(object):
    def commonPrefixLen(self , s):
        if not s :
            return ""
        s.sort()  
        first_Str = s[0]
        last_Str = s[-1]  
        commonPrf = []
        for i in range(len(first_Str)):
            if i < len(last_Str) and first_Str[i] == last_Str[i] :
                commonPrf.append(first_Str[i])
            else:
                break
        return ''.join(commonPrf)      
solutions = Solution()
strs = ["Flow" , "Flower" , "Floral"   ]
resultant = solutions.commonPrefixLen(strs) 
print("Common Prefix in Words" , resultant)




## 35. Length of SubString ##

       
        