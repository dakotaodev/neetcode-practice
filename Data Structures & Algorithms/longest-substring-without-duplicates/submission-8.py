class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        window=set()
        res=0
        for r,c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l+=1
            window.add(c)
            res=max(res,len(window))
    
        return res
