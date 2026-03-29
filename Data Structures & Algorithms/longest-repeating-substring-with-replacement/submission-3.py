class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        uniques=set(s)
        longest=0
        for u in uniques:
            matches=0
            l=0
            for r,c in enumerate(s):
                if c==u:
                    matches+=1
                
                count=r-l+1-matches

                while count > k:
                    if s[l]==u:
                        matches-=1
                    l+=1
                    count=r-l+1-matches
                longest=max(longest,r-l+1)
            
        return longest