class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0

        for num in nums:
            if num-1 not in nums:
                l=1
                while num+1 in nums:
                    num+=1
                    l+=1
                longest=max(longest,l)
        return longest
