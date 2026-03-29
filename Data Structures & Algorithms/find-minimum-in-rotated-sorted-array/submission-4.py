class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        result=nums[0]

        while l<=r:

            if nums[l]<=nums[r]:
                result=min(result,nums[l])
                return result
            
            m=(l+r)//2
            result=min(result,nums[m])
            if nums[l]<=nums[m]:
                # this does not have our pivot
                l=m+1
            else:
                r=m-1

        return result        