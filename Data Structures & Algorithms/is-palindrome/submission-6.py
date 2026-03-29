class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two potiner
        l,r=0,len(s)-1
        while l<r:

            # check alnum
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            # check
            if s[l].lower()!=s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True
            