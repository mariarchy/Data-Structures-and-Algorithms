def isValidTree(n, edges):
    if n == 0 or not edges: return True

    adj_list = buildGraph(n, edges)

    visited = [0 for _ in range(n)]
    return checkTree(0, adj_list, visited, -1) and all(marker for marker in visited)

    # starting at node 0
    # mark as visited
    # for all adj nodes
        # if node is not visited, visit and check if cycle
        # if node is visited, check if we arrived at this node from a previous edge or new edge
        #   if new edge AKA if cycle return False
        #   if thru parent node, continue
    # for i in range(n) if val == 0 return False
    # return True
def checkTree(node, graph, visited, parent):
    visited[node] = 1
    for adj in graph[node]:
        if not visited[adj]:
            if not checkTree(adj, graph, visited, node): return False
        else:
            # if the visited adj node isn't a visited parent, ret False
            if parent != adj: return False
    print(visited)
    return True



def buildGraph(n, edges):
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

print(isValidTree(5, [[4,0],[1,2],[2,3],[3,4]]))
print(isValidTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(isValidTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
