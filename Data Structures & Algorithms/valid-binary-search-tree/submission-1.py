# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        if not root:
            return root
        
        def dfs(root,high,low):

            if not root:
                return True
            
            right=dfs(root.right,high,root.val)
            left=dfs(root.left,root.val,low)

            if right and left and root.val>low and root.val<high:
                return True
            return False

        high,low=float("infinity"),float("-infinity")
        return dfs(root,high,low)