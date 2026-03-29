# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        curr=ListNode()
        while list1 or list2:
            node = ListNode()
            if list1 and not list2:
                node.val=list1.val
                list1=list1.next
            elif list2 and not list1:
                node.val=list2.val
                list2=list2.next
            elif list1.val <=list2.val:
                node.val=list1.val
                list1=list1.next
            else:
                node.val=list2.val
                list2=list2.next
            
            if not head:
                head=node
            
            curr.next=node
            curr=curr.next

        return head