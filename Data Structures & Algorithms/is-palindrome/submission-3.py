class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # approach = two pointers

        l,r=0,len(s)-1

        while l<r:

            # first check that neither are no alnum
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            # use inward traversal two pointer
            if not s[l].lower() == s[r].lower():
                return False
            else:
                l+=1
                r-=1

        return True