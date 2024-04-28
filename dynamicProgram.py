## OverCome Overlapping SubProblems ##
## Memoization OR  Top_Down Approach ##
# Tc is O(n) , Sc is O(n)
# Increases Depth Of tree for complex Num # 
def fib_Num(n , memo):
    result = []
    if memo[n]:
        return memo[n] 
    if n == 1 or n == 2 :
        result = 1
    else :   
        result = fib_Num(n-1 , memo) + fib_Num(n-2 , memo)
    memo[n] = result 
    return result       
def fib_memo(n):
    memo = [None] * (n+1)
    return fib_Num(n , memo)


# n = 100
# result = fib_memo(n)
# print(result )

## OverCome the Depth of Tree ##
## Tabulation OR Bottom-Up Approach ##
# Tc is O(n) , Sc is O(n)
def fib_Tab(n):
    if n == 1 or n == 2:
        return 1
    bottom = [None] * (n+1)    
    bottom[1] = 1
    bottom[2] = 1
    for i in range(3 , n+1):
        bottom[i] = bottom[i-1] + bottom[i-2]
    return bottom[n]    

n = 1000
result = fib_Tab(n)
print(result )