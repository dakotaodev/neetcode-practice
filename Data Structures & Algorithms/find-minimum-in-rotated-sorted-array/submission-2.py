class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        result=nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[l]<=nums[r]:
                result=min(result, nums[m])
                return result
            if nums[l]<=nums[m]:
                # lhs does not contain the pivot
                l+=1
            else:
                #rhs does not have the pivot
                r-=1

        return result