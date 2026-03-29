# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total=self.sum_ll(l1)+self.sum_ll(l2)
        total=str(total)
        head=None
        curr=None
        for c in total[::-1]:
            node=ListNode(val=int(c))
            if not head:
                head=node
                curr=node
            else:
                curr.next=node
                curr=curr.next
        return head


    def sum_ll(self,node: Optional[ListNode]) -> int:
        res=""
        while node:
            res=str(node.val)+res
            node=node.next
        return int(res)