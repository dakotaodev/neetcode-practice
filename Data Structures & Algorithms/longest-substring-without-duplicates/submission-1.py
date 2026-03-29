class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding windows!
        L=0
        window=set()
        length=0

        for R in range(len(s)):
            # manage duplicates existing in substring
            while s[R] in window:
                window.remove(s[L])
                L+=1
            window.add(s[R])
            length=max(length, len(window))
        
        return length