class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get char counts
        count_t=defaultdict(int)
        for c in t:
            count_t[c]=count_t[c]+1

        # create trackers
        res=[-1,-1]
        res_length=float("infinity")
        window=defaultdict(int)

        # sliding window
        l=0
        needs=len(count_t)
        matches=0
        for r,c in enumerate(s):

            # add to the window
            if c in t:
                window[c]=window[c]+1
                # see if that created a valid match
                if window[c]==count_t[c]:
                    matches+=1

                while matches==needs:
                    
                    if (r-l+1)<res_length:
                        res_length=r-l+1
                        res=[l,r]
                    
                    # remove l and see if it creates a mismatch
                    if s[l] in count_t:
                        window[s[l]]-=1
                        if window[s[l]]+1==count_t[s[l]]:
                            matches-=1
                    l+=1
    

        return s[res[0]:res[1]+1] if res_length!=float("infinity") else ""

