# LEETCODE PROBLEM 133 - Clone Graph
# https://leetcode.com/problems/clone-graph/
# -----------------------------------------------------------------------------
# Given a reference of a node in a connected undirected graph, return a deep
# copy (clone) of the graph. Each node in the graph contains a val (int) and a
# list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS - want to get to the deepest node from the starting node then copy info over
        if not node: return None
        visited = {}
        return self.cloneHelper(node, visited)

    def cloneHelper(self, node, visited):
        new_node = Node(node.val, [])
        if node.val not in visited: visited[node.val] = new_node
        for nbr in node.neighbors:
            new_node.neighbors.append(visited[nbr.val] if nbr.val in visited else self.cloneHelper(nbr, visited))
        return new_node
