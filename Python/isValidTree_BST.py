from collections import deque

def isValidTree(n, edges):
    if n == 0 or not edges: return True

    adj_list = buildGraph(n, edges)

    visited = [0 for _ in range(n)]
    queue = deque([0])
    return checkTree(queue, adj_list, visited) and all(marker for marker in visited)

    # starting at node 0
    # mark as visited
    # for all adj nodes
        # if node is not visited, visit and check if cycle
        # if node is visited, check if we arrived at this node from a previous edge or new edge
        #   if new edge AKA if cycle return False
        #   if thru parent node, continue
    # for i in range(n) if val == 0 return False
    # return True
def checkTree(queue, graph, visited):
    parent_list = [-1 for _ in range(len(graph))]
    while queue:
        parent = queue.popleft()
        visited[parent] = 1
        for adj_node in graph[parent]:
            if not visited[adj_node]:
                parent_list[adj_node] = parent
                queue.append(adj_node)
            elif parent_list[parent] != adj_node:
                return False

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
