class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        L = 0
        R = len(nums) - 1

        while L <= R:
            if nums[L] < nums[R]:
                minimum = min(minimum, nums[L])
                break

            # binary search
            m = (L+R) // 2
            minimum = min(minimum, nums[m])
            if nums[m] >= nums[L]:
                L = m + 1
            else:
                R = m - 1
        return minimum
