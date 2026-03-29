# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=k
        result=root.val

        def dfs(root):
            if not root:
                return
            
            nonlocal result, count
            dfs(root.left)
            count-=1
            if count==0:
                result=root.val
                return
            
            dfs(root.right)
            return
        
        dfs(root)

        return result