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

        # make a copy of the nodes
        curr=head
        while curr:
            copies[curr]=Node(x=curr.val)
            curr=curr.next 
        
        # wire up the pointers
        curr=head
        while curr:
            c=copies[curr]
            c.next=copies[curr.next]
            c.random=copies[curr.random]
            copies[curr]=c
            curr=curr.next
        
        return copies[head]