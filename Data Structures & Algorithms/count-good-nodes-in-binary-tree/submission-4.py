# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0

        def dfs(root: TreeNode, above:int):
            if not root:
                return
            if root.val>=above:
                nonlocal count
                count+=1
            above=max(above,root.val)
            if root.right:
                dfs(root.right,above)
            if root.left:
                dfs(root.left,above)

        dfs(root,-1*math.inf)
        return count