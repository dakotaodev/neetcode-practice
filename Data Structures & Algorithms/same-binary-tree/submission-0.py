# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and q or (not q and p):
            return False
        
        if not p and not q:
            return True

        
        if (
            self.isSameTree(p.right, q.right)
            and self.isSameTree(p.left, q.left)
            and (p.val == q.val) and (q.val==p.val)
        ):
            return True
        
        return False

        