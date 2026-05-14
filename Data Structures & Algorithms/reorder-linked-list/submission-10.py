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
        
        h2 = slow.next
        slow.next=None

        # reverse
        curr=h2
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp

        h2=prev

        # merge
        curr1=head
        curr2=h2

        while curr1 and curr2:
            tmp1=curr1.next
            tmp2=curr2.next

            curr1.next=curr2
            curr2.next=tmp1

            curr1=tmp1
            curr2=tmp2
        
          



