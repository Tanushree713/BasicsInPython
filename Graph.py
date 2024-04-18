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
##            GREEDY APPLICATION                     ##
##-----Fractional KnapSack -----------------##
# Tc is O(nlogn) , Sc is O(n) #

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




##------Job Sequences-------##
# Tc is O(nlogn) , Sc is O(maxDeadline) #
def jobSequences(arr , maxDeadline):
    n = len(arr)
    arr.sort(key = lambda x:x[1] , reverse=True)
    result = [False] * maxDeadline
    job = [-1] * maxDeadline
    for i in range(n):
        for j in range(min(maxDeadline-1 , arr[i][2]-1) ,  -1 , -1):
            if result[j] is False :
                result[j] = True 
                job[j] = arr[i][0]
                break
    return job         

arr = [
    ['J1', 55, 5],
    ['J2', 65, 2],
    ['J3', 75, 7],
    ['J4', 60, 3],
    ['J5', 70, 2],
    ['J6', 50, 1],
    ['J7', 85, 4],
    ['J8', 68, 5],
    ['J9', 45, 3]
]
maxDeadline = 7   ## maxdeadline =  max(job[2] for job in arr ) 
result = jobSequences(arr , maxDeadline)    
print("MaxProfit when Scheduling Job Like:" , result )





## ---------------Dij kstra's Algorithm ---------------##
#Tc is O((V+E)log(V)) , Sc is O(1) #
from heapq import heappush , heappop 
def dijkstrasAlgo(graph , start_vertex):
    distances = {vertex : float("infinity") for vertex in graph}
    distances[start_vertex] = 0

    pq = [(0 , start_vertex)]
    while len(pq) > 0 :
        current_distance , current_vertex = heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor , weight in graph[current_vertex].items():
            distance = current_distance + weight 

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq , (distance, neighbor))


    return distances



graph = {
    "A":{"B":2 , "C":5, "D":2 , "E":7 , "F":50} ,
    "B":{"C":2, "D":1, "E":2, "F":60},
    "C":{"B":3, "E":3 , "F": 90},
    "D":{"E":1 , "F":3},
    "E":{"D":4 , "F":4},
    "F":{}
}
print(dijkstrasAlgo(graph , "A"))