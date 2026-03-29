class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        # get the character count of t and the window of s of length t
        count_t={}
        window={}
        for c in t:
           count_t[c]=1+count_t.get(c,0)
        # create the trackers of matching freqs
        res=[-1,-1]
        res_length=float("infinity")
        have=0
        need=len(count_t)

        l=0
        for r,c in enumerate(s):
            # add to window
            window[c]=window.get(c,0)+1
            # check if c is a char we care about
            if c in count_t and window[c]==count_t[c]:
                have+=1
            
            # check if we have a valid window
            while have==need:
                # we do, lets store the results if they beat the current
                if (r-l+1)<res_length:
                    res_length=r-l+1
                    res=[l,r]
                
                # shrink the window to see if we can find a smaller substring
                cl=s[l]
                window[cl]-=1
                if cl in count_t and window[cl] < count_t[cl]:
                    have -= 1

                l+=1
        l,r=res
        return s[l:r+1] if res_length!=float("infinity") else ""
