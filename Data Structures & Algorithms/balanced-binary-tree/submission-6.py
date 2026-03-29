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
                return True,0

            right,rh=dfs(root.right)
            left,lh=dfs(root.left)

            if left and right and abs(rh-lh)<=1:
                return True, 1+max(rh,lh)
            else:
                return False,0

        return dfs(root)[0] 