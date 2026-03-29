# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move the fast pointer n nodes
        # we are able to remove the head, so create a dummy that points to it
        # then we can move fast and slow until it reaches None
        #from there we can remove the node
        # return dummy next
        dummy=ListNode(0, head)
        slow=dummy
        fast=head
        while n>0:
            fast=fast.next
            n-=1
        
        while fast:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next
        return dummy.next


