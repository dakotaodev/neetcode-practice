class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0

        uniques=set(s)
        for u in uniques:
            count=0
            l=0
            for r,c in enumerate(s):
                if c==u:
                    count+=1
                
                while r-l+1-count>k:
                    if s[l]==u:
                        count-=1
                    l+=1
                longest=max(longest,r-l+1)
                
        return longest