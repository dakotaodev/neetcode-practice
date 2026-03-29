class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # approach
        # diffs will be a dict of target-num: idx
        # if num in diffs, return the current index plus the value
        # if not, add to diffs

        diffs: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], idx]
            diffs[target-num]=idx
                