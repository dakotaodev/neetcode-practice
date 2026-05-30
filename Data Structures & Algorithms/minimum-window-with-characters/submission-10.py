class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        t_count=defaultdict(int)
        window=defaultdict(int)
        l=0

        for c in t:
            t_count[c]+=1
        
        have=0
        target=len(t_count)
        res=[-1,-1]
        res_length=float("infinity")

        for r,c in enumerate(s):

            # add r
            if c in t:
                window[c]+=1
            
            if c in t and window[c]==t_count[c]:
                have+=1
            
            while have==target:

                if (r-l+1)<res_length:
                    res=[l,r]
                    res_length=r-l+1
                if s[l] in t:
                    window[s[l]]-=1

                    if window[s[l]]+1==t_count[s[l]]:
                        have-=1
                l+=1

        return s[res[0]:res[1]+1] if res_length<float("infinity") else "" 