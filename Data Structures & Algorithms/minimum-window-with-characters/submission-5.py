class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res=[-1,-1]
        res_length=float("infinity")
        count_t=defaultdict(int)
        window=defaultdict(int)

        # initialize count_t
        for c in t:
            count_t[c]+=1
        
        target=len(count_t)
        have=0

        # sliding window
        l=0
        for r,c in enumerate(s):
            if c in t:
                window[c]+=1
            
            if c in t and window[c]==count_t[c]:
                have+=1
            
            while have==target:
                if (r-l+1) < res_length:
                    res_length=r-l+1
                    res=[l,r]

                # try to shrink from the left
                if s[l] in t:
                    window[s[l]]-=1
                    if window[s[l]]+1==count_t[s[l]]:
                        have-=1
                l+=1
        
        return s[res[0]:res[1]+1] if res_length!=float("infinity") else ""









