class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        if self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot):
            return True
        return False
    
    def isSameTree(self, root,subroot):
        if not root and not subroot:
            return True
        
        if root and subroot and root.val==subroot.val and self.isSameTree(root.right, subroot.right) and self.isSameTree(root.left,subroot.left):
            return True
        return False