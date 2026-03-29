class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        minimum=nums[0]

        while l<=r:
            # check if our search space is sorted
            if nums[l]<=nums[r]:
                minimum=min(minimum, nums[l])
                break
            
            # not sorted
            m=(l+r)//2
            minimum=min(minimum, nums[m])
            if nums[m]>=nums[l]:
                # we then know that the lhs is sorted, we need to reduce space to the right of this
                l=m+1
            else:
                # we then know that the lhs is unsorted, meaning the middle is a viable candidate, lets search left of it
                r=m-1
            
        return minimum