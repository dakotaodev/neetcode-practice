class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {} # key = difference, value = index
        for i, n in enumerate(nums):
            if n in seen:
                return [seen[n], i]
            diff = target - n
            seen[diff]=i
        
