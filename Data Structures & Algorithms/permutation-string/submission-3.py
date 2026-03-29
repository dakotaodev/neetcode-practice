class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        # get the initial char acounts
        s1_count=[0] * 26
        s2_count=[0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]=s1_count[ord(s1[i])-ord('a')]+1        
            s2_count[ord(s2[i])-ord('a')]=s2_count[ord(s2[i])-ord('a')]+1

        # count the number of matches
        matches=0
        for i in range(len(s1_count)):
            if s1_count[i]==s2_count[i]:
                matches+=1

        # sliding window
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            # add to window
            index=ord(s2[r])-ord('a')
            s2_count[index]=s2_count[index]+1
            # check if we created a mismatch
            if s1_count[index]+1==s2_count[index]:
                matches-=1
            elif s1_count[index]==s2_count[index]:
                matches+=1
            
            # remove from window
            index=ord(s2[l])-ord('a')
            s2_count[index]=s2_count[index]-1
            # check if we created a mismatch
            if s1_count[index]-1==s2_count[index]:
                matches-=1
            elif s1_count[index]==s2_count[index]:
                matches+=1
            l+=1
        
        return matches == 26