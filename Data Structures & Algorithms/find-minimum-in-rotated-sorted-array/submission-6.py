class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            m=(l+r)//2
            if nums[l]<=nums[r]:
                return min(res,nums[l]) 
            res=min(res,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m
        return res