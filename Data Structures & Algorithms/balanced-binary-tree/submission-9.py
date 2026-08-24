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

        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:

            if not root: 
                return True, 0
            
            l, lh = dfs(root.left)
            r, rh = dfs(root.right)

            if l and r and abs(lh -rh) <=1:
                return True, max(lh,rh)+1
            else:
                return False, -1

        r, rh = dfs(root)
        return r