class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        uniques=set()
        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l+=1
            uniques.add(s[r])
            res=max(res,len(uniques))                 

        return res