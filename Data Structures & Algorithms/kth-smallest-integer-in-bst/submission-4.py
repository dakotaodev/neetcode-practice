# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0

        curr=0
        kth=None

        def dfs(root):

            if not root:
                return

            dfs(root.left)
            nonlocal curr
            curr+=1
            if curr==k:
                nonlocal kth
                kth=root.val
            dfs(root.right)
        dfs(root)
        return kth