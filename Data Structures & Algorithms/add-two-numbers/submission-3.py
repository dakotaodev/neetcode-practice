# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total=str(self.sum_ll(l1)+self.sum_ll(l2))

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

    def sum_ll(self, node: Optional[ListNode]) -> int:
        s=""
        while node:
            s=str(node.val)+s
            node=node.next
        return int(s)
