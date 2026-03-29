class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0

        for n in nums:
            if n-1 not in nums:
                # new candidate sequence
                curr=1
                while n+1 in nums:
                    curr+=1
                    n+=1
                longest=max(longest,curr)
        return longest