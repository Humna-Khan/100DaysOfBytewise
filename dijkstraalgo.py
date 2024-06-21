def dijkstraAlgo(g, s):
    dist = {node: float('inf') for node in graph}
    dist[s] = 0
    
    visit = set()
    
    while len(visit) < len(graph):
        minNode = None
        minDistance = float('inf')
        
        for node in graph:
            if node not in visit and dist[node] < minDistance:
                minNode = node
                minDistance = dist[node]
        
        if minNode is None:
            break
        visit.add(minNode)
        
        for neighbor, weight in graph[minNode].items():
            newDist = dist[minNode] + weight
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
    
    return dist

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

sNode = 'A'
shortPaths = dijkstraAlgo(graph, sNode)
print("Shortest paths from node", sNode + " ", shortPaths)