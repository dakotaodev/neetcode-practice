class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        window=[]

        for r,c in enumerate(s):
            while c in window:
                window.remove(s[l])           
                l+=1
            window.append(c)
            longest=max(longest,len(window))

        return longest