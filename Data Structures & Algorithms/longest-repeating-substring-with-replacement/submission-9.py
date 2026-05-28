class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniques=set(s)
        res=0
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
                res=max(res,(r-l+1))

        return res 