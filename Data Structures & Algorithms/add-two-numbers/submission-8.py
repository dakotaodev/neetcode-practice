# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total:str=str(self.convert(l1)+self.convert(l2))
        curr=None
        head=None
        for i in range(len(total)-1,-1,-1):
            node=ListNode(val=int(total[i]))
            if head==None:
                head=node
                curr=node
            else:
                curr.next=node
                curr=curr.next
        
        return head

    def convert(self, node: Optional[ListNode])->int:
        res=""

        while node:
            res=str(node.val)+res
            node=node.next

        return int(res)