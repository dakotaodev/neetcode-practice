# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root: Optional[TreeNode], low:int, high:int):

            if not root:
                return True

            left=dfs(root.left,low, root.val)
            right=dfs(root.right,root.val,high)

            if right and left and root.val<high and root.val>low:
                return True
            return False

        return dfs(root,float("-infinity"),float("infinity"))