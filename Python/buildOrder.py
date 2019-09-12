from collections import defaultdict

def buildOrder(projects, deps):
    graph = buildGraph(projects, deps)
    order = []
    while graph:
        if not graph[key]:
            order.append(key)
            graph.remove(key)
        else:
            for node in graph[key]:


def buildGraph(nodes, edges):
    graph = {node: [] for node in nodes}
    print(graph)
    for node, dep in edges:
        graph[node].append(dep)
    return graph

buildOrder(projects=['a', 'b', 'c'], deps=[('a','c'), ('b','c')])
