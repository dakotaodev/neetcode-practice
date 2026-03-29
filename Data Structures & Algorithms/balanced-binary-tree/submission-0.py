# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root)->list[bool, int]:
            # return of [is_balanced, height at node]
            if not root:
                return [True, 0]
            
            # find [is_balanced, height] for the left and right subtree
            left=dfs(root.left)
            right=dfs(root.right)

            # to be balanced, left and right must be balanaced 
            # and the height between the two must not have a difference>1
            is_balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            # return is balanced and the height of this node (height of tallest subtree plus 1 for the current node)
            return [is_balanced, 1+max(left[1],right[1])]
        
        return dfs(root)[0]