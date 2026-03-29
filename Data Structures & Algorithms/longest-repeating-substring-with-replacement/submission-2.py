class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniques=set(s)
        longest=0

        for i,u in enumerate(uniques):
            count=0
            l=0
            r=0
            while r<len(s):
                if s[r]==u:
                    count+=1

                if (r-l+1)-count>k:
                    if s[l]==u:
                        count-=1
                    l+=1
                else:
                    longest=max(longest,(r-l+1))
                    r+=1
        return longest