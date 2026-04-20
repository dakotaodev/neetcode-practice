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
            
            r,rh=dfs(root.right)
            l,lh=dfs(root.left)

            if r and l and abs(rh-lh)<=1:
                return True, max(rh,lh)+1
            else:
                return False, -1
        
        return dfs(root)[0]


