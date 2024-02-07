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





## 38. Reverse Vowels In String ##
# Time Complexity O(n) , Space Complexity is O(n) #
class Solution(object):
    def reverseVowels(self , s):
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        s =list(s)  #list are mutable , we are mutating the string values 
        while left < right :
            while left < right and s[left] not in vowels :
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
solutions = Solution()
result = solutions.reverseVowels("leetcode")
print("reverse vowels in string" , result)                     




## 39. Valid Palindrome ##
# Only AphaNumeric (A to Z , a to z , 0 to 9 ) are Allowed , if any non-alphaNum( , : !) are present then remove them and convert all char into lowerCase #
# Time Complexity is O(n)  , Space Complexity is O(c)  # c= 26 letters
class Solution:
    def validPalindrome(self , s):
        def sanitized_str(s):
            sanitize = ""
            for char in s:
                if char.isalnum():
                    sanitize += char.lower()
            return sanitize
        s = sanitized_str(s)
        left = 0 
        right = len(s) - 1
        while left < right :
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True 
solutions = Solution()
result = solutions.validPalindrome("A man, a plan, a canal: Panama")
print("Valid Palindrome are :", result )                            




## 40. Redistribute Characters To Make All Strings Are Equal ##
# Time Complexity is O(n*m) , Space Complexity is O(c) #
class Solution:
    def makeEqualString(self , words):
        n = len(words)
        charCount = Counter()
        for w in words :
            charCount.update(w)
        for count in charCount.values():
            if count % n != 0 :
                return False
        return True
redistributor = Solution()
results = redistributor.makeEqualString(["abc","aabc","bc"])
print("redistribute Char To make String Equal" , results)                



