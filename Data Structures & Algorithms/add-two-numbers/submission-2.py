# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # convert ll to ints
        l1_sum=self.ll_to_int(l1)
        l2_sum=self.ll_to_int(l2)
        # sum the ints
        total=str(l1_sum+l2_sum)
        # create sum as linked list
        head=None
        curr=None
        for s in total[::-1]:
            node=ListNode(val=int(s))
            if not head:
                head=node
                curr=node
            else:
                curr.next=node
                curr=curr.next
        
        return head



    def ll_to_int(self, head: Optional[ListNode]) -> int:
        num_str=""
        while head:
            num_str=str(head.val)+num_str
            head=head.next
        return int(num_str)