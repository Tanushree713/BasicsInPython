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


#----------$$$---------------#

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

# n = 1000
# result = fib_Tab(n)
# print(result )




##------------------------------------------------------##
                             
## Extra Questions ##               ## Extra Questions ##

##------------------------------------------------------##    



##1. Isomorphic Strings ##
# Tc is O(n) , Sc is O(n)  #
def isIsomorphicStr(s , t):
    if len(s) != len(t):
        return False 
    map_s_to_t = {}
    map_t_to_s = {}
    for char_s , char_t in zip(s , t):  #simultaneous move in both str
       map_s_to_t.setdefault(char_s , char_t)  #returns the value associated with the key
       map_t_to_s.setdefault(char_t , char_s)

       if map_s_to_t[char_s] != char_t or  map_t_to_s[char_t] != char_s :
        return False
    return True 

s2, t2 = "foo", "baa"
print(isIsomorphicStr(s2, t2))  # Output: False

