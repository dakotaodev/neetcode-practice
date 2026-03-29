# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        results=0

        def dfs(root,above_max):
            
            if not root: 
                return

            nonlocal results
            if root.val>=above_max:
                results+=1

            above_max=max(above_max,root.val)
            dfs(root.left,above_max)
            dfs(root.right,above_max)

        dfs(root,float("-infinity"))
        return results
