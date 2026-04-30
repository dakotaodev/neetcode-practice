class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0

        uniques=set(s)

        for u in uniques:
            l=0
            count=0
            for r in range(len(s)):
                c=s[r]
                if c == u:
                    count+=1
                
                while r-l+1-count > k:
                    if s[l]==u:
                        count-=1
                    l+=1
                else:
                    longest=max(longest,r-l+1)

        return longest