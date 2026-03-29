# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy=ListNode(0,head)
        group_prev=dummy

        while True:

            # identify next group
            kth=self.get_kth(group_prev,k)
            if not kth:
                # exit as there is no longer a group of size k to reverse
                break
            
            group_next=kth.next

            prev,curr=kth.next,group_prev.next
            #kth's next node will point to the start of the next group
            # group_prev's next will give us the start of the new group we are looking to reverse

            while curr!=group_next: # this cant be null, it needs to be the start of the next group
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=group_prev.next # retain the start of the start of the prev group
            group_prev.next=kth
            group_prev=tmp
        
        return dummy.next

    def get_kth(self, node:Optional[ListNode], k:int):
        while node and k>0:
            node=node.next
            k-=1
        return node



