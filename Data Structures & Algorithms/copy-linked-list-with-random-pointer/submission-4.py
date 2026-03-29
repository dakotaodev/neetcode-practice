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
        copies={None:None}

        # first, create copies
        curr=head
        while curr:
            copies[curr]=Node(x=curr.val)
            curr=curr.next
        
        # create links
        curr=head
        while curr:
            copy=copies[curr]
            copy.next=copies[curr.next]
            copy.random=copies[curr.random]
            copies[curr]=copy
            curr=curr.next
        
        return copies[head]



