# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # given: root node of tree
        # ask: find depth of tree (max length from root to leaf)
        # root counts for the length
        # return: max length
        # approach: BFS
        
        if not root:
            return 0
        
        # initialize
        queue=deque()
        queue.append(root)
        max_length=1
        current_length=1

        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if not node.right and not node.left:
                    max_length=max(max_length, current_length)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            current_length+=1

        return max_length

