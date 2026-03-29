# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return root
        count=k
        res=root.val
        def dfs(root):       
            if not root:
                return
            
            dfs(root.left)
            nonlocal count
            count-=1
            if count==0:
                nonlocal res
                res=root.val
                return
            dfs(root.right)
            return
        dfs(root)
        return res