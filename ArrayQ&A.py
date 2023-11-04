## 1.Min And Max Element  in given Array ##
# Time Complexity is O(n) 
# Space complexity is O(1)
arr = [11, 23, 12, 13 , 36 , 40 , 9]
def minAndMax(arr):
 arr.sort()
 print(arr)
 minAndmax = { "min": arr[0] , "max": arr[len(arr)-1 ]}
 return minAndmax

resultant = minAndMax(arr)
print("min element is :" , resultant["min"] )
print("max element is :" , resultant["max"] )

## 2. Best Time to Buy and sell the Stock ##
# Time Complexity is O(n)
# Space Complexity is O(1) 
prices = [ 7, 1, 5, 4, 6, 3]
def buysellStock(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit :
            max_profit = prices[i] - min_price    
    return max_profit

result = buysellStock(prices)
print("Max Profit is :" , result )     



