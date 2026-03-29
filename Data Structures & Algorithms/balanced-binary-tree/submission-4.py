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

        
        def dfs(root):
            if not root:
                return True, 0

            left,lh=dfs(root.left)
            right,rh=dfs(root.right)

            if not right or not left:
                return False,0

            if abs(rh-lh)<=1:
                return True, max(rh,lh)+1
            
            return False, 0
            
        return dfs(root)[0]

