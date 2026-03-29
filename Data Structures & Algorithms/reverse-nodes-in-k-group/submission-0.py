# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # initialize references
        dummy=ListNode(0,head)  # we need a dummy to point to the head
        group_prev=dummy # group_prev will have the node of the last group

        while True:
            kth=self.get_kth(group_prev,k) # get k nodes from current node
            if not kth: # if it is none, then we know that there are left over nodes, do not process
                break
            
            group_next=kth.next # now that we have kth, we need to maintain a reference to the start of the next group

            # reverse the group
            prev,curr=kth.next,group_prev.next # prev must point to the next group 
            while curr!=group_next: # go until current is at the next group
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=group_prev.next # maintain reference 
            group_prev.next=kth # the previous group needs to point to kth, as it is now the head of the group
            group_prev=tmp # move the prev group reference to its original next

        return dummy.next


    def get_kth(self,curr:ListNode,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr 