# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root: Optional[TreeNode], above: int):
            if not root:
                return
            
            if root.val>=above:
                nonlocal count
                count+=1

            above=max(above, root.val)
            dfs(root.right,above)
            dfs(root.left,above)

        dfs(root,float("-infinity"))
        return count