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
        if not head:
            return head
        
        copies={None:None}

        # create copies with val
        curr=head
        while curr:
            node=Node(x=curr.val)
            copies[curr]=node
            curr=curr.next
        # update copy pointers
        curr=head
        while curr:
            copy=copies[curr]
            copy.next=copies[curr.next]
            copy.random=copies[curr.random]
            copies[curr]=copy
            curr=curr.next

        # return head
        return copies[head]