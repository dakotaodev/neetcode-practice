# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # fast and slow pointers to find halfway point
        slow,fast=head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # slow now is at the half way point. from here, reverse the list
        second=slow.next
        prev=None
        slow.next=prev # we need to create slow as if it the head of a linked list
        while second:
            tmp = second.next
            second.next=prev
            prev=second
            second=tmp
        
        # now that we have a reversed list, we can iterate through and create the new order
        first,second=head, prev
        while second:
            tmp1=first.next
            tmp2=second.next

            first.next=second
            second.next=tmp1

            second=tmp2
            first=tmp1
