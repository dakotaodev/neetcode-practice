# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0

        def dfs(root, above):
            if not root:
                return
            
            dfs(root.left,max(root.val,above))
            dfs(root.right,max(root.val,above))

            nonlocal count
            if root.val>=above:
                count+=1
            
        dfs(root, float("-infinity"))
        return count