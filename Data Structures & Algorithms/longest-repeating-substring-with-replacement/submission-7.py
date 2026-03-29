class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length=0
        uniques=set(s)
        for u in uniques:
            l=0
            count=0
            for r,c in enumerate(s):
                if c==u:
                    count+=1

                if (r-l+1)-count<=k:
                    length=max(r-l+1,length)
                
                while r-l+1-count>k:
                    if s[l]==u:
                        count-=1
                    l+=1
                    
        return length