# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # value to maintain = tuple of (is this balance, height at node)
            if not root:
                return (True, 0)
            
            left=dfs(root.left)
            right=dfs(root.right)

            # is this node balanced?
            if left[0] and right[0] and abs(left[1]-right[1])<=1:
                # this is balanced
                return (True, max(left[1],right[1])+1)
            
            return (False, 0)
        
        return dfs(root)[0]