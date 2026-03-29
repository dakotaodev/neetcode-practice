class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        uniques=set(s)
        longest=0

        for u in uniques:

            matches=0
            l=0
            for r,c in enumerate(s):
                # check if c matches u
                if c==u:
                    matches+=1
                # check if we have a valid window
                while (r-l+1-matches) > k:
                    # not valid
                    if s[l]==u:
                        matches-=1
                    l+=1
                longest=max(longest, (r-l+1))
            
        return longest
