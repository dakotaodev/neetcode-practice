# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total:str=str(self.sum_ll(l1)+self.sum_ll(l2))
        dummy=ListNode()
        tail=dummy
        for i in range(len(total)-1,-1,-1):
            node=ListNode(val=int(total[i]))
            tail.next=node
            tail=tail.next
        return dummy.next

    def sum_ll(self, node: Optional[ListNode]):
        res=""
        while node:
            res=str(node.val)+res
            node=node.next
        return int(res)