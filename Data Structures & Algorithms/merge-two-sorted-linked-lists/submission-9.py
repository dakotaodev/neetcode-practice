# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1 and list2) or (not list1 and not list2):
            return list2
        if not list2 and list1:
            return list1
        
        head: ListNode = None
        tail: ListNode = head
        while list1 and list2:
            curr=None
            if list1.val<=list2.val:
                curr=list1
                list1=list1.next
            else:
                curr=list2
                list2=list2.next
            if not head:
                head=curr
                tail=head
            else:
                tail.next=curr
                tail=tail.next
        
        if not list1:
            tail.next=list2
        elif not list2:
            tail.next=list1
        
        return head



