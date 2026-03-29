# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split in half
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
    
        h2=slow.next
        slow.next=None # to break into halves

        # reverse the second half
        curr=h2
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp

        h2=prev
        h1=head
        # merge 
        while h2:
            # maintain ref
            temp_h2_next=h2.next
            temp_h1_next=h1.next

            #merge
            h1.next=h2
            h2.next=temp_h1_next

            #move
            h2=temp_h2_next
            h1=temp_h1_next
