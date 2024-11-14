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
result = _2DMatrix(matrix)
print("Maximum Values with top bottom or left right Route" , result )
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


import math
def encryptStrIn2DMat(string) :
    n = len(string)
    rows = math.ceil(math.sqrt(n))
    cols = math.ceil(n // rows)
    mat = [['']* cols for _ in range(rows)]
    index = 0 
    for i in range(rows):
        for j in range(cols):
            if index < n :
                mat[i][j] = string[index]
                index += 1
            else:
                mat[i][j] = "" 
    print(mat)            
    encryptStr = ""            
    for j in range(cols):
        for i in range(rows):
            if mat[i][j] != '':
                encryptStr += mat[i][j]     
    return encryptStr
input_string = "PLEASESAVEME"
result  = encryptStrIn2DMat(input_string)
print("Encrypted Str", result)
