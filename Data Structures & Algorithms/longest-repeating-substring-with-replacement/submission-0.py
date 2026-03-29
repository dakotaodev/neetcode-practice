class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        uniques=set(s)

        for u in uniques:
            count=0
            l=0
            for r,c in enumerate(s):
                # check if the current char is the unique
                if c==u:
                    count+=1
                # shrink current substr until the condition is met with replacements
                while (r-l+1)-count>k:
                    if s[l]==u:
                        count-=1
                    l+=1
                res=max(res, (r-l+1))
        
        return res