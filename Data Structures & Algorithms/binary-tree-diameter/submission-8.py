# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            nonlocal res
            res = max(res, rh+lh)

            return 1 + max(rh,lh)

        dfs(root)
        return res