# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1,l2=list1,list2

        if not l1 and not l2:
            return l1
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        
        current = None
        head = None
        while l1 or l2:
            print(f"l1:{l1.val if l1 else None}, l2:{l2.val if l2 else None}")
            node=ListNode()
            if not l1 and l2:
                node.val=l2.val
                l2=l2.next
            elif not l2 and l1:
                node.val=l1.val
                l1=l1.next
            elif l1.val<=l2.val:
                node.val=l1.val
                l1=l1.next
                print("hit")
            elif l1.val>l2.val:
                node.val=l2.val
                l2=l2.next
            if current == None:
                current=node
                head=node
            else:
                current.next=node
                current=current.next
        
        return head
            



