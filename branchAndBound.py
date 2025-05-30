"""
import graph
import math
import sys
import queue
import dijkstra
"""
from PythonSalesMan import graph
import math
import sys
import queue
from PythonSalesMan import dijkstra
  
# SalesmanTrackBranchAndBound1 ===================================================

def SalesmanTrackBranchAndBound1(g, visits):
    return graph.Track(g)


# SalesmanTrackBranchAndBound2 ===================================================

def SalesmanTrackBranchAndBound2(g, visits):
    n = len(visits.Vertices)
    matriz_dist = [[0]*n for i in range(n-1)]
    matriz_paths = [[0]*n for i in range(n-1)]
    
    maximos = [0 for i in range(n)]
    minimos = [0 for i in range(n)]
    
    for i in range(n-1):
        dijkstra.Dijkstra(g, visits.Vertices[i])
        for j in range(n):
            if i != j:
                matriz_dist[i][j] = visits.Vertices[j].DijkstraDistance
                path = []
                v = visits.Vertices[j]
                while v != visits.Vertices[i]:
                    path.insert(0, v.predecesor)
                    v = v.predecesor.Origin
                matriz_paths[i][j] = path
    
    for j in range(n): 
        #columna = [matriz_dist[i][j] for i in range(n-1) if i !=j]
        maximos[j] = max([matriz_dist[i][j] for i in range(n-1) if i !=j])
        minimos[j] = min([matriz_dist[i][j] for i in range(n-1) if i !=j])
        
    #primero = visits.Vertices[0]
    #ultimo = visits.Vertices[-1]
    
    superior_global = sys.float_info.max
    sol = [None, sys.float_info.max]
    
    actual_path = [0]
    actual_superior = sum(maximos)
    actual_inferior = sum(minimos)
    actual_dist = 0
    
    cola = queue.PriorityQueue()
    cola.put((actual_inferior, (actual_path, actual_dist, actual_superior)))
    
    while not cola.empty(): 
        actual_inferior, estado = cola.get()
        actual_path, actual_dist, actual_superior = estado[0], estado[1], estado[2]
        
        i = actual_path[-1]
        if i == n-1:     
            if len(actual_path) == n and actual_dist < sol[1] : 
                sol[0], sol[1] = actual_path, actual_dist
            continue
        
        
        if actual_superior < superior_global: 
            superior_global = actual_superior
            
        for j in range(n):
            if j not in actual_path: 
                
                new_inferior = actual_inferior - minimos[j] + matriz_dist[i][j]
                new_superior = actual_superior - maximos[j] + matriz_dist[i][j]
                new_dist = actual_dist + matriz_dist[i][j]
                
                new_path = list(actual_path)
                new_path.append(j)
                
                if new_inferior < superior_global: 
                    
                    cola.put((new_inferior, (new_path, new_dist, new_superior)))   

    track = graph.Track(g)
    print(sol[0], sol[1])
    for index in range(len(sol[0]) - 1):
        i = sol[0][index]
        j = sol[0][index + 1]
        for e in matriz_paths[i][j]:
            track.AddLast(e)
    return track

# SalesmanTrackBranchAndBound3 ===================================================

def SalesmanTrackBranchAndBound3(g, visits):
    return graph.Track(g)
	