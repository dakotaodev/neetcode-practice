# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,above):
            if not root:
                return
            if root.val>=above:
                nonlocal count
                count+=1
            above=max(root.val,above)
            dfs(root.right,above)
            dfs(root.left,above)
            return 
        dfs(root,float("-infinity"))
        return count