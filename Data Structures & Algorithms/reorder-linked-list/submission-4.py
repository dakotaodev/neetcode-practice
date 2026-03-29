# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split list in half
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        h2=slow.next
        slow.next=None 
        # reverse the second half
        curr=h2
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp

        h2=prev 
        # merge
        h1=head
        while h2:
            h1_temp=h1.next
            h2_temp=h2.next

            h1.next=h2
            h2.next=h1_temp

            h1=h1_temp
            h2=h2_temp
                    