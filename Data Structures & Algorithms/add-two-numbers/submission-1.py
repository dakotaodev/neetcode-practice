# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_num = self.list_to_int(l1)
        l2_num = self.list_to_int(l2)

        total:str = str(l1_num+l2_num)

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


    def list_to_int(self, node: Optional[ListNode]) -> int:

        num_str=""
        while node:
            num_str=str(node.val)+num_str
            node=node.next
        
        return int(num_str)

    