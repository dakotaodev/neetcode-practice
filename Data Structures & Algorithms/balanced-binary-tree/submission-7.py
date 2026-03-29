# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True,0
            
            left,lh=dfs(root.left)
            right,rh=dfs(root.right)

            if left and right and abs(rh-lh)<=1:
                return True,1+max(lh,rh)
            return False,-1
        
        res,_=dfs(root)
        return res