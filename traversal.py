def bfs(g, s):
    visit = set()
    queue = [s]
    bfsTraversal = []

    while queue:
        node = queue.pop(0)
        if node not in visit:
            bfsTraversal.append(node)
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
    return bfsTraversal

def dfs(g, s):
    visit = set()
    stack = [s]
    dfsTraversal = []

    while stack:
        node = stack.pop()
        if node not in visit:
            dfsTraversal.append(node)
            visit.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visit:
                    stack.append(neighbor)
    
    return dfsTraversal
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
sNode = 1
print("BFS starting from node", sNode, " ", bfs(graph, sNode))
print("DFS starting from node", sNode, " ", dfs(graph, sNode))