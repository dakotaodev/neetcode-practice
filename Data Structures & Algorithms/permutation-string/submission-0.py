class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # find the char counts for len s1 characters of both strings
        s1_count=[0] * 26
        s2_count=[0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1

        # now, check how many current matches there are
        matches=0
        for i in range(26):
            if s1_count[i]==s2_count[i]:
                matches+=1
        
        # sliding window
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True # we made it!
            
            # we didnt, so lets slide the window starting with r
            index=ord(s2[r])-ord('a')
            # increment the count at index to add r
            s2_count[index]+=1
            # check if this creates a match
            if s2_count[index]==s1_count[index]:
                # its a match so we increment
                matches+=1
            # check if there is an off by one, meaning we lost a match
            elif s2_count[index]==s1_count[index]+1:
                # oh no, we lost one back there
                matches-=1
            
            # now we do the same for l
            index=ord(s2[l])-ord('a')
            # decremement the count as we are sliding l
            s2_count[index]-=1
            # check if this creates a match
            if s2_count[index]==s1_count[index]:
                # its a match so we increment
                matches+=1
            # check if there is an off by one, meaning we lost a match
            elif s2_count[index]==s1_count[index]-1:
                # oh no, we lost one back there
                matches-=1
            
            l+=1
            
        return matches==26















