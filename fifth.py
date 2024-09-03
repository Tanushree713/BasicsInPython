## BUBBLESORT Array ##
## Time complexity is O(n^2) ##

arr = [ 87 , 20 , 50 , 70 , 5, 15 , 90]
n = len(arr)

def bubbleSortAlgo(arr) :
    for i in range(n):
        # No Need To update last element(already get sorted in 1st pass) again nad again use Logic # 
        for j in range(n-i-1):
         if arr[j] > arr[j+1]:
            #Swaps the elements #
            arr[j], arr[j+1] = arr[j+1] , arr[j]
    return arr 

result  = bubbleSortAlgo(arr)
# print(result)


def exchangeFirstToSecondCharandReverse(string,  firstChar , secondChar):
    if not string :
        return []
    s = list(string)
    for i in range(len(s)):
        if s[i] == firstChar:
            s[i] = secondChar
        elif s[i] == secondChar:
            s[i] = firstChar 
    return ''.join(s)           
string = "codebashers"
firstChar = "c"
secondChar = "b"
result = exchangeFirstToSecondCharandReverse(string , firstChar, secondChar)
print(result )
