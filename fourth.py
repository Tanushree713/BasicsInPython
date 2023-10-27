### Search In 2D Matrix ###
# Sorted Array row wise and 
# first element of next row is greater then previous row element
# Time Complexity is O(log(m*n)) 
matrix = [[1, 2, 3, 4] ,[6, 7, 8 , 9] ,[11 , 12, 13, 14]]
target = 13
def searchInSortedArray(matrix , target):
    m = len(matrix)
    n = len(matrix[0]) 
    if m == 0 :
        return False
    left = 0 
    right = m*n-1
    while left<=right :
        mid = left + right - left//2
        mid_element = matrix[mid//n][mid%n]
        if mid_element == target :
            return True
        elif mid_element < target:
            left = mid + 1
        else :
             right = mid - 1
    return False         

result = searchInSortedArray(matrix , target)
print(result)
