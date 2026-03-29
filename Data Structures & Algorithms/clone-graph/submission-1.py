"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited={None:None}

        def dfs(node):
            if node in visited:
                return visited[node]
            copy=Node(node.val)
            visited[node]=copy
            for n in node.neighbors:
                nc=dfs(n)
                copy.neighbors.append(nc)
            return copy
        return dfs(node)