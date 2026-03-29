class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # since we know that there are n + integers and in the range of 1-n,
        # we can treat this as if it were a linked list and apply floyds

        # use slow and fast pointers to find the duplicate
        # this will be the point of intersection
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # then init a second slow pointer, at interate both slow pointers 
        # until the are the same, this is the entry to our cycle, and our dup
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow