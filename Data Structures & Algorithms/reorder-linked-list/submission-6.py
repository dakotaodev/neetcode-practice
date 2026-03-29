# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split in half
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        h2=slow.next
        slow.next=None # break in two

        # reverse second half
        prev=None
        curr=h2
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        rev=prev

        # merge
        curr=head
        while rev:
            # maintain ref to break
            tmp_rev=rev.next
            tmp_curr=curr.next

            # merge
            curr.next=rev
            rev.next=tmp_curr

            # move
            rev=tmp_rev
            curr=tmp_curr


            