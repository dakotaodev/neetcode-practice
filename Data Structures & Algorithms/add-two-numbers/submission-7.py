# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=, NoDefault0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=self.sumNode(l1)
        n2=self.sumNode(l2)
        total=str(n1+n2)

        head=None
        curr=None
        for i in range(len(total)-1, -1,-1):
            n=int(total[i])
            node=ListNode(val=n)
            if not head:
                head=node
                curr=node
            else:
                curr.next=node
                curr=curr.next

        return head
    
    def sumNode(self, node:Optional[ListNode]) -> int:
        res=""

        while node:
            res=str(node.val)+res
            node=node.next
        return int(res)




