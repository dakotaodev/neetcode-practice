# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # check if root
        if not root:
            return False

        # check if root is a leaf node and targetSum is 0
        if not root.right and not root.left and targetSum-root.val==0:
            return True

        # not a leaf node with the target sum, explore the subtrees
        if self.hasPathSum(root.left, targetSum-root.val):
            return True
        if self.hasPathSum(root.right,targetSum-root.val):
            return True

        return False 