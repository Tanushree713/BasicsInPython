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