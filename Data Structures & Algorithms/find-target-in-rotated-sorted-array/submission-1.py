class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            
            # check if the lhs is sorted
            if nums[l]<=nums[m]:
                # lhs is sorted, check if we are in the bounds of lhs
                if target > nums[m] or target<nums[l]:
                    # we are outside, constrain to rhs
                    l=m+1
                else:
                    # we are possibly in the range of lhs, constrain to lhs
                    r=m-1
            else:
                # this means we are in the rhs and the lhs has the pivot
                # check if we are in the bounds of rhs
                if target<nums[m] or target>nums[r]:
                    # we are not in the bounds of rhs, move to lhs
                    r=m-1
                else:
                    # we are in the bounds of rhs, constrain
                    l=m+1

        return -1