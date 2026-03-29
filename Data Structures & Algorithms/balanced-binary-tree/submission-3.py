# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def dfs(node):
            
            if not node:
                return (True, 0)

            # maintain the tuple (is_balanced, height)
            right=dfs(node.right)
            left=dfs(node.left)
            if (
                right[0] and left[0] and abs(right[1]-left[1])<=1
            ):
                return (True, max(right[1],left[1]) + 1)
            
            return (False, 0)
        
        return dfs(root)[0]