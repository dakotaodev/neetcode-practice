class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window=[]
        l=0
        res=0
        for r,c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l+=1
            window.append(c)
            res=max(res, len(window))

        return res