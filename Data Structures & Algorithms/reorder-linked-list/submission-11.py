# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode(0,head)     
        # split
        slow,fast=head,head
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
        while head and head2:
            tmp=head.next
            tmp2=head2.next

            head.next=head2
            head2.next=tmp

            head=tmp
            head2=tmp2

        


