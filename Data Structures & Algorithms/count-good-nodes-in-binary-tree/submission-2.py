# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0

        def dfs(root:TreeNode, above):
            nonlocal count
            if not root:
                return
            if root.val>=above:
                count+=1
            
            above=max(root.val,above)
            dfs(root.right,above)
            dfs(root.left,above)
        
        dfs(root,float("-infinity"))
        return count
