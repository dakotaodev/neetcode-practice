# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # split
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        h2=slow.next
        slow.next=None

        # reverse
        curr=h2
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        
        head2=prev

        # merge
        curr=head
        curr2=head2
        while curr and curr2:
            tmp=curr.next
            tmp2=curr2.next

            curr.next=curr2
            curr2.next=tmp

            curr=tmp
            curr2=tmp2




