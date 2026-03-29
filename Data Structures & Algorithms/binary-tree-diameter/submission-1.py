# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        res=0

        def dfs(root):

            if not root:
                return 0
            nonlocal res
            right=dfs(root.right)
            left=dfs(root.left)
            res=max(res,right+left)
            return 1+max(right,left)
        
        dfs(root)
        return res