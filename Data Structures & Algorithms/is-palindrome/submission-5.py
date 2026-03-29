class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointer approach - converge to middle
        # skip any chars that are not alnum by moving pointer
        l=0
        r=len(s)-1
        while l<r:
            
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else: 
                return False


        return True