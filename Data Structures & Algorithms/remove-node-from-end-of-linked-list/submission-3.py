# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast=head
        dummy=ListNode(val=0, next=head)
        slow=dummy
        # put a pointer n nodes from start
        while n>0:
            fast=fast.next
            n-=1
        # move pointers until end
        while fast:
            slow=slow.next
            fast=fast.next
        # remove nth node connection 
        slow.next=slow.next.next

        return dummy.next
