# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        i=0
        res=None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal i
            i+=1
            if i==k:
                nonlocal res
                res=root.val
                return
            dfs(root.right)
        dfs(root)
        return res