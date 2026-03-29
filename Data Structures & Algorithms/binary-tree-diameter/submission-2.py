# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # the diameter is really the hieght of a nodes left and right subtree

        if not root:
            return 0
        diameter=0

        def dfs(root):
            nonlocal diameter

            if not root:
                return 0
            
            right=dfs(root.right)
            left=dfs(root.left)
            diameter=max(diameter,right+left)

            return 1+max(right,left)
        dfs(root)
        return diameter
