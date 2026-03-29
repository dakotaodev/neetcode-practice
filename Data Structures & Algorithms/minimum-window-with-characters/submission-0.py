class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        count_t,window={},{}

        # get the counts for t
        for c in t:
            count_t[c]=count_t.get(c,0)+1
        
        need,have=len(count_t),0
        res=[-1,-1]
        res_length=float("infinity")

        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1

            if c in count_t and window[c]==count_t[c]:
                have +=1
            
            while have==need:

                if (r-l+1)<res_length:
                    res=[l,r]
                    res_length=(r-l+1)
                
                window[s[l]]-=1
                if s[l] in count_t and window[s[l]]<count_t[s[l]]:
                    have-=1
                l+=1
        
        l,r=res
        return s[l:r+1] if res_length!=float('infinity') else ""





