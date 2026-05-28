class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""

        res=[-1,-1]
        res_length=float("infinity")
        window=defaultdict(int)
        count_t=defaultdict(int)

        for i in range(len(t)):
            count_t[t[i]]+=1

        target=len(count_t)
        have=0
        l=0
        for r,c in enumerate(s):

            if c in t:
                window[c]+=1
            
            if c in t and window[c]==count_t[c]:
                have+=1
            
            while have==target:

                # check if this is better than current answer
                if (r-l+1) < res_length:
                    res_length=r-l+1
                    res=[l,r]
                
                # move in from the left
                if s[l] in t:
                    window[s[l]]-=1
                    if window[s[l]]+1==count_t[s[l]]:
                        have-=1
                l+=1

        return s[res[0]:res[1]+1] if res_length<float("infinity") else ""