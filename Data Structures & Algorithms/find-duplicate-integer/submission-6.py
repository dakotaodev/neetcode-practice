class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # find intersection
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        # now find entry of cycle
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow