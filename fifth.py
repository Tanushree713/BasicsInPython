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

##VennDiagramProblem##
# Tc is O(1) , Sc is O(1) #
def vennDiagram(p1, p2, p3, q, r, e):
    res_abcExactly = e - (p1+p2+p3 - 2*q + r)   # (e = 3x + p1-q + p2-q + p3-q + q + r)
    One_a = int((res_abcExactly / 3)) + (p1-q + p3-q + q) #CompleteCircleA
    return res_abcExactly , One_a

p1 = 30#(A intersects B)
p2 = 26 #(B intersects C)
p3 = 28#(A intersects C)
q = 14#(A , B , C intersects)
r = 43#(Not Inside)
e = 345#(Total)
result = vennDiagram(p1,p2,p3,q,r,e) #(1.Exactly One of them (only A + only B + Only C)    2. A (One))
print(f"{result[0]} {result[1]}")