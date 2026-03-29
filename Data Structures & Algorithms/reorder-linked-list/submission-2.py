# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the head of half way
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        h2=slow.next
        # we need to break the list in two
        slow.next=None

        ## reverse the second half
        curr=h2
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        
        h2=prev

        # now that I have the two, we can merge
        h1=head
        while h2:
            #maintain ref
            tempH1=h1.next
            tempH2=h2.next

            # reorder
            h1.next=h2
            h2.next=tempH1
            # move
            h1=tempH1
            h2=tempH2


