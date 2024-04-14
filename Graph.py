##--------------------------------------------------GRAPH-------------------------------------------##
# It has Two Traversal Algorithm #
# 1. DFT           2. BFT

#-----------Depth First Traversal Algo ----------------------#
# Tc is O(V+E) , Sc is O(V+E) #
# 5 --> 3, 7 $ 3-->2, 4 $ 7-->8 $ 4-->8 
def depthFirstTraverse(visited , graph , node):
    if node is not  visited:
        print(node , end=' ')
        visited.add(node)
        for adjacentNodes in graph[node]:
            if adjacentNodes not in visited:
                depthFirstTraverse(visited, graph , adjacentNodes)



visited = set()
graph = {
  '5' : ['3', '7'] , 
  '3' : ['2' , '4'] ,
  '7' : ['8'] ,
  '2' : [] ,
  '4' : ['8'] ,
  '8' : [] ,
}    
depthFirstTraverse(visited , graph , '5')


#-----------------------BreadthFirst Traversal Algo ----------------------#
# Tc is O(V+E) , Sc is O(V+E) #
# A-->B, C , D $ B--> E $ C--> E , F $ D-->F , E-->G $ F--> G $ G--> []
from collections import deque
queue = deque()
def breadthFirstTraverse(visited , graph , node):
    visited.add(node)
    queue.appendleft(node)
    while queue:
        node = queue.pop()
        print(node , end=" ")
        for adjacentNodes in graph[node]:
            if adjacentNodes not in visited :
                visited.add(adjacentNodes)
                queue.appendleft(adjacentNodes)

    

visited = set()
graph ={
    'A' : ['B' , 'C' , 'D'] ,
    'B' : ['E'] ,
    'C' : ['E' , 'F'] ,
    'D' : ['F'],
    'E' : ['G'],
    'F' : ['G'] ,
    'G' : []
}   
print()
print() 
breadthFirstTraverse(visited, graph , 'A')




##---------------------------------------------------------##
##-----Fractional KnapSack -----------------##
class Item:
    def __init__(self , profit , weight):
        self.weight = weight
        self.profit = profit

def fractionalKnapsack(arr , M):
    arr.sort(key = lambda x : (x.profit /x.weight) , reverse = True)  #sort in descending on profit/weight
    maxProfit = 0.0
    for item in arr :
        print(item.profit , item.weight , item.profit//item.weight)
    for item in arr :   #decrementing the capacity and incrementing profit values
        if item.weight <= M:
            M-= item.weight
            maxProfit+= item.profit 
        else:
            maxProfit += item.profit * M /item.weight   
            break
    return maxProfit      

M = 37 
arr = [Item(25 , 5) , Item(75 , 10) , Item(100 , 12) , Item(50 , 4) , Item(45 , 7) ]
maxProfit = fractionalKnapsack(arr , M)
print("Maximum Profit " , maxProfit )