#2D find greater route moving only top to bottom or left to right #
def _2DMatrix(arr):
    top = 0 
    left = 0 
    bottom = len(arr)-1 
    right = len(arr[0])-1
    result = arr[top][left]
    while top < bottom or left < right :
        if top < bottom and left < right :
           if arr[top+1][left] > arr[top][left+1]:
              top += 1  #down movement 
           else:
              left += 1   #right movement
        elif top < bottom :
            top += 1
        else:
            left += 1
        result += arr[top][left]
    return result           

matrix = [[1 , 2, 3 , 4], [14 , 15, 16 , 17],[7 , 8, 3 , 22],[9 , 10 , 1 , 19]]
# result = _2DMatrix(matrix)
# print("Maximum Values with top bottom or left right Route" , result )


#---Taking 2D Matrix Input---#
# rows , columns = map(int , (input("Enter rows and columns: ").split()))
# matrix = []
# for i in range(rows):
#     rows = []
#     for j in range(columns):
#         element = int(input())
#         rows.append(element)
#     matrix.append(rows)
# print("Matrix is Formed") 
# print()   
# for row in matrix :
#     print(row)


#---Taking 2D Matrix Input ----#
# rows , columns = map(int , (input("Enter rows and columns: ").split()))
# matrix = []
# for i in range(rows):
#     row = list(map(int , input("Enter elements  ").split()))
#     matrix.append(row)
# print("Matrix is Formed") 
# print()   
# for row in matrix :
#     print(row)
 
def flipStr(pwd):
    result = []
    count = 0 
    for char in pwd :
        if char == "0":
            result.append("1")
            count += 1
        else:
            result.append("0")
    return  count           

pwd = "01011001"
# print(flipStr(pwd) )   

def flipZeroes(arr , k):
    n = len(arr)
    maxlen = 0
    for i in range(n):
        cnt = 0 
        for j in range(i , n ):
            if arr[j] == 0 :
                cnt += 1
            if cnt <= k:
                    maxlen = max(maxlen , j-i+1)
            else:
                    break
        return maxlen        
    
            
    
arr = [1,1,1,1,0,1,0,1,0,0,0,1,1]   # 8
k = 2
res = flipZeroes(arr , k)
print(res)