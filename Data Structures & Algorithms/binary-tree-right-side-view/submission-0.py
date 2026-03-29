# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        results=[]
        q=deque([root])
        while q:
            curr_length=len(q)
            for i in range(curr_length):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i==curr_length-1:
                    # this is the last node on the level, which must be the right most
                    results.append(node.val)
        return results        