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

        max_diameter=0

        def dfs(root):
            nonlocal max_diameter
            
            # approach: add the height of the left subtree and the right subtree
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            max_diameter=max(max_diameter,left+right)

            return 1+max(right,left)

        
        dfs(root)
        return max_diameter