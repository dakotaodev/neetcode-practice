class Solution:
    def findMin(self, nums: List[int]) -> int:
        result=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<=nums[r]:
                # our search space is sorted, return the result
                result=min(result,nums[l])
                return result
            # we have a pivot in our search space
            m=(l+r)//2
            result=min(result,nums[m])
            if nums[l]<=nums[m]:
                # LHS is sorted, no pivot
                l=m+1
            else:
                # rhs is sorted, no pivot
                r=m-1
        
        return result
