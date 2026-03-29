class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,0
        boundary=len(nums)

        while r<boundary:
            nums[l]=nums[r]
            # search
            while r <boundary and nums[l]==nums[r]:
                r+=1
            # search ended, increment unique pos pointer
            l+=1
        
        return l