class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="": 
            return ""

        count_t,window={},{}
        res_length=float("infinity")
        res=[-1,-1]

        # count characters in t
        for c in t:
            count_t[c]=count_t.get(c,0)+1
            
        have,need=0,len(count_t)
        
        l=0
        for r,c in enumerate(s):

            # first, add r to the window
            window[c]=window.get(c,0)+1
            if c in count_t and count_t[c]==window[c]:
                have+=1
            
            while have==need:
                if (r-l+1)<res_length:
                    res=[l,r]
                    res_length=r-l+1
                char_l = s[l]
                window[char_l]-=1
                if char_l in count_t and window[char_l] < count_t[char_l]:
                    have-=1
                l+=1
        
        l,r=res
        return s[l:r+1] if res_length!=float("infinity") else ""
