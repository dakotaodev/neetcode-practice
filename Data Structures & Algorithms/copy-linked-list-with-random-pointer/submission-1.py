"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # old, new
        copies={None: None}
        
        # create new nodes
        curr=head
        while curr:
            new=Node(curr.val)
            copies[curr]=new
            curr=curr.next

        # update new nodes
        curr=head
        while curr:
            new=copies[curr]
            new.next=copies[curr.next]
            new.random=copies[curr.random]
            copies[curr]=new
            curr=curr.next
        
        return copies[head]

        
