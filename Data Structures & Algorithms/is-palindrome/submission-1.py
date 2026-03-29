class Solution:
    def isPalindrome(self, s: str) -> bool:
        # approach = two pointers
        # l = 0, r = end
        # if not alnum, move l/inc and r/dec
        # if equal, move inward
        # exit condition if l>r

        l,r=0,len(s)-1

        while l<r:
            # move if not alnum
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            # check for match
            if s[r].lower() == s[l].lower():
                l+=1
                r-=1
            else:
                print(s[r], s[l])
                return False
        return True
            

        