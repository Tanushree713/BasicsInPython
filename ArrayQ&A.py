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


## 3. Max Product of SubArray ##
# Time complexity is O(n^2)
# Space Complexity is O(n^2)
## Approach 1 ##
def find_subArray(arr):
    subArrays = []
    n = len(arr)
    for i in range(n):
        subArray = []
        for j in range(i , n):
            subArray.append(arr[j])
            subArrays.append(subArray.copy())
    return subArrays
def productOfSubArray(subarrays):
    products = []
    for subarray in subarrays:
        product = 1
        for element in subarray:
            product *= element
        products.append(product)
    return products

arr = [ 1, 2, 3]
subarrays = find_subArray(arr)
products =  productOfSubArray(subarrays)
subArraysAndProducts = list(zip(subarrays , products))
maxSubArrayProductIs = max(subArraysAndProducts , key = lambda x: x[1])
max_product = maxSubArrayProductIs[1]
print("max product is:" , maxSubArrayProductIs)
print("product of subarray " , max_product)

## Approach2 (OPTIMIZE)##

## 4. 3Sums
# Getting triplets sum is equal to zero return that subarray #
#  Two pointer Approach
# Time Complexity is O(n^2)
# Space Complexity is O(k) where k depneds on number of subarray 

def tripletSum(nums):
    nums.sort() # use sorting so proceed with 2 pointer approach 
    results = []

   #To confirm that we have three element atleast in an array
    for i in range(len(nums)-2):
        # find duplicates
        if i > 0 and nums[i] == nums[i-1]: 
            # skip duplicates 
            continue
        # start implementation of 2 pointer approach
        left , right = i + 1 , len(nums) - 1
        while left < right :
            total  = nums[i] + nums[left] + nums[right]
            if total == 0 :
                results.append([nums[i] , nums[left] , nums[right]])
                # removing duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1
    return results 

nums = [ 1 , 2, -1 , 0 , -2 , 4 , -3]                    
resultants = tripletSum(nums)
print ("triplet whose sum is zero is " , resultants)
















