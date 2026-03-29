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

        # first create copies of the nodes, with no pointers
        curr=head
        while curr:
            new_node=Node(curr.val)
            copies[curr]=new_node
            curr=curr.next
        
        # now that we have copies, update the copies pointers to the new copies
        curr=head
        while curr:
            copy=copies[curr]
            copy.next=copies[curr.next]
            copy.random=copies[curr.random]
            copies[curr]=copy
            curr=curr.next
        
        # return the head, which we can get from the copies dict
        return copies[head]
