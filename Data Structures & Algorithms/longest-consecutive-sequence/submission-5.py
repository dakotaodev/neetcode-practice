class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        for n in nums:
            if n-1 not in nums:
                curr=0
                while n in nums:
                    curr+=1
                    n+=1
                longest=max(longest,curr)
        return longest            