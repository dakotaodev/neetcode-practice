class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}
        for idx, num in enumerate(nums):
            diff=target-num
            if num in seen:
                return [seen[num], idx]
            seen[diff]=idx