class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs={}

        for idx, num in enumerate(nums):
            if num not in diffs:
                diffs[target-num]=idx
            else:
                return [diffs[num],idx]