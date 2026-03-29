# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total=str(self.sum_ll(l1) + self.sum_ll(l2))
        output=""
        current=ListNode(val=int(total[-1]))
        head=None
        for i in range(len(total)-2, -1, -1):
            num=int(total[i])
            node=ListNode(val=num)
            current.next=node
            if head is None:
                head=current
            current=current.next
        
        return head if head else current
    
    def sum_ll(self, node: Optional[ListNode]) -> int:
        num_str = ""
        while node:
            num_str = str(node.val) + num_str
            node=node.next
        return int(num_str)