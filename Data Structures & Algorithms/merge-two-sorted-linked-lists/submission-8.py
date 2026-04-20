# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif list1 and not list2:
            return list1
        
        head=None
        curr=None
        while list1 and list2:
            new=None

            if list1.val<=list2.val:
                new=list1
                list1=list1.next
            else:
                new=list2
                list2=list2.next
            if not head:
                head=new
                curr=new
            else:
                curr.next=new
                curr=curr.next
            
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        
        return head














