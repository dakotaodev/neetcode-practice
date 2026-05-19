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
        
        copies:dict[Node,Node]={} # old, new

        # # first populate all og nodes
        # def dfs(node):
        #     if node in copies:
        #         return
        #     copies[node]=Node(node.val)
        #     for n in node.neighbors:
        #         dfs(n)
        # dfs(node)

        # # now add the neighbors for each copy
        # for old, new in copies.items():
        #     for on in old.neighbors:
        #         new.neighbors.append(copies[on])

        def dfs(node) -> Node:
            if node in copies:
                return copies[node]
            
            copies[node]=Node(node.val)

            for n in node.neighbors:
                copies[node].neighbors.append(dfs(n))
            
            return copies[node]
        
        return dfs(node)


