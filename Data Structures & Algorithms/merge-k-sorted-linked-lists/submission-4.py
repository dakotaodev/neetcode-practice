# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                res = self.merge(
                    lists[i],
                    lists[i+1] if (i+1) < len(lists) else None
                )
                merged.append(res)
            lists=merged
        return lists[0]

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next 

        if not l1:
            tail.next=l2
        if not l2:
            tail.next=l1
        
        return dummy.next

        