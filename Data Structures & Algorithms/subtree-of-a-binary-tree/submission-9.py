# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True
        if self.isSubtree(root.right, subRoot) or self.isSubtree(root.left,subRoot):
            return True
        return False
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val==subRoot.val and self.isSameTree(root.right, subRoot.right) and self.isSameTree(root.left,subRoot.left):
            return True
        return False