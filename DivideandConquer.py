## 1st Application >> Find Min and Max in an array ##
# Time Complexity is O(n) , Space Complexity is O(1)
def findMaxandMin(arr , i , j):
    # Small Problem #
    # having single element pushing that element in both value
    if i == j :
        max_value = arr[i]
        min_value = arr[i]
    # having 2 elements do one comparison     
    elif i == j -1 : 
        if arr[i] < arr[j]:
          max_value = arr[j]
          min_value = arr[i]
        else:
            max_value = arr[i]
            min_value = arr[j]
    # Big problem #        
    # Divide
    else: 
        mid = i + (j-i)//2
    # recursion -> conquer 
        max_l , min_l  = findMaxandMin(arr , i , mid)
        max_r , min_r  = findMaxandMin(arr , mid+1 , j)   

    # combine
        max_value  = max(max_l , max_r)
        min_value  = min(min_l , min_r)

    return max_value , min_value

arr = [ -2 , 100 , 76 , 436 , 89 , -33 , 0  ]
i = 0
j = len(arr) - 1
max_value , min_value = findMaxandMin(arr , i , j)
print("Mx and Min" , max_value  , min_value)
