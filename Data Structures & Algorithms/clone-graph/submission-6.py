"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copies={None:None}

        def dfs(node:Node):
            if node in copies:
                return copies[node]
            
            new=Node(node.val)
            copies[node]=new
            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return copies[node]
        
        dfs(node)
        return copies[node]