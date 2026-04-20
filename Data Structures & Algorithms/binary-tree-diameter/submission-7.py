# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0

        def dfs(root):
            if not root:
                return 0

            right=dfs(root.right)
            left=dfs(root.left)
            d=right+left

            nonlocal max_diameter
            max_diameter=max(max_diameter,d)
            return max(right,left)+1
        
        dfs(root)
        return max_diameter