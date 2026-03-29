# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        
        head=None
        curr=None
        while list1 or list2:
            node=None
            if not list1: 
                node=list2
                list2=list2.next
            elif not list2:
                node=list1
                list1=list1.next
            elif list1.val<=list2.val:
                node=list1
                list1=list1.next
            else:
                node=list2
                list2=list2.next
            
            if not curr:
                curr=node
                head=node
            else:
                curr.next=node
                curr=curr.next
        return head

