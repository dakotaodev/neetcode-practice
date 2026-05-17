# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1: int = self.converter(l1)
        n2: int = self.converter(l2)

        total=str(n1+n2)
        head=None
        curr=None
        for i in range(len(total)-1,-1,-1):
            new=ListNode(val=int(total[i]))
            if not head:
                head=new
                curr=new
            else:
                curr.next=new
                curr=curr.next
        
        return head

    def converter(self, node: ListNode) -> int:

        res=""

        while node:
            res=str(node.val)+res
            node=node.next
        
        return int(res)