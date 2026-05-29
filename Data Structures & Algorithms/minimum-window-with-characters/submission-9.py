class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window=defaultdict(int)
        t_count=defaultdict(int)

        for c in t:
            t_count[c]+=1
        
        total=len(t_count)
        have=0
        l=0
        res=[-1,-1]
        res_length=float("infinity")

        for r,c in enumerate(s):

            # add to the window
            window[c]+=1
            if window[c]==t_count[c]:
                have+=1

            while have==total:

                if (r-l+1)<res_length:
                    res_length=r-l+1
                    res=[l,r]
                
                # shrink from the left
                window[s[l]]-=1
                if window[s[l]]+1==t_count[s[l]]:
                    have-=1
                l+=1

        return s[res[0]:res[1]+1] if res_length<float("infinity") else ""