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

        def dfs(root, least, most):
            if not root:
                return True

            left=dfs(root.left,least,root.val)
            right=dfs(root.right,root.val,most)

            if left and right and root.val>least and root.val<most:
                return True
            return False

        return dfs(root,float("-infinity"),float("infinity")) 