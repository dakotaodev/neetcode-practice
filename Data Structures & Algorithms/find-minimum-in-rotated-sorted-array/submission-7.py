class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1

        while l<=r:            
            if nums[l]<=nums[r]:
                return nums[l]
            m=(r+l)//2
            if nums[l]<=nums[m]:
                # this does not contain the pivot
                l=m+1
            else:
                r=m
