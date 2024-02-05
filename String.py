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




## 35. Length of SubString  Without repeating Characters ##
# Time Complexity is O(2n) , Space Complexity is O(n) #
# TC is 2n bcoz takimg extra time after traversing right pointer , left will also get started with 0 indx 
# Must be Improved by storing the its left pointer corresponding indices and updating its indices , directly jump the left pointer to the corresponds indices ..this will reduces time ... 
class Solution(object):
    def longestSubstr(self , s):
        charSet = set()
        maxlen = 0
        left = 0
        for right in range(len(s)):
            while s[right] in charSet :
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxlen = max(maxlen , right - left + 1) 
        return maxlen       
solutions = Solution()
strs = "abcbdabab"
result = solutions.longestSubstr(strs)
print("longestSubstring is " , result )


## 36. Jewels And  Stones ##
# Time Complexity is O(n+m) , Space Complexity is O(n) #
class Solution(object):
    def jewelStones(self , jewels , stones):
        jewelSet = set(jewels)
        count = 0
        for s in stones:
            if s in jewelSet :
                count += 1
        return count        
solutions = Solution()
jewelStone = solutions.jewelStones("aAB" , "aAAbBcA")    
print("Number of jewels in stones" , jewelStone)  
       

## 37. Valid Anagram (In rearranging Order )   ##
# Time Complexity is O() , Space Complexity is O() #
from collections import Counter
class Solution(object):
    def validAnagram(self , str1 , str2):
        str1_cnt = Counter(str1)
        str2_cnt = Counter(str2)
        if str1_cnt == str2_cnt :
            return True 
        return False    
solutions = Solution()
result = solutions.validAnagram("anagram" , "nagaram")   
print("Valid Anagram ? " , result  )     



## 38. 